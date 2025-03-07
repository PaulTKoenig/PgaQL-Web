<script>
    import { ProjectCard } from '$lib';
    import emblaCarouselSvelte from 'embla-carousel-svelte';
    import { Carousel } from '$lib';
    import { articles } from '../lib/articles.ts';

    const whatImDoingNowList = [
        {
            title: "Finishing beta version of PgaQL"
        },
        {
            title: "Finally getting around to documenting all of my personal projects"
        },
        {
            title: "Winter bulk"
        },
        {
            title: "Not getting victory royales in fortnite"
        }
    ]
</script>

<div class="px-10vh">
    <div class="text-4xl font-bold pb-4">
        Hi, I'm Paul
    </div>
    <div class="text-4xl font-bold pb-8">
        Software Engineer
    </div>
    <div class="flex flex-col gap-6 dark-text">
        <div class="text-xl font-bold">
            I'm a shitty developer with a range of experience in web development, systems engineering, and data science. I got into coding in 2019 from the need to take an extra elective in course schedule and a curiosity for the internet, which eventually led me to major in Computer Science at The Ohio State University.
        </div>

        <div class="text-xl font-bold">
            I love music and spending time outdoors, enjoying activities like golf, snowboarding, and fishing in my free time. I created this page to share more about my development journey and life experiences.
        </div>
    </div>

    <div class="projects-section-header">
        <div class="text-3xl font-bold">
            My Favorite Projects
        </div>
        <a class="more-projects-btn ml-auto text-lg font-bold" href="/projects">
            All Projects
        </a>
    </div>

    <div class="projects-carousel">
        <Carousel />
    </div>

    <div class="section-header text-3xl font-bold">
        What I'm Doing Now<span class="text-base">&nbsp;&nbsp;(outside of work)</span>
    </div>
    <div class="section-description">
        <div class="text-lg dark-text">
            Last updated 3/3/2025
        </div>
    </div>

    <div class="section-container text-xl dark-text">
        <ul>
            {#each whatImDoingNowList as item}
                <li class="py-1">{item.title}</li>
            {/each}
        </ul>
    </div>

    <div class="section-header">
        <div class="text-3xl font-bold">
            Articles
        </div>
        <a class="more-articles-btn ml-auto text-lg font-bold" href="/articles">
            All Articles
        </a>
    </div>
    <div class="section-description">
        <div class="text-lg dark-text">
            Personal notes about development, projects, and anything else
        </div>
    </div>

    <div class="articles-section-container text-xl dark-text">
        <ul>
            {#each articles as article}
                <li class="flex py-1">
                    <a href={"articles/"+article.id}>{article.title}</a>
                    <div class="ml-auto hidden lg:block">{article.date}</div>
                </li>
            {/each}
        </ul>
    </div>

    <div class="p-12"/>

</div>

<style type="text/css">

    @media (min-width: 1500px) {
        .px-10vh {
            padding: 0 10vh;
        }
    }

    .more-projects-btn {
        border: 1px solid lightgrey;
		border-radius: 8px;
        padding: .3em .6em;
		cursor: pointer;
    }

    .more-articles-btn {
        border: 1px solid lightgrey;
        border-radius: 8px;
        padding: .3em .6em;
        cursor: pointer;
    }

    .more-projects-btn:hover {
      text-decoration: underline;
    }

    .min-h-40vh {
        min-height: 40vh;
    }

    .min-h-50vh {
        min-height: 50vh;
    }

    .section-header, .projects-section-header {
        display: flex;
        align-items: center;
    }

    .section-header {
        padding: 6rem 10% .5rem;
    }

    .section-description {
        padding: 0 10%;
    }

    .projects-section-header {
        padding: 6rem 10% 2rem;
    }

    .section-container, .articles-section-container {
        padding: 1rem 12% 0;
    }

    .section-container ul {
        list-style-type: disc;
        padding: 0 50px;
    }

    .articles-section-container ul {
        padding: 0 30px;
    }

    .parent {
        padding-bottom: 20vh;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 40px;
        div {
            border: 1px solid white;
        }
    }

    .px-20vh {
        padding-left: 15%;
        padding-right: 15%;
    }
</style>