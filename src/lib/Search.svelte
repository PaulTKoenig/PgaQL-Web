<script lang="ts">
	let query = $state('');
	let submittedInput = $state('');
    const submit = () => {
        submittedInput = query
    }
</script>

<input bind:value={query} placeholder="Enter your query" />
<button onclick={submit}>Submit</button>
<p>Submitted Query: {submittedInput || 'rawr'}</p>
