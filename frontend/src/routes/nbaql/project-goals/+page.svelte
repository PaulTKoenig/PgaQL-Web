<script lang="ts">
  import { NbaqlHeader, NbaqlSidebar } from '$lib';
</script>

<NbaqlHeader />
<div class="lg:flex">
  <div class="w-full lg:w-1/3 xl:w-1/4 mx-auto pb-10">
    <NbaqlSidebar />
  </div>

  <div class="flex flex-col gap-10 w-full lg:w-2/3 xl:w-3/4 mx-auto">
    <div class="nbaql-goals-container">
      <p>Short Term (3 months)</p>
      <ul>
        <li>Be able to handle box score data from every season in NBA history. Will need to implement lazy loading and create abstract views such as season and career</li>
        <li>Images for players</li>
        <li>Expand With Step ability</li>
      </ul>

      <p class="pt-10">Long Term (1 year)</p>
  		<ul>
        <li>Build a sql-like database from scratch out of Golang or C to directly query from</li>
        <li>More Data such as NBA combine, player info, historical game odds</li>
        <li>allow custom data fields</li>
        <li>add in more plot types</li>
      </ul>

      <p class="pt-10">Long Long Term (2-3 years)</p>
      <ul>
        <li>NLP search</li>
        <li>More Sports</li>
      </ul>
  	</div>
  </div>
</div>

<style>
    .nbaql-goals-container {
      padding: 3rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
    }

    ul {
        list-style-type: disc;
        padding: 20px 50px;
    }
</style>