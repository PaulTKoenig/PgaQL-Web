<script>
    const projects = [
        {
            name: "NbaQL Interpreter",
            description: "Interpreter for the developed language 'NbaQL' that allows users to easily find trends in their favorite athletes and teams",
            demo_link: "/nbaql/build-a-query",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Interpreter",
            year: "2024",
            favorite: true,
            active: true,
            technologies: ['C', 'Svelte', 'Docker']
        },
        {
            name: "PaulKoenig.com",
            description: "Source of this website & NbaQL UI",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Web",
            year: "2024",
            active: true,
            technologies: ['Svelte', 'Docker']
        },
        {
            name: "MLExpress",
            description: "Web application enabling users to interact with datasets and experiment building and fine-tuning ML models without coding; Includes data exploration, cleaning, transformation, visualization, and model development",
            // article_link: "/articles/001",
            // repo_link: "https://github.com/PaulTKoenig/MLExpress",
            year: "2024",
            favorite: true,
            technologies: ['React', 'TensorFlow.js']
        },
        {
            name: 'Basketballs "R" Us',
            description: "One stop e-commerce shop for all things basketball with fully functional inventory management and order processing. Completed in my Distributed Enterprise Computing course",
            year: "2023",
            favorite: true,
            technologies: ['React', 'Node.js', 'Express.js', 'Kafka']
        },
        {
            name: "Resort Price & Amenity Data Collection Service",
            description: "Data collection system for 7 resorts to monitor patterns in dynamic room pricing, aiding in forecasting real estate returns; Saves the client 60 hours of manual collection each quarter",
            year: "2023",
            technologies: ['Python', 'BeatuifulSoup', 'Selenium']
        },
        {
            name: "Community-Driven Indoor Navigation App",
            description: "Web application that navigates users through complex indoor spaces. Incorporates gamification to increase user engagement allowing for crowdsourcing indoor building layouts",
            year: "2023",
            medal: true,
            technologies: ['Javascript', 'HTML', 'CSS']
        },
        {
            name: "Automated Dataset Builder for AI Voice Generation",
            description: "Data collection project to automate creating AI voice clones",
            year: "2023",
            technologies: ['Python']
        },
        {
            name: "Statistical Approach to Predicting NCAAB Outcomes",
            description: "Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season",
            // article_link: "/articles/003",
            year: "2022",
            favorite: true,
            technologies: ['Python', 'PyTorch', 'TensorFlow']
        },
        {
            name: "Walk Safe",
            description: "Student commute matching app for safer traveling at night. Matches students by commute route and user compatability level.",
            year: "2022",
            medal: true,
            technologies: ['Python', 'Flask']
        },
        {
            name: "Automated Steering Navigation System for Driver Safety",
            description: "Navigation system utilizing image processing by giving vibrating cues within the steering wheel by an arduino",
            year: "2022",
            technologies: ['Python', 'OpenCV']
        }
    ];

    let showFavoritesFirst = true;

    $: sortedProjects = showFavoritesFirst
        ? [...projects].sort((a, b) =>
          (b.favorite === true ? 1 : 0) - (a.favorite === true ? 1 : 0)
          )
        : projects;

</script>

<div class="text-xl 2xl:text-3xl font-bold">
    Projects
</div>
<div class="text-base 2xl:text-xl py-5 dark-text">
    Personal projects, hackathons, and other collaborative efforts I have worked on
</div>
<label class="pb-5">
  <input type="checkbox" bind:checked={showFavoritesFirst} />
  Show Favorites First
</label>
<div class="projects-container">
    {#each sortedProjects as project}
        <div class="project-container">
            <div class="flex flex-col h-full">
                <div class="flex pb-4">
                    <div class="flex items-center text-base 2xl:text-xl font-bold max-w-3/4">
                        {project.name}
                    </div>
                    <div class="ml-auto dark-text">{project.year}</div>
                </div>
                <div class="flex flex-wrap gap-y-2 gap-x-1">
                    {#if project.favorite}  <span class="ml-2 bg-yellow-500 text-white text-sm px-2.5 py-1 rounded-full">⭐ Favorite</span>
                    {/if}
                    {#if project.medal}  <span class="ml-2 bg-gray-400 text-white text-sm px-2.5 py-1 rounded-full">🏅 2nd Place Hackathon</span>
                    {/if}
                    {#if project.active}  <span class="ml-2 bg-green-600 text-white text-sm px-2.5 py-1 rounded-full">In Progress</span>
                    {/if}

                    {#each project.technologies as tech}  <span class="ml-2 bg-teal text-white text-sm px-2.5 py-1 rounded-full">{tech}</span>
                    {/each}
                </div>
                <div class="p-3 dark-text">{project.description}</div>
                <div class="carousel-action-btns-container">
                    {#if project.demo_link}
                        <a class="carousel-action-btn coming-soon-btn" href={project.demo_link}>
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

<style type="text/css">

    .projects-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        padding: 2rem;
    }

    @media (max-width: 1500px) {
        .projects-container {
            grid-template-columns: repeat(2, 1fr);
            padding: 0;
        }
    }

    @media (max-width: 1000px) {
        .projects-container {
            grid-template-columns: repeat(1, 1fr);
            padding: 0;
        }
    }

    .project-container {
        background-color: #333333;
        padding: 1.5rem;
        margin: 0.5rem 1rem;
        border-radius: 16px;
    }

    .carousel-action-btns-container {
        margin-top: auto;
        align-self: flex-start;
        display: flex;
        gap: 1rem;
        padding-top: 1rem;
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

    .bg-teal {
        background-color: #018786;
    }

    label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1rem;
        font-weight: 500;
        cursor: pointer;
        user-select: none;
        color: #9e9e9e;
      }

      input[type="checkbox"] {
        appearance: none;
        width: 1.2rem;
        height: 1.2rem;
        border: 2px solid #555;
        border-radius: 4px;
        display: inline-block;
        position: relative;
        transition: background 0.2s, border-color 0.2s;
      }

      input[type="checkbox"]:checked {
        background-color: #007bff;
        border-color: #007bff;
      }

      input[type="checkbox"]:checked::after {
        content: '✔';
        color: white;
        font-size: 0.9rem;
        position: absolute;
        top: -2px;
        left: 2px;
      }
</style>