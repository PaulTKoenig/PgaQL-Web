<script lang="ts">
  import { NbaqlHeader, NbaqlSidebar } from '$lib';
</script>

<NbaqlHeader />
<div class="lg:flex">
  <div class="w-full lg:w-1/3 xl:w-1/4 mx-auto pb-10 md:pb-20">
    <NbaqlSidebar />
  </div>

  <div class="flex flex-col gap-10 w-full lg:w-2/3 xl:w-3/4 mx-auto pb-20">
    <div class="nbaql-main-container">
  		Docs
  	</div>
  </div>
</div>

<style>
    .nbaql-main-container {
      padding: 3rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
    }
</style>