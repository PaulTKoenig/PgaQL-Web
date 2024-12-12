<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import Nav from './lib/Nav.svelte'
  import Search from './lib/Search.svelte'
</script>

<main>
  <div class="nav">
    <Nav />
  </div>

  <h1>Vite + Svelte</h1>
  <div>
    <Search />
  </div>

  <div class="card">
    <Counter />
  </div>
</main>
