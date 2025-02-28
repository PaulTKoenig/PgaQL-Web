<script lang="ts">
  import { onMount } from 'svelte';
  import { Chart } from '$lib';
	let input = $state("");
	let submittedInput = $state("");
  let queryTab = $state(0);

  const updateQueryTab = (updatedTab) => {
      queryTab=updatedTab;
  }

  const submit = () => {
      submittedInput = input;
      fetchData()
  }

  let data = $state([]);
  let error = $state(null);
  let loading = $state(false);

  async function fetchData() {
  loading = true;
  error = null;

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

    data = await response.json()
  } catch (err) {
    error = err.message;
  } finally {
    loading = false;
  }
}
</script>

<div class="pt-nav xl:w-1/2 lg:w-3/5 md:w-3/4 sm:w-5/6 mx-auto pb-20">
  <div class="pgaql-container">
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
      <div class="flex flex-col text-center items-center justify-center">
        <textarea bind:value={input} placeholder="Enter your query"></textarea>
        <button class="query-submit-btn" onclick={submit} disabled={input.trim() === ""}>Search</button> 
        <p class="pt-5 px-5">
          <b>Example:</b> CHART box_score IN scatter_plot FOR fga VS fgm WHERE team_abbr = 'CLE'
        </p>
      </div>
      
    </div>
    <div class="pgaql-chart-container mx-auto">
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.length > 0}
      <div class="pt-5">
        <Chart {data} />
      </div>
      {/if}
    </div>
  </div>
</div>

<style>

  .pgaql-container {
    padding: 3rem;
    margin: 0 1rem;
    border-radius: 16px;
    background-color: #333333;

    textarea {
        border-radius: 8px;
        border: 1px solid #F0F0F0;
        padding: 0.6em 1.2em;
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
        transition: border-color 0.25s;
        width: 100%;
      }
    }

    .pt-nav {
        padding-top: max(3.5rem, 10vh);
    }

    .query-submit-btn {
      width: 25%;
      margin-top: 1rem;
      border: 1px solid #F0F0F0;
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