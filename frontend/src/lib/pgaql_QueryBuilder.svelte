<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let input = "";

	function handleAppendInput(btnValue) {
		input+=btnValue;
	}

	function handleClear() {
		input="";
	}

	function handleSubmit() {
		dispatch('submit');
	}
</script>

<div class="flex flex-col text-center items-center justify-center">
	<p>
		Build a query by selecting what you would like to chart
	</p>
	<div class="w-full py-10">
		<button class="query-submit-btn" onclick={handleAppendInput("CHART")}>CHART</button> 
	</div>
	<div class="w-full py-10">
		Input: "{input}"
	</div>
	<div class="w-full flex gap-8 justify-center">
		<button class="query-clear-btn" onclick={handleClear}>Clear</button> 
		<button class="query-submit-btn" onclick={handleSubmit} disabled={input.trim() === ""}>Search</button> 
	</div>
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

	.query-clear-btn, .query-submit-btn {
		width: 25%;
		margin-top: 1rem;
		border: 1px solid #F0F0F0;
    }

    .gap-8 {
    	gap: 2rem;
    }
</style>