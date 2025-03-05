<script>
    const projects = [
        {
            name: "pgaql interpreter",
            description: "Interpreter for the developed language 'PgaQL' that allows users to easily find trends in their favorite athletes and teams",
            demo_link: "/pgaql",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Interpreter",
            year: "2024",
            favorite: true
        },
        {
            name: "paul.com",
            description: "my wesbite",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Web",
            year: "2024"
        },
        {
            name: "no code",
            description: "Web application enabling users to interact with datasets and experiment building and fine-tuning ML models without coding; Includes data exploration, cleaning, transformation, visualization, and model development",
            repo_link: "https://github.com/PaulTKoenig/MLExpress",
            year: "2024",
            favorite: true
        },
        {
            name: "bball r us",
            year: "2023",
            favorite: true
        },
        {
            name: "hotel scraper",
            description: "Data collection system for 7 resorts to monitor patterns in dynamic room pricing, aiding in forecasting real estate returns; Saves the client 60 hours of manual collection each quarter",
            year: "2023"
        },
        {
            name: "indoor maps - hackohio 3",
            year: "2023"
        },
        {
            name: "ai voice generation dataset automation",
            description: "Data collection project to automate creating AI voice clones",
            year: "2023"
        },
        {
            name: "ncaab predict",
            description: "Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season",
            article_link: "/articles/001",
            year: "2022",
            favorite: true
        },
        {
            name: "walk step run - hackohio 2",
            year: "2022"
        },
        {
            name: "steering wheel - hackohio 1",
            year: "2022"
        }
    ];

</script>

<div class="px-10vh pt-nav">
    <div class="text-5xl font-bold">
        Projects
    </div>
    <div class="text-2xl font-bold py-5">
        I pledge Allegiance to the flag
        of the United States of America
        and to the Republic for which it stands,
        one nation under God, indivisible,
        with Liberty and Justice for all.
    </div>
    <div class="projects-container">
        {#each projects as project}
            <div class="project-container">
                <div class="flex flex-col h-full">
                    <div class="flex">
                        <div class="flex text-xl font-bold">
                            {project.name}
                            {#if project.favorite}
                                <span class="teal-star">&nbsp;*</span>
                            {/if}
                        </div>
                        <div class="ml-auto dark-text">{project.year}</div>
                    </div>
                    <div class="p-3 dark-text">{project.description}</div>
                    <div class="carousel-action-btns-container">
                        {#if project.demo_link}
                            <a class="carousel-action-btn coming-soon-btn" href={project.demo_link} target="_blank" rel="noopener noreferrer">
                              Demo
                            </a>
                        {/if}
                        {#if project.repo_link}
                            <a class="carousel-action-btn coming-soon-btn" href={project.repo_link} target="_blank" rel="noopener noreferrer">
                              Repo
                            </a>
                        {/if}
                        {#if project.article_link}
                            <a class="carousel-action-btn coming-soon-btn" href={project.article_link}>
                              Article
                            </a>
                        {/if}
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>

<style type="text/css">
    .pt-nav {
        padding-top: max(3.5rem, 12vh);
    }

    .px-10vh {
        padding-left: 10vh;
        padding-right: 10vh;
    }

    .projects-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        padding: 2rem;
    }

    @media (max-width: 1500px) {
        .projects-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 1000px) {
        .projects-container {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    .project-container {
        background-color: #333333;
        padding: 1rem;
        border-radius: 4px;
    }

    .carousel-action-btns-container {
        margin-top: auto;
        align-self: flex-start;
        display: flex;
        gap: 1rem;
        padding-top: 2rem;
    }

      .carousel-action-btn {
        background-color: #202124;
        color: #F0F0F0;
        padding: .5rem 1rem;
        border-radius: 6px;
        cursor: pointer;
        display: flex;
        align-items: center;
    }

    .teal-star {
        color: #03DAC6;
        font-size: larger;
    }
</style>