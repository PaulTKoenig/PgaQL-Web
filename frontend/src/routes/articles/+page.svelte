<script>
    import { articles } from '../../lib/articles.ts';
</script>

<div class="text-5xl font-bold">
    Articles
</div>
<div class="text-2xl font-bold py-5">
    Deeper dive into projects, development, and any other thoughts I have
</div>
<div class="articles-container">
    {#each articles as article}
        <a class="article-container" href={"/articles/" + article.id}>
            <div class="text-xl font-bold">{article.title}</div>
            <div>{article.date}</div>
            <div>{article.description}</div>
        </a>
    {/each}
</div>

<style type="text/css">

    .articles-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 2rem;
    }

    @media (max-width: 1400px) {
        .articles-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 900px) {
        .articles-container {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    .article-container {
        background-color: #333333;
        padding: 1rem;
        border-radius: 4px;
    }

    .article-container:hover {
        cursor: pointer;
/*        border: 1px solid #03DAC6;*/

        --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 1);
        box-shadow: var(--tw-ring-offset-shadow, 0 0 #fff), var(--tw-ring-shadow, 0 0 #fff), var(--tw-shadow);
    }
</style>