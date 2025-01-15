<script lang="ts">
  import Nav from './lib/Nav.svelte'
  import Search from './lib/Search.svelte'

  let page = $state("Resume");
</script>


<main>
  <div class="nav">
    <Nav bind:page />
  </div>
  {page}

  <div class="page-body">
    <div class="card">
      <Search />
    </div>
  </div>
</main>
