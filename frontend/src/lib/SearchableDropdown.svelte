<script>
	export let statFieldOptions = [];
	let searchQuery = '';
	let statFieldIsActive = false;
	let valueFieldIsActive = false;
	const options = ['Apple', 'Banana', 'Orange', 'Grapes', 'Peach', 'Mango', 'Pineapple'];

	const filteredOptions = () => {
		return options.filter(option => option.toLowerCase().includes(searchQuery.toLowerCase()));
	};

	const filteredStatFieldOptions = () => {
		return statFieldOptions.filter(option => option.label.toLowerCase().includes(searchQuery.toLowerCase()));
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

	function selectOption(option) {
		searchQuery = option;
		closeDropdown();
	}
</script>

<div class="dropdown">
  <input 
    type="text" 
    bind:value={searchQuery} 
    placeholder="Search..."
    on:focus={toggleStatFieldDropdown} 
    on:blur={closeStatFieldDropdown}
  />
  
  <div class="dropdown-menu {statFieldIsActive ? 'active' : ''}">
    {#each filteredStatFieldOptions() as option}
      <div 
        class="dropdown-item" 
        on:click={() => selectOption(option.label)}
      >
        {option.label}
      </div>
    {/each}
  </div>
</div>
&nbsp;&nbsp;=&nbsp;&nbsp;
<div class="dropdown">
  <input 
    type="text" 
    bind:value={searchQuery} 
    placeholder="Search..."
    on:focus={toggleValueFieldDropdown} 
    on:blur={closeValueFieldDropdown}
  />
  
  <div class="dropdown-menu {valueFieldIsActive ? 'active' : ''}">
    {#each filteredOptions() as option}
      <div 
        class="dropdown-item" 
        on:click={() => selectOption(option)}
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
    cursor: pointer;
  }

  .dropdown-item:hover {
    background-color: #f0f0f0;
    color: #202124;
  }

  input {
    padding: 8px;
    width: 200px;
    box-sizing: border-box;
	border-radius: 8px;
	border: 1px solid #F0F0F0;
  }
</style>