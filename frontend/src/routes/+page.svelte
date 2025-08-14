<script>    import { goto } from '$app/navigation';

    import { ProjectCard } from '$lib';
    import emblaCarouselSvelte from 'embla-carousel-svelte';
    import { Carousel } from '$lib';
    import { articles } from '../lib/articles.ts';
    let profilePicture = '../profile_picture2.jpg';

    const navigate = (url) => {
        goto(url);
    }
</script>

<div class="px-10vh">
    <div class="flex flex-col h-screen-wo-header items-center justify-center">
    <div class="polka-dots"></div>
        <div class="text-5xl 2xl:text-6xl font-bold pb-4 inline-block z-10">
            Paul Koenig
        </div>
        <div class="text-md 2xl:text-xl font-bold text-center w-2/3 2xl:w-1/2 z-10">
            23-year-old full stack developer based in Columbus, Ohio.
        </div>
        <button class="contact-me-btn text-base 2xl:text-lg z-10">
            <a href="mailto:paul.koenig.002@gmail.com">
                <strong>Contact Me</strong>
            </a>
        </button>
    </div>

    <div class="section-header first-section-header">
        <div class="text-xl 2xl:text-3xl font-bold inline-block">
            My Experience
            <div class="h-0.75 my-1 bg-teal"></div>
        </div>
    </div>

    <div class="articles-section-container text-sm 2xl:text-lg flex flex-col gap-8">
        <div class="experience-container">
            <div>
                JPMorgan Chase
            </div>
            <div class="experience-details">
                <div>
                    2023 - Current
                </div>
                <div class="text-xs 2xl:text-base dark-text pb-2">
                    I currently work here as a full stack software engineer developing various legal applications including and legal form lifecycle management. Using React.js, Java, Spring, MongoDB, Oracle Database
                </div>
                <div class="text-xs 2xl:text-base dark-text">
                    I also interned here building a web tool to automated tech risk report generation and introduced persistent user annotations. Used React.js, Python, Flask, and PostgreSQL.
                </div>
            </div>
        </div>

        <div class="experience-container">
            <div>
                John Deere
            </div>
            <div class="experience-details">
                <div>
                    2022
                </div>
                <div class="text-xs 2xl:text-base dark-text">
                    Internship where I built a vehicle simulation management tool, enabling 10 vehicle teams to efficiently test embedded controllers. Used C#, .NET, and Microsoft SQL Server.
                </div>
            </div>
        </div>

        <div class="experience-container">
            <div>
                Crown Battery Manufacturing
            </div>
            <div class="experience-details">
                <div>
                    2021
                </div>
                <div class="text-xs 2xl:text-base dark-text">
                    Internship where I lead a human-machine interface upgrade project and assisting in electrical maintenance tasks.
                </div>
            </div>
        </div>
    </div>

    <!-- <div class="xl:flex items-center">
        <div>
            <div class="text-2xl 2xl:text-4xl font-bold pb-4 inline-block">
                Hi, I'm Paul
                <div class="h-1 my-1 bg-teal"></div>
            </div>
            <div class="flex flex-col gap-6 dark-text">
                <div class="text-base 2xl:text-lg font-bold">
                    I'm a curious and driven software engineer with experience in full-stack development, data science, and systems engineering. I began coding in 2019 after a one-off programming elective in C# that sparked my interest, ultimately leading me to major in Computer Science at The Ohio State University.
                </div>

                <div class="text-base 2xl:text-lg font-bold">
                    I love music and spending time outdoors, enjoying activities like golf, snowboarding, and fishing in my free time. I created this page to share more about my development journey and life experiences.
                </div>
            </div>
        </div>
        <img src={profilePicture} alt="Profile Picture" class="hidden xl:block ml-24 h-72 rounded-lg" />
    </div> -->

    <div class="projects-section-header">
        <div class="text-xl 2xl:text-3xl font-bold inline-block">
            My Favorite Projects
            <div class="h-0.5 my-1 bg-teal"></div>
        </div>
        <div class="xl:pt-4">
            <button class="more-projects-btn text-base 2xl:text-lg font-bold" on:click={() => navigate("/projects")}>
                <strong>All Projects</strong>
            </button>
        </div>
    </div>

    <div class="projects-carousel">
        <Carousel />
    </div>

    <div class="section-header text-xl 2xl:text-3xl font-bold inline-block">
        What I'm Working On Now
        <div class="h-0.5 my-1 bg-teal"></div>
    </div>
    <!-- <div class="section-description">
        <div class="text-base 2xl:text-xl pb-1">
            (outside of work)
        </div>
    </div> -->
    <div class="section-description">
        <div class="text-base 2xl:text-xl dark-text">
            Last updated 7/1/2025
        </div>
    </div>

    <div class="section-container text-base 2xl:text-xl dark-text">
        <ul>
            <li class="py-1">Developing my latest project, <a href="/nbaql/build-a-query">NbaQL</a>, a custom query language for exploring NBA data</li>
            <li class="py-1">Organizing past personal projects by refining repositories and writing articles to showcase their achievements and what I learned</li>
        </ul>
    </div>

    <!-- <div class="section-header">
        <div class="text-xl 2xl:text-3xl font-bold inline-block">
            Articles
            <div class="h-0.75 my-1 bg-teal"></div>
        </div>
        <a class="more-articles-btn ml-auto text-lg font-bold" href="/articles">
            All Articles
        </a>
    </div> -->

    <!-- <div class="articles-section-container text-base 2xl:text-xl dark-text">
        Coming Soon...
        <ul>
            {#each articles as article}
                <li class="flex py-1">
                    <a href={"articles/"+article.id}>{article.title}</a>
                    <div class="ml-auto hidden lg:block">{article.date}</div>
                </li>
            {/each}
        </ul>
    </div> -->

</div>

<style type="text/css">

    .experience-details {
        border-left: 2px solid #555555;
        padding: 0.25rem 0 0.25rem 0.75rem;
        margin-top: 10px;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .h-screen-wo-header {
        height: calc(100vh - max(3.5rem, 12vh));
    }

    .polka-dots {
        position: absolute;
        border-radius: 30%;
        top: 15vh;

        width: 70vh;
        height: 70vh;

        background-image:
            radial-gradient(circle, #555555 8%, transparent 9%),
            radial-gradient(circle, #444444 8%, transparent 9%);

        background-size: 20px 20px;

        background-position: 0 0, 10px 10px;

        background-color: transparent;

        -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 10%, rgba(0,0,0,0) 90%);
        -webkit-mask-repeat: no-repeat;
        -webkit-mask-position: center;
        -webkit-mask-size: cover;

        mask-image: radial-gradient(circle, rgba(0,0,0,1) 10%, rgba(0,0,0,0) 90%);
        mask-repeat: no-repeat;
        mask-position: center;
        mask-size: cover;
    }

    .background-div {
        width: 66vh;
        height: 50vh;
        position: absolute;
        background-size: cover;
        background-position: center;
        z-index: 1;
        border-radius: 15%;
      }

    @media (min-width: 1536px) {
        .px-10vh {
            padding: 0 10vh;
        }
    }

    .more-projects-btn, .contact-me-btn {
        border: 1px solid lightgrey;
		border-radius: 8px;
        padding: .3em .6em;
		cursor: pointer;
    }

    .contact-me-btn {
        margin-top: 1rem;
        padding: .45em .9em;
    }

    .more-articles-btn {
        border: 1px solid lightgrey;
        border-radius: 8px;
        padding: .3em .6em;
        cursor: pointer;
    }

    .more-projects-btn:hover, .contact-me-btn:hover {
      text-decoration: underline;
    }

    .min-h-40vh {
        min-height: 40vh;
    }

    .min-h-50vh {
        min-height: 50vh;
    }

    .section-header {
        padding: 4rem 0 .5rem;
    }

    .first-section-header {
        padding-top: 0;
    }

    .section-description {
/*        padding: 0;*/
    }

    .projects-section-header {
        padding: 4rem 0 2rem;
    }

    .section-container, .articles-section-container {
        padding: 1rem 1rem 0;
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

    .section-container li a {
        text-decoration: underline;
        color: #627fc4;
    }

    .bg-teal {
        background-color: #018786;
    }

    .bg-copper {
        background-color: #d48e3d;
    }

    @media (max-width: 1280px) {
        .projects-section-header {
            display: block;
        }

        .more-projects-btn {
            margin-top: 1rem;
            display: block;
        }

        .section-container ul {
            list-style-type: disc;
            padding: 0 20px;
        }

        .articles-section-container ul {
            padding: 0 20px;
        }

        .polka-dots {
            width: 50vh;
            height: 70vh;
        }
    }

    @media (max-width: 500px) {
        .polka-dots {
            width: 40vh;
        }
    }
</style>