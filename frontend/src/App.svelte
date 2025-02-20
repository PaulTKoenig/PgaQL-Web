<script lang="ts">
  import Nav from './lib/Nav.svelte'
  import Search from './lib/Search.svelte'

  let page = $state("Resume");
</script>


<main>
  <div class="nav">
    <Nav bind:page />
  </div>

  <div class="page-body">
    <div class="card">
      {#if page === 'Resume'}
        <h1 class="text-3xl font-bold underline">
          Hellos world!
        </h1>
      {:else if page === 'PgaQL'}
        <Search />
      {/if}
    </div>
  </div>
</main>
