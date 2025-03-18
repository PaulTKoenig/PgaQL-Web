<script>
  import { onMount } from 'svelte';

  let props = $props();
	let statFieldOptions = props.statFieldOptions;

	let whereField = $state("");
  let whereValue = $state("");
	let statFieldIsActive = $state(false);
	let valueFieldIsActive = $state(false);
	// let options = ['Apple', 'Banana', 'Orange', 'Grapes', 'Peach', 'Mango', 'Pineapple'];

  let options = $state(['Apple', 'Banana', 'Orange', 'Grapes', 'Peach', 'Mango', 'Pineapple']);
  let data = $state([]);
  let error = $state(null);

	const filteredStatValueOptions = () => {

    const optionsWithoutSelected = options.filter(option => option.toLowerCase().includes(whereValue.toLowerCase()));
		return optionsWithoutSelected;
	};

	const filteredStatFieldOptions = () => {

    const optionsWithoutSelected = statFieldOptions.filter(option => option.label.toLowerCase().includes(whereField.toLowerCase()));

    return optionsWithoutSelected;
	};

	function toggleStatFieldDropdown() {
		statFieldIsActive = !statFieldIsActive;
	}

	function toggleValueFieldDropdown() {
		valueFieldIsActive = !valueFieldIsActive;
	}

	function closeStatFieldDropdown() {
		statFieldIsActive = false;
	}

	function closeValueFieldDropdown() {
		valueFieldIsActive = false;
	}


  function selectWhereFieldOption(option) {
    console.log(option)
    whereField = option;
    closeStatFieldDropdown();
  }

	function selectWhereValueOption(option) {
    console.log(option)
		whereValue = option;
		closeValueFieldDropdown();
	}

  async function fetchOptionValuesData() {
    error = null;

    try {
      const response = await fetch(`/api/get-all-field-values`);
      
      if (!response.ok) {
        throw new Error('Sorry something went wrong. Please try again');
      }

      responseJson = await response.json();
      options = responseJson.map(option => option[0]);
    } catch (err) {
      error = err.message;
    }
  }

  onMount(() => {
    fetchOptionValuesData();
  });
</script>

<div 
  class="dropdown"
  on:blur={closeStatFieldDropdown}
>
  <input 
    type="text" 
    bind:value={whereField} 
    placeholder="Search..."
    on:focus={toggleStatFieldDropdown} 
  />
  
  <div 
    class="dropdown-menu {statFieldIsActive ? 'active' : ''}"
  >
    {#each filteredStatFieldOptions() as option}
      <div 
        class="dropdown-item"  
        on:click={() => {
          selectWhereFieldOption(option.label)
        }}
      >
        {option.label}
      </div>
    {/each}
  </div>
</div>
&nbsp;&nbsp;=&nbsp;&nbsp;
<div 
  class="dropdown"
  on:blur={closeValueFieldDropdown}
>
  <input 
    type="text" 
    bind:value={whereValue} 
    placeholder="Search..."
    on:focus={toggleValueFieldDropdown}
  />
  
  <div class="dropdown-menu {valueFieldIsActive ? 'active' : ''}">
    {#each filteredStatValueOptions() as option}
      <div 
        class="dropdown-item"
        on:click={() => selectWhereValueOption(option)}
      >
        {option}
      </div>
    {/each}
  </div>
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