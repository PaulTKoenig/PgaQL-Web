<script type="text/css">
    import { page } from '$app/state';
</script>


<div class="pgaql-nav-container">
	<div class="flex flex-col gap-1 items-start">
		<a class="nbaql-nav-btn" href="/pgaql/build-a-query" class:font-bold={page.url.pathname === "/pgaql/build-a-query"}>
		Build a Query
		</a>
		<a class="nbaql-nav-btn" href="/pgaql/docs" class:font-bold={page.url.pathname === "/pgaql/docs"}>
		Documentation
		</a>
		<a class="nbaql-nav-btn" href="/pgaql/project-goals" class:font-bold={page.url.pathname === "/pgaql/project-goals"}>
		Future of the Project
		</a>
	</div>
</div>
<div class="pgaql-nav-pill-container">
	<div class="flex gap-5 items-start">
		<a class="nbaql-nav-btn" href="/pgaql/build-a-query" class:pgaql-nav-pill-active={page.url.pathname === "/pgaql/build-a-query"}>
		Build a Query
		</a>
		<a class="nbaql-nav-btn" href="/pgaql/docs" class:pgaql-nav-pill-active={page.url.pathname === "/pgaql/docs"}>
		Documentation
		</a>
		<a class="nbaql-nav-btn" href="/pgaql/project-goals" class:pgaql-nav-pill-active={page.url.pathname === "/pgaql/project-goals"}>
		Future of the Project
		</a>
	</div>
</div>

<div class="pgaql-menu-container">
	<p class="font-bold">
	NbaQL UI is an interactive platform to build queries with the query language 'NbaQL' allowing users to easily search and chart trends for their favorite athletes and teams
	</p>
	<p class="pt-10">
	Example: CHART player_stats IN scatter_plot FOR fga VS fgm WHERE blk = '10'
	</p>
</div>

<style type="text/css">
	.pgaql-menu-container, .pgaql-nav-container {
		padding: 3rem;
		margin: 0 1rem;
		border-radius: 16px;
		background-color: #333333;
    }

    @media (max-width: 1023px) {
    	.pgaql-nav-container {
    		display: none;
    	}
    }

    @media (min-width: 1024px) {
    	.pgaql-nav-pill-container {
    		display: none;
    	}
    }

    .pgaql-nav-container {
    	margin-bottom: 2rem;
    }

    .pgaql-nav-pill-container {
    	margin: 0 1rem 2rem;

    	.nbaql-nav-btn {
	    	background-color: #333333;
	    	border-radius: 16px;
	    	padding: 0.5rem 0.75rem;
    	}
    }



    .pgaql-nav-pill-active {
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
    }

    .nbaql-nav-btn:hover {
    	background-color: #555555;
    }
</style>