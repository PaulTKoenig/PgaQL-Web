<script>
  import { onMount } from 'svelte';
  import Dropdown from './Dropdown.svelte';

  let props = $props();
  let whereClauseIdx = props.whereClauseIdx;

  let whereValueDisabled = $state(true);

  let statValueOptions = $state([]);

  let data = $state([]);
  let error = $state(null);


  function handleSelectWhereFieldOption(selectedOption) {
    props.whereStepSelectedOptions[whereClauseIdx].whereFieldSelectedOption = selectedOption;
    props.whereStepSelectedOptions[whereClauseIdx].whereValueSelectedOption = "";
    whereValueDisabled = false;
    fetchOptionValuesData(selectedOption.value);
  }

	function handleSelectWhereValueOption(selectedOption) {
    props.whereStepSelectedOptions[whereClauseIdx].whereValueSelectedOption = selectedOption;
	}

  async function fetchOptionValuesData(selectedField) {
    error = null;
    statValueOptions=[];

    try {
      const response = await fetch("/api/get-all-field-values/" + selectedField);

      if (!response.ok) {
        throw new Error('Sorry something went wrong. Please try again');
      }

      const responseJson = await response.json();

      const tempStatValueOptions = [];
      statValueOptions = responseJson.forEach(option => {
        const optionValue = option[0]
        if (!tempStatValueOptions.includes(optionValue)) {
          tempStatValueOptions.push(optionValue)
        }
      });
      statValueOptions = smartSort(tempStatValueOptions);

    } catch (err) {
      error = err.message;
      console.error(error)
    }
  }

  function smartSort(list) {

    const hadEmptyString = list.includes("");
    list = list.filter(item => item !== "");

    if (list.every(item => !isNaN(item))) {
        list.sort((a, b) => Number(a) - Number(b));
    } else {
        list.sort();
    }

    if (hadEmptyString) {
        list.push("N/A");
    }

    return list;
  }
</script>

<div class="flex flex-col items-center justify-center gap-1 pb-8">
    <div class="text-center w-24 pb-2">
      WHERE
    </div>

    <Dropdown options={props.statFieldOptions} value={props.whereStepSelectedOptions[whereClauseIdx].whereFieldSelectedOption ? props.whereStepSelectedOptions[whereClauseIdx].whereFieldSelectedOption.label : ""} disabled={false} placeholder={"Search Stat Field..."} onSelect={handleSelectWhereFieldOption} bindLabel={"label"} />
    <div class="w-24 text-2xl text-center">
      =
    </div>

    <Dropdown options={statValueOptions} value={props.whereStepSelectedOptions[whereClauseIdx].whereValueSelectedOption} disabled={whereValueDisabled} placeholder={"Search Field Value..."} onSelect={handleSelectWhereValueOption} />
</div>

<style>
  .dropdown {
    position: relative;
    display: inline-block;
  }

  .dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border-radius: 8px;
    border: 1px solid #202124;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-height: 200px;
    overflow-y: auto;
    z-index: 1;
    display: none;
/*    color: #202124;*/
    background-color: #333333;
  }

  .dropdown-menu.active {
    display: block;
  }

  .dropdown-item {
    padding: 8px 12px;
  }

  .dropdown-item:hover {
    background-color: #f0f0f0;
    color: #202124;
    cursor: pointer;
  }

  input {
    padding: 8px;
    width: 200px;
    box-sizing: border-box;
  	border-radius: 8px;
  	border: 1px solid #F0F0F0;
  }
</style>