<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import Nav from './lib/Nav.svelte'
  import Search from './lib/Search.svelte'
</script>

<main>
  <div class="nav">
    <Nav />
  </div>

  <div>
    <Search />
  </div>

  <div class="card">
    <Counter />
  </div>
</main>
