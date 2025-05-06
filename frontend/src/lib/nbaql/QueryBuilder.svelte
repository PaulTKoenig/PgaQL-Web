<script>
	import { createEventDispatcher } from 'svelte';
	import { queryBuilderSteps } from './queryBuilderSteps';
	import WhereClauseDropdowns from './WhereClauseDropdowns.svelte';
	import Dropdown from './Dropdown.svelte';

	const dispatch = createEventDispatcher();

	let inputArray = $state([]);
	let queryBuilderStep = $state(0);
	let selectedOptionForStep = $state("");
	let statFieldAggregateType = $state("");
	let xAxisSelectedOption = $state("");
	let yAxisSelectedOption = $state("");

  	let whereStepSelectedOptions = $state([
  		{
  			whereFieldSelectedOption: "",
  			whereValueSelectedOption: ""
  		}
  	]);

    function addToInputArray() {
    	let inputValue = "";
    	const stepQueryPrefix = queryBuilderSteps[queryBuilderStep].queryPrefix;

    	if (stepQueryPrefix) {
    		inputValue+=stepQueryPrefix;
    	}
    	inputValue+=selectedOptionForStep;

        inputArray.push(inputValue);
        queryBuilderStep+=1;
        selectedOptionForStep="";
    }

    function handleSkip() {
        queryBuilderStep+=1;
        selectedOptionForStep="";
    }

	function handleRestart() {
		inputArray=[];
		queryBuilderStep=0;
        selectedOptionForStep="";
        xAxisSelectedOption="";
        yAxisSelectedOption="";
        statFieldAggregateType="";
	}

	function handleRevert() {
		inputArray.pop();
		queryBuilderStep-=1;
        selectedOptionForStep="";
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

	function handleSelectedOptionForStep(stepValue) {
		selectedOptionForStep = stepValue;
		if (queryBuilderSteps[queryBuilderStep].options.length === 1) {
			addToInputArray();
		}
	}

	function handleSetStatFieldAggregateType(stepValue) {
		if (statFieldAggregateType === stepValue) {
			statFieldAggregateType = "";
		} else {
			statFieldAggregateType = stepValue;
		}
	}

	const options = ['Apple', 'Banana', 'Cherry', 'Grapes', 'Mango', 'Orange'];

	$effect(() => {
	    let allWhereClausesCompleted = true;
	    let whereClauseValues = "WHERE "

	    whereStepSelectedOptions.forEach((whereStep, idx) => {
	    	if (allWhereClausesCompleted) {
		    	if (whereStepSelectedOptions[idx].whereFieldSelectedOption.value === "" || whereStepSelectedOptions[idx].whereValueSelectedOption === "") {
			        allWhereClausesCompleted = false;
				} else {
					if (idx !== 0) {
						whereClauseValues += " AND ";
					}
					whereClauseValues += whereStepSelectedOptions[idx].whereFieldSelectedOption.value + " = " + whereStepSelectedOptions[idx].whereValueSelectedOption;
				}

			}
	    })

	    if (allWhereClausesCompleted) {
	      	handleSelectedOptionForStep(whereClauseValues);
		}
	  });

	$effect(() => {
	    if (xAxisSelectedOption !== "" && yAxisSelectedOption !== "") {
			selectedOptionForStep = xAxisSelectedOption.value + " VS " + yAxisSelectedOption.value;
	    }
	});

	const handleSetXSelectedOption = (selectedOption) => {
		xAxisSelectedOption = selectedOption;
	}

	const handleSetYSelectedOption = (selectedOption) => {
		yAxisSelectedOption = selectedOption;
	}

	const addNewWhereClause = () => {
		whereStepSelectedOptions.push({
  			whereFieldSelectedOption: "",
  			whereValueSelectedOption: ""
  		});
	}

	const removeLastWhereClause = () => {
		whereStepSelectedOptions.pop();
	}
</script>

<div class="flex flex-col">
	<p class="font-bold pb-3 text-xl">
		Build a query by selecting what you would like to chart
	</p>
	<p class="text-xl">
		<span class="font-bold">Step {queryBuilderSteps[queryBuilderStep].step}:</span> 
		&nbsp;{queryBuilderSteps[queryBuilderStep].title}</p> 
	<div class="pt-16 pb-20 px-8 text-lg">
		{#if queryBuilderSteps[queryBuilderStep].stepType === "STAT_FIELD_STEP" && inputArray.includes("CHART season_box_score")}
			<p>Aggregate Types (Optional)</p>
	        <div class="flex gap-5 pb-12">
				<button class="query-clear-btn" class:selectedOption={statFieldAggregateType==="avg"} onclick={() => handleSetStatFieldAggregateType("avg")}>Average</button> 
				<button class="query-submit-btn" class:selectedOption={statFieldAggregateType==="total"} onclick={() => handleSetStatFieldAggregateType("total")}>Total</button> 
			</div>
			<p>Stat Field (Required)</p>
		{/if}
		{#if queryBuilderSteps[queryBuilderStep].stepType === "WHERE_STEP"}

			{#each whereStepSelectedOptions as _, idx}
				<div class="flex justify-center py-3">
					{idx !== 0 ? "AND" : ""}
				</div>
				<WhereClauseDropdowns statFieldOptions={queryBuilderSteps[queryBuilderStep].options} handleSelectedOptionForStep={handleSelectedOptionForStep} whereStepSelectedOptions={whereStepSelectedOptions} whereClauseIdx={idx} />
			{/each}

			<div class="flex justify-center gap-5">
				<button class="text-2xl query-feature-btn" onclick={addNewWhereClause}>+</button>
				<button class="text-2xl query-feature-btn" onclick={removeLastWhereClause} disabled={whereStepSelectedOptions.length === 1}>-</button>
			</div>
		{:else if queryBuilderSteps[queryBuilderStep].stepType === "STAT_FIELD_STEP"}
			<div class="flex justify-center gap-10">
				<div>
					<div>X Axis</div>
					<Dropdown options={queryBuilderSteps[queryBuilderStep].options.filter(option => option.value !== yAxisSelectedOption.value)} value={xAxisSelectedOption ? xAxisSelectedOption.label : ""} disabled={false} onSelect={handleSetXSelectedOption} bindLabel={"label"} placeholder={"Search Stat Field..."} />
				</div>
				<div>
					<div>Y Axis</div>
					<Dropdown options={queryBuilderSteps[queryBuilderStep].options.filter(option => option.value !== xAxisSelectedOption.value)} value={yAxisSelectedOption ? yAxisSelectedOption.label : ""} disabled={false} onSelect={handleSetYSelectedOption} bindLabel={"label"} placeholder={"Search Stat Field..."} />
				</div>
			</div>
		{:else if queryBuilderSteps[queryBuilderStep].options && queryBuilderSteps[queryBuilderStep].options.length >= 3}
			<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
				{#each queryBuilderSteps[queryBuilderStep].options as step}
					<button class="query-feature-btn" class:selectedOption={selectedOptionForStep===step.value} onclick={() => handleSelectedOptionForStep(step.value)}>{step.label}
					</button>
				{/each}
			</div>
		{:else if queryBuilderSteps[queryBuilderStep].options}
	        <div class="flex justify-center gap-5">
				{#each queryBuilderSteps[queryBuilderStep].options as step}
					<button class="query-feature-btn" class:selectedOption={selectedOptionForStep===step.value} onclick={() => handleSelectedOptionForStep(step.value)}>{step.label}
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
	<div class="flex flex-col">
		<button class="query-next-btn" onclick={addToInputArray} disabled={selectedOptionForStep===""}>Next</button> 
		<div class="flex gap-3">
			<button class="query-revert-btn" onclick={handleRevert} disabled={queryBuilderStep===0}>Revert</button> 
			<button class="query-skip-btn" onclick={handleSkip} disabled={queryBuilderStep!==3}>Skip</button> 
		</div>
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

	.query-clear-btn, .query-submit-btn, .query-revert-btn, .query-skip-btn, .query-feature-btn, .query-next-btn {
		width: 200px;
		margin-top: 1rem;
		border: 1px solid #F0F0F0;
    }

    .query-feature-btn {
    	width: auto;
    	min-height: 80px;
    }

    .gap-8 {
    	gap: 2rem;
    }

    .selectedOption {
    	color: #03DAC6;
    }
</style>