<script>
  import { onMount } from 'svelte';
  import Dropdown from './Dropdown.svelte';

  let props = $props();

	let whereFieldSelectedOption = $state("");
  let whereValueSelectedOption = $state("");

  let whereValueDisabled = $state(true);

  let statValueOptions = $state(['Apple', 'Banana', 'Orange', 'Grapes', 'Peach', 'Mango', 'Pineapple']);

  let data = $state([]);
  let error = $state(null);

  $effect(() => {
      if (whereFieldSelectedOption !== "" && whereValueSelectedOption !== "") {
        props.handleSelectedOptionForStep("WHERE " + whereFieldSelectedOption.value + " = " + whereValueSelectedOption);
      }
  });


  function handleSelectWhereFieldOption(selectedOption) {
    whereFieldSelectedOption = selectedOption;
    whereValueDisabled = false;
    fetchOptionValuesData();
  }

	function handleSelectWhereValueOption(selectedOption) {
    whereValueSelectedOption = selectedOption;
	}

  async function fetchOptionValuesData() {
    error = null;

    try {
      const response = await fetch(`/api/get-all-field-values`);

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
      statValueOptions = tempStatValueOptions.sort();
    } catch (err) {
      error = err.message;
      console.error(error)
    }
  }
</script>

<Dropdown options={props.statFieldOptions} value={whereFieldSelectedOption ? whereFieldSelectedOption.label : ""} disabled={false} onSelect={handleSelectWhereFieldOption} bindLabel={"label"} />
&nbsp;&nbsp;
<span class="text-2xl">=</span>
&nbsp;&nbsp;
<Dropdown options={statValueOptions} value={whereValueSelectedOption} disabled={whereValueDisabled} onSelect={handleSelectWhereValueOption} />

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