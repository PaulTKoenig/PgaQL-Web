<script lang="ts">
  import { NbaqlHeader, NbaqlSidebar } from '$lib';
</script>

<NbaqlHeader />
<div class="lg:flex">
  <div class="w-full lg:w-1/3 xl:w-1/4 mx-auto pb-10">
    <NbaqlSidebar />
  </div>

  <div class="flex flex-col gap-10 w-full lg:w-2/3 xl:w-3/4 mx-auto">
    <div class="nbaql-docs-container">
      <p>
        query : action features conditions?;
      </p>

      <p>
        action : 'CHART' plotType | 'FIND';
      </p>

      <p>
        plotType : 'scatterPlot';
      </p>

      <p>
        features : entity 'VS' entity;
      </p>

      <p>
        entity : 'playerName' | 'teamName' | 'pts' | 'mins' | etc..;
      </p>

      <p>
        conditions : 'WHERE' condition ('AND' condition)*;
      </p>

      <p>
        condition : field comparator value | field 'IN' '(' value (',' value)* ')';
      </p>

      <p>
        field : 'playerName' 
              | 'teamName'
              | 'pts'
              | 'mins'
              | etc..;
      </p>

      <p>
        comparator    : '=' | '&lt;' | '&gt;' | '&lt;=' | '&gt;=';
      </p>

      <p class="pt-10">
        FIND golfers WHERE score &lt; 0 AND round = 1 AND tournament = "PGA Championship"
      </p>

      <p>
        CHART golfers IN scatter_plot FOR driving_distance VS score WHERE tournament = "US Open"

      </p>

      <p>
        CHART golfers IN box_plot FOR driving_distance_per_par_5 VS score WHERE tournament = "US Open" and driving_distance_per_par_5 defined as (FIND driving_distance_average WHERE par = 5 AND tournament = "US Open")
      </p>
  	</div>
  </div>
</div>

<style>
    .nbaql-docs-container {
      padding: 3rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
</style>