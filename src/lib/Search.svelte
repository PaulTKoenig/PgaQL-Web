<script>
	let query = $state('');
</script>

<input bind:value={query} placeholder="Enter your query" />
<p>Query: {query || 'rawr'}!</p>
