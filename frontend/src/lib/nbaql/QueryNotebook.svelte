<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let input = $state("");
	
	function handleSubmit() {
		dispatch('submit', { input });
	}

	function handleKeyDown(event) {
		if (event.key === 'Enter' && !event.shiftKey) {
		  event.preventDefault();
		  handleSubmit();
		}
	}

	function handleTryExample() {
		input = 'CHART player_stats IN scatter_plot FOR mins VS pts WHERE gameType = \'Playoffs\' AND seriesGameNumber = \'7.0\'';
		handleSubmit();
	}
</script>

<div class="flex flex-col text-center items-center justify-center gap-5">
	<p class="font-bold">Write a query you would like to chart</p>
	<textarea 
	bind:value={input} 
	placeholder="Enter your query"
	onkeydown={handleKeyDown}
	>
	</textarea>
	<button class="query-submit-btn" onclick={handleSubmit} disabled={input.trim() === ""}>Search</button>
	<button class="query-try-example-btn" onclick={handleTryExample}>Try Example</button>
</div>

<style type="text/css">
	textarea {
	    border-radius: 8px;
	    border: 1px solid #F0F0F0;
	    padding: 0.6em 1.2em;
	    font-size: 1em;
	    font-weight: 500;
	    font-family: inherit;
	    transition: border-color 0.25s;
	    width: 100%;
	    min-height: 200px;
	}

	.query-submit-btn, .query-try-example-btn {
		width: 25%;
		min-width: 100px;
		margin-top: 1rem;
		border: 1px solid #F0F0F0;
    }

    .query-try-example-btn {
    	margin-top: 0;
		min-width: 150px;
    }
</style>