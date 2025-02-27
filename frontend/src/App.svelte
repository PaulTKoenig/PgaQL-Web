<script lang="ts">
  import Nav from './lib/Nav.svelte'
  import Home from './lib/Home.svelte'
  import Search from './lib/Search.svelte'
  import Projects from './lib/Projects.svelte'
  import Notes from './lib/Notes.svelte'

  let page = $state("Home");
</script>


<main>
  <Nav bind:page />

  <div class="z-0">
    {#if page === 'Home'}
      <Home bind:page />
    {:else if page === 'PgaQL'}
      <Search />
    {:else if page === 'Projects'}
      <Projects />
    {:else if page === 'Notes'}
      <Notes />
    {/if}
  </div>
</main>
