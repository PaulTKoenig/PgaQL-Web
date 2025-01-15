<script lang="ts">
	let input = $state('');
	let submittedInput = $state('');
    const clearInput = () => {
        input = '';
    }
    const submit = () => {
        submittedInput = input;
    }
</script>

<input bind:value={input} placeholder="Enter your query" />
<button onclick={clearInput}>Clear</button>
<button onclick={submit}>Submit</button>
<p>Submitted Query: {submittedInput || 'rawr'}</p>

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