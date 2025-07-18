<script type="text/css">
    let downArrowIcon = '/down-arrow-icon.svg';
	import { slide } from 'svelte/transition';

    let showExpandableContent = false;

    const toggleExpandableContent = () => {
    	showExpandableContent = !showExpandableContent
    }
  
</script>

<div class="nbaql-menu-container">
	<p class="nbaql-menu-title flex lg:hidden" onclick={toggleExpandableContent}>
		NbaQL
		<img src={downArrowIcon} alt="Down Arrow Icon" class="ml-auto" />
	</p>
	{#if showExpandableContent}
	<div class="nbaql-menu-expanded-content" 
		transition:slide={{ duration: 500 }}
	>
		<p class="font-bold">
		NbaQL UI is an interactive platform to build queries with the query language 'NbaQL' allowing users to easily search and chart trends for their favorite athletes and teams
		</p>
		<p class="nbaql-menu-sidebar-example">
		Example: CHART player_stats IN scatter_plot FOR mins VS pts WHERE gameType = 'Playoffs' AND seriesGameNumber = '7.0'
		</p>
	</div>
	{/if}
	<div class="nbaql-menu-sidebar hidden lg:block">
		<p class="font-bold">
		NbaQL UI is an interactive platform to build queries with the query language 'NbaQL' allowing users to easily search and chart trends for their favorite athletes and teams
		</p>
		<p class="nbaql-menu-sidebar-example">
		Example: CHART player_stats IN scatter_plot FOR mins VS pts WHERE gameType = 'Playoffs' AND seriesGameNumber = '7.0'
		</p>
	</div>
</div>

<style type="text/css">
	.nbaql-menu-container, .nbaql-menu-sidebar {
		padding: 1rem 2rem;
		margin: 0 1rem;
		border-radius: 16px;
		background-color: #333333;
    }

    .nbaql-menu-sidebar {
		padding: 1rem 0rem;
    }

    .nbaql-menu-title {    	align-items: center;
    	font-size: 20px;
    	font-weight: 600;
    	cursor: pointer;
    }

    .nbaql-menu-expanded-content {
    	margin-top: 24px;
    }


    .nbaql-menu-sidebar-example {
    	padding-top: 40px;
    }



    @media (max-width: 600px) {
    	.nbaql-menu-title  {
    		font-size: 14px;
    	}

        .nbaql-menu-container, .nbaql-menu-sidebar {
    		font-size: 12px;
        }

        .nbaql-menu-expanded-content {
	    	margin-top: 16px;
	    }

	    .nbaql-menu-sidebar-example {
	    	pading-top: 16px;
	    }
    }
</style>