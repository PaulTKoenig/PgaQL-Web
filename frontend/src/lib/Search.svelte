<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from './Chart.svelte';

	let input = $state("");
	let submittedInput = $state("");

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

<div class="flex w-1/2 mx-auto gap-10">
  <div 
    class="w-1/3 border-b hover:shadow-lg focus:shadow-lg cursor-pointer p-3 transition-all"
  >Open Query</div>
  <div 
    class="w-1/3 border-b hover:shadow-lg focus:shadow-lg cursor-pointer p-3 transition-all"
  >Query Builder</div>
  <div 
    class="w-1/3 border-b hover:shadow-lg focus:shadow-lg cursor-pointer p-3 transition-all"
  >Natural Language Query</div>
</div>

<div class="p-5">
  <input bind:value={input} placeholder="Enter your query" />
  <button onclick={submit} disabled={input.trim() === ""}>Search</button>
  <p class="p-5">
    <b>Example:</b> CHART box_score IN scatter_plot FOR fga VS fgm WHERE team_abbr = 'CLE'
  </p>
</div>
<div class="w-1/2 mx-auto">
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

<style>
    input {
        border-radius: 8px;
        border: 1px solid #F0F0F0;
        padding: 0.6em 1.2em;
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
        transition: border-color 0.25s;
    }
</style>