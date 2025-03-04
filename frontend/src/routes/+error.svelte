<script lang="ts">
  import { page } from '$app/state';
</script>

<div class="pt-nav">
  <div class="text-3xl font-bold">ERROR: {page.status}</div>
  <div class="text-3xl font-bold">{page.error.message}</div>
</div>

<style>
  .pt-nav {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .error-status, .error-message {
    text-align: center;
  }
</style>
