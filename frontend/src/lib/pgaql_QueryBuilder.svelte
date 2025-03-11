<script>
	import { createEventDispatcher } from 'svelte';
	import { queryBuilderSteps } from './pgaql_queryBuilderSteps'

	const dispatch = createEventDispatcher();

	let inputArray = $state([]);
	let queryBuilderStep = $state(0);

    function addToInputArray(stepValue) {
    	let inputValue = "";
    	const stepQueryPrefix = queryBuilderSteps[queryBuilderStep].queryPrefix;
    	console.log(stepQueryPrefix)

    	if (stepQueryPrefix) {
    		inputValue+=stepQueryPrefix;
    	}
    	console.log(inputValue)
    	inputValue+=stepValue;
    	console.log(inputValue)

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
		let input = concatQuery();
		dispatch('submit', { input });
	}

	function concatQuery() {
		let input = "";
		inputArray.map((inputValue, inputIdx) => {
			if (inputIdx !== 0) {
				input+=" ";
			}
			input+=inputValue;
		});
		return input;
	}
</script>

<div class="flex flex-col">
	<p class="font-bold pb-3 text-xl">
		Build a query by selecting what you would like to chart
	</p>
	<p class="text-xl">Step {queryBuilderSteps[queryBuilderStep].step}: &nbsp;
		{queryBuilderSteps[queryBuilderStep].title}</p> 
	<div class="py-16 text-lg">
		{#if queryBuilderSteps[queryBuilderStep].options && queryBuilderSteps[queryBuilderStep].options.length >= 3}
			<div class="grid grid-cols-3 gap-5">
				{#each queryBuilderSteps[queryBuilderStep].options as step}
					<button class="query-feature-btn" onclick={() => addToInputArray(step.value)}>	{step.label}
					</button>
				{/each}
			</div>
		{:else if queryBuilderSteps[queryBuilderStep].options}
	        <div class="flex justify-center gap-5">
				{#each queryBuilderSteps[queryBuilderStep].options as step}
					<button class="query-feature-btn" onclick={() => addToInputArray(step.value)}>	{step.label}
					</button>
				{/each}
			</div>
		{:else}
	        <div class="flex justify-center gap-5">
				<button class="query-clear-btn" onclick={handleRestart}>Restart</button> 
				<button class="query-submit-btn" onclick={handleSubmit}>Search</button> 
			</div>
		{/if}
	</div>
	<div class="w-full text-xl">
		Input:&nbsp;
		<span class="font-bold">	
    		{concatQuery()}
		</span>
	</div>
	<div class="flex gap-8">
		<button class="query-revert-btn" onclick={handleRevert} disabled={queryBuilderStep===0}>Revert</button> 
		<button class="query-skip-btn" onclick={null} disabled>Skip</button> 
	</div>
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

	.query-clear-btn, .query-submit-btn, .query-revert-btn, .query-skip-btn, .query-feature-btn {
		width: 200px;
		margin-top: 1rem;
		border: 1px solid #F0F0F0;
    }

    .query-feature-btn {
    	width: auto;
    }

    .gap-8 {
    	gap: 2rem;
    }
</style>