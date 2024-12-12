<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import Nav from './lib/Nav.svelte'
  import Search from './lib/Search.svelte'
</script>

<main>
  <div class="nav">
    <Nav />
  </div>

  <div class="page-body">
    <div class="card">
      <Search />
    </div>
  </div>
</main>
