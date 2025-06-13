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
      <p>Short Term (3-6 months)</p>
      <ul>
        <li>Support complete historical NBA box score data, including efficient handling through lazy loading and abstract views such as per-season and career summaries.</li>
        <li>Display player images alongside relevant stats and visualizations.</li>
        <li>Introduce additional plot types to enhance data exploration and visualization capabilities.</li>
        <li>Enhance the WITH clause functionality to support advanced logical operators and enable users to define custom data fields derived from existing ones.</li>
      </ul>

      <p class="pt-10">Long Term (1+ years)</p>
  		<ul>
        <li>Develop a relational database engine from scratch using Go or C to optimize performance and provide direct querying capabilities over the dataset.</li>
        <li>Implement a natural language interface to allow users to search and analyze data using conversational queries.</li>
        <li>Expand the dataset and query capabilities to include more detailed basketball data and support for other sports.</li>
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


  @media (max-width: 1500px) {
      ul {
          padding: 10px 25px;
      }
    }
</style>