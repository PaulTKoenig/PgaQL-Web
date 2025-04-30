<script>
    const projects = [
        {
            name: "PgaQL Interpreter",
            description: "Interpreter for the developed language 'PgaQL' that allows users to easily find trends in their favorite athletes and teams",
            demo_link: "/pgaql",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Interpreter",
            year: "2024",
            favorite: true
        },
        {
            name: "paul.com",
            description: "Portfolio to showcase my journey as a software developer",
            repo_link: "https://github.com/PaulTKoenig/PgaQL-Web",
            year: "2024"
        },
        {
            name: "MLExpress",
            description: "Web application enabling users to interact with datasets and experiment building and fine-tuning ML models without coding; Includes data exploration, cleaning, transformation, visualization, and model development",
            repo_link: "https://github.com/PaulTKoenig/MLExpress",
            year: "2024",
            favorite: true
        },
        {
            name: 'Basketballs "R" Us',
            description: "One stop e-commerce shop for all things basketball with fully functional inventory management and order processing",
            year: "2023",
            favorite: true
        },
        {
            name: "Resort Price & Amenity Data Collection Service",
            description: "Data collection system for 7 resorts to monitor patterns in dynamic room pricing, aiding in forecasting real estate returns; Saves the client 60 hours of manual collection each quarter",
            year: "2023"
        },
        {
            name: "Community-Driven Indoor Navigation App",
            description: "Placed 2nd out of 25 teams in Ohio State University Hackathon",
            year: "2023",
            medal: true
        },
        {
            name: "Automated Dataset Builder for AI Voice Generation",
            description: "Data collection project to automate creating AI voice clones",
            year: "2023"
        },
        {
            name: "Statistical Approach to Predicting NCAAB Outcomes",
            description: "Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season",
            article_link: "/articles/001",
            year: "2022",
            favorite: true
        },
        {
            name: "Student Commute Matching App for Safer Traveling at Night",
            description: "Placed 2nd out of 25 teams in Ohio State University Hackathon",
            year: "2022",
            medal: true
        },
        {
            name: "Automated Navigation System for Driver Safety",
            description: "Navigation system utilizing image processing by giving vibrating cues to an arduino in the steering wheel",
            year: "2022"
        }
    ];

</script>

<div class="text-5xl font-bold">
    Projects
</div>
<div class="text-2xl py-5 dark-text">
    Personal projects, hackathons, and other collaborative efforts I have worked on throughout the years
</div>
<div class="projects-container">
    {#each projects as project}
        <div class="project-container">
            <div class="flex flex-col h-full">
                <div class="flex pb-2">
                    <div class="flex items-center text-xl font-bold max-w-3/4">
                        {project.name}
                    </div>
                    <div class="ml-auto dark-text">{project.year}</div>
                </div>
                <div class="flex gap-2">
                    {#if project.favorite}  <span class="ml-2 bg-yellow-400 text-white text-xs px-2 py-1 rounded-full">⭐ Favorite</span>
                            {/if}
                    {#if project.medal}  <span class="ml-2 bg-gray-400 text-white text-xs px-2 py-1 rounded-full">🏅 2nd Place Hackathon</span>
                            {/if}
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
</style>