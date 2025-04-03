<script>
  import { onMount } from 'svelte';

  let props = $props();

  let isActive = $state(false);

  const filteredOptions = () => {

    if (props.value === undefined || props.value.toString().trim() === "") {
      return props.options
    }

    const optionsWithoutSelected = props.options.filter(option => !option.toString().toLowerCase().includes(props.value.toString().toLowerCase()));

    return optionsWithoutSelected;
  };

	function toggleDropdown() {
		isActive = !isActive;
	}

	function closeDropdown() {
		isActive = false;
	}

</script>

<div 
  class="dropdown"
>
  <input 
    type="text" 
    bind:value={props.value}
    placeholder="Search..."
    on:focus={toggleDropdown}
    on:blur={() => setTimeout(closeDropdown, 150)}
    disabled={props.disabled}
  />
  
  <div class="dropdown-menu {isActive ? 'active' : ''}">
    {#each filteredOptions() as option}
      <div 
        class="dropdown-item"
        on:click={() => props.onSelect(option)}
      >
        {props.bindLabel !== undefined ? option[props.bindLabel] : option}
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