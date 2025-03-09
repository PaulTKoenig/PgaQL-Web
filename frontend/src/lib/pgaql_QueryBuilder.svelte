<script>
	import { createEventDispatcher } from 'svelte';
	import { queryBuilderSteps } from './pgaql_queryBuilderSteps'

	const dispatch = createEventDispatcher();

	let inputArray = $state([]);
	let queryBuilderStep = $state(0);

    function addToInputArray(inputValue) {
        inputArray.push(inputValue);
        queryBuilderStep+=1;
    }

	function handleRestart() {
		inputArray=[];
		queryBuilderStep=0;
	}

	function handleRevert() {
		inputArray.pop();
		queryBuilderStep-=1;
	}

	function handleSubmit() {
		let input = "";
		inputArray.map((inputValue, inputIdx) => {
			if (inputIdx !== 0) {
				input+=" ";
			}
			input+=inputValue;
		});
		dispatch('submit', { input });
	}
</script>

<div class="flex flex-col text-center items-center justify-center">
	<p class="font-bold pb-5">
		Build a query by selecting what you would like to chart
	</p>
	<p>Step {queryBuilderSteps[queryBuilderStep].step}</p>
	<p>{queryBuilderSteps[queryBuilderStep].title}</p>
	<div class="w-full py-10 flex gap-8 justify-center">
		{#if queryBuilderSteps[queryBuilderStep].options}

			{#each queryBuilderSteps[queryBuilderStep].options as step}

				<button class="query-submit-btn" onclick={() => addToInputArray(step.value)}>{step.label}</button>
			{/each}
		{:else}
			<button class="query-clear-btn" onclick={handleRestart}>Restart</button> 
			<button class="query-submit-btn" onclick={handleSubmit}>Search</button> 
		{/if}
	</div>
	<div class="w-full py-10">
		Input: "
		<span class="font-bold">	
    		{#each inputArray as inputValue, index}
    			{#if index > 0}  
    				&nbsp;
    			{/if}
    			{inputValue}
    		{/each}
		</span>
		"
	</div>
	<div class="w-full flex gap-8 justify-center">
		<button class="query-clear-btn" onclick={handleRevert} disabled={queryBuilderStep===0}>Revert</button> 
		<button class="query-submit-btn" onclick={null} disabled>Skip</button> 
	</div>
	<p class="pt-5 px-5">
	  <b>Example:</b> CHART box_score IN scatter_plot FOR fga VS fgm WHERE team_abbr = 'CLE'
	</p>
</div>

<style type="text/css">

	button:disabled {
		pointer-events: none;
		background-color: grey;
	}

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