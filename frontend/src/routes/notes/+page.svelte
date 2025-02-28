<script>
    const projects = [
        {
            name: "this"
        },
        {
            name: "is"
        },
        {
            name: "very"
        },
        {
            name: "unhelpful"
        },
        {
            name: "thoughts"
        }
    ];

</script>

<div class="px-10vh pt-nav">
    <div class="text-5xl font-bold">
        Notes
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
            <div class="project-container">{project.name}</div>
        {/each}
    </div>
</div>

<style type="text/css">
    .pt-nav {
        padding-top: max(3.5rem, 15vh);
    }

    .px-10vh {
        padding-left: 10vh;
        padding-right: 10vh;
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