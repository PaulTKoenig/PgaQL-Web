<script lang="ts">
  import { Nav } from '$lib';
  import '../app.css';
  let { children } = $props();
</script>

<main>
  <Nav />

  <div class="pt-nav px-10vh z-0">
    {@render children()}
  </div>
</main>

<style type="text/css">
  .pt-nav {
      padding-top: max(3.5rem, 12vh);
  }

  .px-10vh {
      padding-left: 10vh;
      padding-right: 10vh;
  }
</style>