<script>
    import { ProjectCard } from '$lib';
    import emblaCarouselSvelte from 'embla-carousel-svelte';
    import { Carousel } from '$lib';

    const whatImDoingNowList = [
        {
            title: "building this piece of shit"
        },
        {
            title: "building the piece of shit interpreter above"
        },
        {
            title: "winter bulk"
        },
        {
            title: "going insane"
        }
    ]

    const notesList = [
        {
            title: "you",
            date: "Jan 2024"
        },
        {
            title: "will",
            date: "Feb 2024"
        },
        {
            title: "regret",
            date: "Mar 2024"
        },
        {
            title: "reading",
            date: "Apr 2024"
        },
        {
            title: "this",
            date: "May 2024"
        }
    ]
</script>

<div class="px-20vh">
    <div class="pt-nav">
        <div class="text-5xl font-bold pb-5">
            Hi, I'm Paul
        </div>
        <div class="text-5xl font-bold pb-12">
            Software Engineer
        </div>
        <div class="text-2xl font-bold">
            I pledge Allegiance to the flag
            of the United States of America
            and to the Republic for which it stands,
            one nation under God, indivisible,
            with Liberty and Justice for all.
        </div>
    </div>

    <div class="projects-section-header">
        <div class="text-3xl font-bold">
            Personal Projects
        </div>
        <a class="more-projects-btn ml-auto text-xl font-bold" href="/projects">
            All Projects
        </a>
    </div>

    <Carousel />

    <div class="section-header text-3xl font-bold">
        What I'm Doing Now<span class="text-base">&nbsp;&nbsp;(outside of work)</span>
    </div>

    <div class="section-container text-xl dark-text">
        <ul>
            {#each whatImDoingNowList as item}
                <li>{item.title}</li>
            {/each}
        </ul>
    </div>

    <div class="section-header">
        <div class="text-3xl font-bold">
            Notes
        </div>
    </div>

    <div class="notes-section-container text-xl dark-text">
        <ul>
            {#each notesList as note}
                <li class="flex">
                    <div>{note.title}</div>
                    <div class="ml-auto">{note.date}</div>
                </li>
            {/each}
        </ul>
    </div>

    <div class="p-15"/>

</div>

<style type="text/css">
    .more-projects-btn {
        border: 1px solid lightgrey;
		border-radius: 8px;
		padding: 0.6em 1.2em;
		cursor: pointer;
		transition: border-color 0.25s;
    }

    .more-projects-btn:hover {
      text-decoration: underline;
    }

    .pt-nav {
        padding-top: max(3.5rem, 15vh);
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
        padding: 6rem 10% 1rem;
    }

    .projects-section-header {
        padding: 6rem 10% 3rem;
    }

    .section-container, .notes-section-container {
        padding: 0 10% 0;
    }

    .section-container ul {
        list-style-type: disc;
        padding: 0 50px;
    }

    .notes-section-container ul {
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

    .dark-text {
        color: #888888;
    }
</style>