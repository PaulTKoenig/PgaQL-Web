<script lang="ts">
  import { onMount } from 'svelte';
  import { Chart, Grid, NbaqlHeader, NbaqlSidebar, QueryBuilder, QueryNotebook } from '$lib';

  let submittedQuery = $state("");
  let queryTab = $state(0);

  const updateQueryTab = (updatedTab) => {
      queryTab=updatedTab;
  }

  let data = $state({});
  let error = $state(null);
  let loading = $state(false);
  let playerData = new Map();

  async function fetchPlayerData(playerIds) {
    let error = null;

    try {
      const response = await fetch("/api/get-player-details", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ player_ids: playerIds })
      });

      if (!response.ok) {
        throw new Error('Sorry something went wrong. Please try again');
      }

      const responseJson = await response.json();
      return responseJson;
    } catch (err) {
      error = err.message;
      console.error(error);
    }
  }

  async function loadPlayerData() {
    const playerIds = data.rowData.map(item => item[0]);
    const players = fetchPlayerData(playerIds);
    console.log(await players);
    playerData = new Map((await players).map(player => [player.playerId, `${player.firstName} ${player.lastName}`]));
  }

  async function fetchData(e) {
    loading = true;
    error = null;
    let input = e.detail.input;

    try {
      const encodedQuery = encodeURIComponent(input);
      const response = await fetch(`/api/interpret-query?query=${encodedQuery}`);
      
      if (!response.ok) {
        if (response.status === 400) {
          throw new Error('Invalid grammar');
        } else {
          throw new Error('Sorry something went wrong. Please try again');
        }
      }

      data = await response.json();
      submittedQuery=input;

      await loadPlayerData();
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>


<NbaqlHeader />
<div class="lg:flex">
  <div class="w-full xl:w-1/3 2xl:w-1/4 mx-auto pb-10">
    <NbaqlSidebar />
  </div>

  <div class="flex flex-col gap-10 w-full lg:w-2/3 xl:w-3/4 mx-auto">
    <div class="nbaql-main-container">
      <div class="nbaql-tabs flex mb-10">
        <div class="nbaql-query-tab" class:nbaql-query-tab-active={queryTab === 0} onclick={() => updateQueryTab(0)}>
          Query Builder
        </div>
        <div 
          class="nbaql-query-tab" class:nbaql-query-tab-active={queryTab === 1} onclick={() => updateQueryTab(1)}
        >Query Notebook</div>
        <!-- <div 
          class="w-1/3 border-b hover:shadow-lg focus:shadow-lg cursor-pointer p-3 transition-all"
        >NL Search</div> -->
      </div>

      <div class="p-5">
        {#if queryTab === 0}
          <QueryBuilder on:submit={fetchData} />
        {:else if queryTab === 1}
          <QueryNotebook on:submit={fetchData} />
        {:else}
          ah shit
        {/if}
        
      </div>
    </div>

    <div class="nbaql-chart-container mx-auto" class:hidden={!loading && !error && (!("rowData" in data) || data.rowData?.length === 0)}>
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.rowData?.length > 0}
      <div class="pt-5">
        <Chart {data} {playerData} />
      </div>
      {/if}
    </div>

    <div class="nbaql-chart-container mx-auto" class:hidden={error || (!loading && (!("rowData" in data) || data.rowData?.length === 0))}>
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.rowData?.length > 0}
      <div>
        <Grid {data} {playerData} />
      </div>
      {/if}
    </div>
  </div>
</div>

<style>

    .nbaql-main-container, .nbaql-menu-container, .nbaql-chart-container {
      padding: 3rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
    }

    .pt-nav {
        padding-top: max(3.5rem, 10vh);
    }

    .nbaql-tabs {
      border: 1px solid #222222;
      border-radius: 4px;
    }

    .nbaql-query-tab {
      width: 50%;
      cursor: pointer;
      padding: 0.75rem;
      display: flex;
      justify-content: center;
      border-radius: 4px;
    }

    .nbaql-query-tab:hover {
      text-decoration: underline;
    }

    .nbaql-query-tab-active {
      transition-property: all;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
      transition-duration: 150ms;

      --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 1);
      box-shadow: var(--tw-ring-offset-shadow, 0 0 #fff), var(--tw-ring-shadow, 0 0 #fff), var(--tw-shadow);
    }
    .nbaql-query-tab-active:hover {
      border: initial;
    }
</style>