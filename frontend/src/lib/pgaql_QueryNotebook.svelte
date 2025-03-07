<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let input = "";
	
	function handleSubmit() {
		dispatch('submit');
	}
</script>

<div class="flex flex-col text-center items-center justify-center">
	<textarea bind:value={input} placeholder="Enter your query"></textarea>
	<button class="query-submit-btn" onclick={handleSubmit} disabled={input.trim() === ""}>Search</button> 
	<p class="pt-5 px-5">
	  <b>Example:</b> CHART box_score IN scatter_plot FOR fga VS fgm WHERE team_abbr = 'CLE'
	</p>
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
	}

	.query-submit-btn {
		width: 25%;
		margin-top: 1rem;
		border: 1px solid #F0F0F0;
    }
</style>