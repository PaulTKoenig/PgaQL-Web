<script lang="ts">
  import { page } from '$app/stores';

  export let articleHtml: string | null = null;

  $: slug = $page.params.slug;

  async function loadArticle() {
    const htmlFilePath = `/articles/${slug}.html`;
    try {
      const response = await fetch(htmlFilePath);

      if (!response.ok) {
        throw new Error('Article not found');
      }

      articleHtml = await response.text();
    } catch (error) {
      console.error('Error loading article:', error);
      articleHtml = null;
    }
  }

  // Call the loadArticle function when the slug changes
  $: slug, loadArticle();
</script>

<div class="pt-nav px-10vh">
  {#if articleHtml}
    <div>
      {@html articleHtml}
    </div>
  {:else}
    <div class="text-5xl font-bold">
		Article Not Found :(
	</div>
  {/if}
</div>

<style type="text/css">
    .pt-nav {
        padding-top: max(3.5rem, 15vh);
    }

    .px-10vh {
        padding-left: 20vh;
        padding-right: 0vh;
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
</style>
