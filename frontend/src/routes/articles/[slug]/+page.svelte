<script lang="ts">
  import { page } from '$app/stores';

  export let articleHtml: string | null = null;
  let loading = true;

  $: slug = $page.params.slug;

  async function loadArticle() {
    const htmlFilePath = `/article-html/${slug}.html`;
    try {
      const response = await fetch(htmlFilePath);

      if (!response.ok) {
        throw new Error('Article not found');
      }

      articleHtml = await response.text();
    } catch (error) {
      console.error('Error loading article:', error);
      articleHtml = null;
    } finally {
      loading = false;
    }
  }

  $: slug, loadArticle();

  function goBack() {
    window.history.back();
  }
</script>

<div class="pt-nav px-10vh w-full">
  {#if loading}
    <div class="loading-spinner-container">
      <div class="loading-spinner"></div>
    </div>
  {:else if articleHtml}
    <div class="back-container">
      <div class="back-btn" on:click={goBack}><span class="arrow">&#8592;</span> Back</div>
    </div>
    <div>
      {@html articleHtml}
    </div>
  {:else}
    <div class="not-found-container">
      <div class="text-5xl font-bold">
    		Article Not Found :(
    	</div>
      <div class="back-btn" on:click={goBack}>Go Back</div>
    </div>
  {/if}
</div>

<style type="text/css">
    .pt-nav {
        padding-top: max(3.5rem, 12vh);
    }

    .px-10vh {
        padding-left: 20vh;
        padding-right: 20vh;
    }

    .projects-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 2rem;
    }

    .project-container {
        background-color: #333333;
        padding: 1rem;
        border-radius: 4px;
    }

    .loading-spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 70vh;
    }

    .loading-spinner {
        border: 8px solid #F0F0F0;
        border-top: 8px solid #03DAC6;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .back-container {
        display: flex;
        align-items: center;
        margin-bottom: 3rem;
    }

    .back-btn {
        border: 1px solid lightgrey;
        border-radius: 8px;
        padding: 0.2em 1.2em;
        cursor: pointer;
        display: flex;
        align-items: center;
    }

    .not-found-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 70vh;
        gap: 2rem;
    }

    .arrow {
      margin-right: 8px;
      font-size: 1.6rem;
    }
</style>
