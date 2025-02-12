<script lang="ts">
  import { onMount } from 'svelte';

	let input = $state('');
	let submittedInput = $state('');


  const clearInput = () => {
      input = '';
  }
  const submit = () => {
      submittedInput = input;
      fetchData()
  }

  let data = $state(null);
  let error = $state(null);
  let loading = $state(false);

  // Function to fetch data on button click
  async function fetchData() {
  loading = true;  // Set loading to true when the fetch starts
  error = null;    // Clear any previous errors

  try {
    const response = await fetch('/api');
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    data = await response.json();  // Store the fetched data
    console.log(data);
  } catch (err) {
    error = err.message;  // Capture any errors
  } finally {
    loading = false;  // Set loading to false when done
  }
}
</script>

<input bind:value={input} placeholder="Enter your query" />
<button onclick={clearInput}>Clear</button>
<button onclick={submit}>Submit</button>
<p>Submitted Query: {submittedInput || 'rawr'}</p>
{#if loading}
  <p>Loading...</p>
{:else if error}
  <p>Error: {error}</p>
{:else if data}
  <ul>
    {#each data as item}
      <li>{item.message}</li>
    {/each}
  </ul>
{/if}

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