<script lang="ts">
  import { onMount } from 'svelte';
  import { Chart } from '$lib';
  import { QueryBuilder, QueryNotebook } from '$lib';

  let submittedQuery = $state("");
  let queryTab = $state(0);

  const updateQueryTab = (updatedTab) => {
      queryTab=updatedTab;
  }

  let data = $state([]);
  let error = $state(null);
  let loading = $state(false);

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
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>


<div class="flex">
  <div class="w-1/3 xl:w-1/4 mx-auto pb-20">
    <div class="pgaql-menu-container">
      <p class="font-bold">
        Welcome to PgaQL. This is an interactive UI to build queries with the language the query language 'PgaQL' allowing users to easily search and chart trends for their favorite athletes and teams
      </p>
      <p class="py-10">
        Example: CHART box_score IN scatter_plot FOR fga VS fgm WHERE team_abbr = 'CLE'
      </p>
      <p class:font-bold={true}>
        Build a Query
      </p>
      <p>
        Read Documentation
      </p>
    </div>
  </div>

  <div class="flex flex-col gap-10 w-2/3 xl:w-3/4 mx-auto pb-20">
    <div class="pgaql-main-container">
      <div class="pgaql-tabs flex mb-10">
        <div class="pgaql-query-tab" class:pgaql-query-tab-active={queryTab === 0} onclick={() => updateQueryTab(0)}>
          Query Builder
        </div>
        <div 
          class="pgaql-query-tab" class:pgaql-query-tab-active={queryTab === 1} onclick={() => updateQueryTab(1)}
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
    <div class="pgaql-chart-container mx-auto" class:hidden={!loading && !error && data.length === 0}>
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.length > 0}
      <div class="pt-5">
        {submittedQuery}
        <Chart {data} />
      </div>
      {/if}
    </div>
  </div>
</div>

<style>

    .pgaql-main-container, .pgaql-menu-container, .pgaql-chart-container {
      padding: 3rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
    }

    .pt-nav {
        padding-top: max(3.5rem, 10vh);
    }

    .pgaql-tabs {
      border: 1px solid #222222;
      border-radius: 4px;
    }

    .pgaql-query-tab {
      width: 50%;
      cursor: pointer;
      padding: 0.75rem;
      display: flex;
      justify-content: center;
      border-radius: 4px;
    }

    .pgaql-query-tab:hover {
      text-decoration: underline;
    }

    .pgaql-query-tab-active {
      transition-property: all;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
      transition-duration: 150ms;

      --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 1);
      box-shadow: var(--tw-ring-offset-shadow, 0 0 #fff), var(--tw-ring-shadow, 0 0 #fff), var(--tw-shadow);
    }
    .pgaql-query-tab-active:hover {
      border: initial;
    }
</style>