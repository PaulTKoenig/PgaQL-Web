<script type="text/css">
    import { page } from '$app/state';
    let buildIcon = '/build-icon.svg';
    let spaceshipIcon = '/spaceship-icon.svg';
    let docsIcon = '/docs-icon.svg';
</script>

<div class="nbaql-nav-pill-container">
	<div class="flex flex-wrap gap-5 items-start">
		<a class="nbaql-nav-btn" href="/nbaql/build-a-query" class:nbaql-nav-pill-active={page.url.pathname === "/nbaql/build-a-query"}>
        <img src={buildIcon} alt="Build a Query Icon" />
		Build a Query
		</a>
		<a class="nbaql-nav-btn" href="/nbaql/docs" class:nbaql-nav-pill-active={page.url.pathname === "/nbaql/docs"}>
        <img src={docsIcon} alt="Documentation Icon" />
		Documentation
		</a>
		<a class="nbaql-nav-btn" href="/nbaql/project-goals" class:nbaql-nav-pill-active={page.url.pathname === "/nbaql/project-goals"}>
        <img src={spaceshipIcon} alt="Future of the Project Icon" />
		Future of the Project
		</a>
	</div>
</div>

<style type="text/css">
    .nbaql-nav-pill-container {
    	margin: 0 1rem 2rem;
    	font-size: 16px;

    	.nbaql-nav-btn {
	    	background-color: #333333;
	    	border-radius: 16px;
	    	padding: 0.5rem 0.75rem;
    	}
    }

    @media (max-width: 640px) {
        .nbaql-nav-pill-container {
    		font-size: 12px;
        }
    }

    .nbaql-nav-pill-active {
    	font-weight: 800;

		transition-property: all;
		transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
		transition-duration: 150ms;

		--tw-shadow: 0 5px 8px -2px rgba(0, 0, 0, 0.6), 0 2px 3px -1px rgba(0, 0, 0, 1);
		box-shadow: var(--tw-ring-offset-shadow, 0 0 #fff), var(--tw-ring-shadow, 0 0 #fff), var(--tw-shadow);
    }

    .nbaql-nav-btn {
    	padding: 0.5rem;
    	border-radius: 4px;
    	display: flex;
    	white-space: nowrap;
    	gap: 0.5rem;
    }

    .nbaql-nav-btn:hover {
    	background-color: #555555;
    }
</style>