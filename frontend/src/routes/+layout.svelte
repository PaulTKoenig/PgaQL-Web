<script lang="ts">
  import { Nav } from '$lib';
  import '../app.css';
  let { children } = $props();
</script>

<main>
  <Nav />

  <div class="z-0">
    {@render children()}
  </div>
</main>