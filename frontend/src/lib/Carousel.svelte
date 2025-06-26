<script>
  import { onMount } from 'svelte';
  import EmblaCarousel from 'embla-carousel';
  let nbaqlSnapshot = '/nbaql.png';
  let bball_r_us = '/bball-r-us.png';
  let bball_chart = '/bball-chart.webp';
  let mlexpress = '/mlexpress.png';

  let embla;
  let prevButton;
  let nextButton;
  let selectedIndex = 0;
  
  const slides = [1, 2, 3];

  onMount(() => {
    const emblaNode = document.querySelector('.embla');
    embla = EmblaCarousel(emblaNode, {
      loop: true,
      speed: 5,
    });


    // Update selected index on slide change
    embla.on('select', () => {
      selectedIndex = embla.selectedScrollSnap();
    });

    // Linking navigation buttons
    prevButton.addEventListener('click', () => embla.scrollPrev());
    nextButton.addEventListener('click', () => embla.scrollNext());
  });
</script>

<div>
	<div class="embla">
	<div class="embla__container">
	  <div class="embla__slide">


      <div class="small-carousel-item">
        <img src={nbaqlSnapshot} alt="NbaQL Interpreter" class="p-3 rounded-2xl block w-13/24" />
        <div class="flex flex-col gap-4 overflow-hidden mt-auto pb-4">
          <div>
            <p class="text-base 2xl:text-xl font-bold">
              NbaQL Interpreter & UI
            </p>
            <p class="text-sm 2xl:text-lg block lg:hidden">
              Interpreter for the developed language 'NbaQL'
            </p>
            <div class="small-project-tags-container">
              <div class="project-tag bg-teal">C</div>
              <div class="project-tag bg-teal">Svelte</div>
              <div class="project-tag bg-teal">Docker</div>
              <div class="project-tag bg-copper dark-text">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn text-xs" href="/nbaql/build-a-query">
              Demo
            </a>
          </div>
        </div>
      </div>



	    <div class="carousel-item">
        <div class="p-5 xl:p-10 flex flex-col gap-12">
          <div>
    	      <p class="text-lg 2xl:text-xl font-bold">
              NbaQL Interpreter & UI
            </p>
            <p class="text-base pt-3 hidden lg:block">
              Interpreter for the developed language 'NbaQL' that allows users to easily find trends in their favorite athletes and teams
            </p>
            <p class="text-base pt-2 block lg:hidden">
              Interpreter for the developed language 'NbaQL'
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">C</div>
              <div class="project-tag bg-teal">Svelte</div>
              <div class="project-tag bg-teal">Docker</div>
              <div class="project-tag bg-copper dark-text">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn" href="/nbaql/build-a-query">
              Demo
            </a>
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
        <img src={nbaqlSnapshot} alt="NbaQL Interpreter" class="p-3 rounded-2xl block ml-auto w-7/12 lg:w-1/2 2xl:w-auto h-3/4 sm:h-full" />
	    </div>


	  </div>
    <div class="embla__slide">


      <div class="small-carousel-item">
        <img src={bball_chart} alt="Basketball Data Chart" class="p-3 rounded-2xl block w-2/3" />
        <div class="px-10 flex flex-col gap-4 overflow-hidden mt-auto pb-4">
          <div>
            <p class="text-base 2xl:text-xl font-bold">
              Statistical Approach to Predicting NCAAB Outcomes
            </p>
            <p class="text-sm 2xl:text-lg block lg:hidden">
              Predictive model for future basketball matchups with a 73% accuracy
            </p>
            <div class="small-project-tags-container">
              <div class="project-tag bg-teal">Python</div>
              <div class="project-tag bg-copper">Data Science</div>
            </div>
          </div>
        </div>
      </div>


      <div class="hidden xl:carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-lg 2xl:text-xl font-bold">
              Statistical Approach to Predicting NCAAB Outcomes
            </p>
            <p class="text-base 2xl:text-lg pt-3 hidden 2x:block">
              Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season. Outperformed when compared to similar models across the same game range (such as TeamRanking.com - 71.2%)
            </p>
            <p class="text-base 2xl:text-lg pt-3 block 2x:hidden">
              Predictive model for future basketball matchups with a 73% accuracy
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">Python</div>
              <div class="project-tag bg-copper">Data Science</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <!-- <a class="carousel-action-btn" href="/articles/003">Read More</a> -->
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
        <div class="flex items-center h-full">
          <img src={bball_chart} alt="Basketball Data Chart" class="p-3 rounded-2xl ml-auto hidden xl:block" />
        </div>
      </div>


    </div>
    <div class="embla__slide">


      <div class="small-carousel-item">
        <img src={mlexpress} alt="MLExpress" class="p-3 rounded-2xl block w-11/12" />
        <div class="px-10 flex flex-col gap-4 overflow-hidden mt-auto pb-4">
          <div>
            <p class="text-base 2xl:text-xl font-bold">
              MLExpress
            </p>
            <p class="text-sm 2xl:text-lg block lg:hidden">
              No code solution to machine learning model development
            </p>
            <div class="small-project-tags-container">
              <div class="project-tag bg-teal">React</div>
              <div class="project-tag bg-copper">Frontend</div>
            </div>
          </div>
        </div>
      </div>



      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-lg 2xl:text-xl font-bold">
              MLExpress
            </p>
            <p class="text-base 2xl:text-lg pt-3 hidden lg:block">
              Web application enabling users to interact with datasets and experiment building and fine-tuning ML models without coding
            </p>
            <p class="text-base 2xl:text-lg pt-3 block lg:hidden">
              No code solution to machine learning model development
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">React</div>
              <div class="project-tag bg-copper">Frontend</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <!-- <a class="carousel-action-btn" href="/articles/001">
              Read More
            </a> -->
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
        <img src={mlexpress} alt="MLExpress" class="p-3 rounded-2xl ml-auto hidden 3x:block" />
        <img src={mlexpress} alt="MLExpress" class="p-3 rounded-2xl ml-auto hidden xl:block 2x:hidden w-1/2" />


      </div>
    </div>
    <!-- <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl font-bold">
              Basketballs "R" Us
            </p>
            <p class="text-lg pt-3 hidden lg:block">
              One stop e-commerce shop for all things basketball with fully functional inventory management and order processing. 
            </p>
            <p class="text-lg pt-3 block lg:hidden">
              One stop ecommerce shop for all things basketball.
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">React</div>
              <div class="project-tag bg-teal">Express.JS</div>
              <div class="project-tag bg-teal">Kafka</div>
              <div class="project-tag bg-copper">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn" href="/articles/002">
              Read More
            </a>
          </div>
        </div>
        <img src={bball_r_us} alt='Basketballs "R" Us' class="p-3 rounded-2xl ml-auto hidden 2x:block" />
        <img src={bball_r_us} alt='Basketballs "R" Us' class="p-3 rounded-2xl ml-auto hidden xl:block 2x:hidden w-1/2" />
      </div>
    </div> -->
	</div>
	</div>

	<div class="slides-nav-container">
    <div class="slides-nav-btn-container">
  	  <button bind:this={prevButton}>&lt;</button>
  	  <button class="ml-2" bind:this={nextButton}>&gt;</button>
    </div>

	  <div class="bubbles-container">
	    {#each slides as _, index}
	      <span 
	        class="bubble" 
	        class:selected={index === selectedIndex} 
	        on:click={() => embla.scrollTo(index)}
	      ></span>
	    {/each}
	  </div>
	</div>
</div>

<style>
  .embla {
    width: 100%;
    overflow: hidden;
  }

  .embla__container {
    display: flex;
  }

  .embla__slide {
    min-width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #121212;
  }

  .carousel-item {
    width: 90%;
    height: 100%;
    max-height: 350px;
    display: none;
    justify-content: left;
    text-align: left;
    border-radius: 10px;
    background-color: lightgrey;
  }

  .small-carousel-item {
    width: 95%;
    height: 100%;
    max-height: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: left;
    text-align: left;
    border-radius: 10px;
    background-color: lightgrey;
  }

  .slides-nav-container {
    display: flex;
    align-items: center;
    margin: 1rem 3% 0;
  }

  .slides-nav-btn-container {
    button {
      background: lightgrey;
      color: #121212;
      padding: .33rem .66rem;
      border: none;
      cursor: pointer;
      margin-top: 20px;
    }
  }

  .bubbles-container {
    display: flex;
    justify-content: center;
    margin-left: auto;
  }

  .bubble {
    width: 12px;
    height: 12px;
    margin: 0 5px;
    border-radius: 50%;
    background-color: #bbb;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .bubble.selected {
    background-color: #03DAC6;
  }

  .carousel-action-btns-container {
    margin-top: auto;
    align-self: flex-start;
    display: flex;
    gap: 1rem;
  }

  .carousel-action-btn {
    background-color: #333333;
    color: #F0F0F0;
    padding: .5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
  }

  .coming-soon-btn {
    display: none;
    cursor: initial;
    background: repeating-linear-gradient(
      45deg,
      yellow,
      yellow 10px,
      black 10px,
      black 20px
    );

    div {
      background-color: white;
      padding: .1rem .4rem;
      color: black;
      border-radius: 4px;
    }
  }

  .project-tags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1rem;
    align-items: center;
  }

  .small-project-tags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 0.5rem;
    align-items: center;
  }

  .project-tag {
    color: #F0F0F0;
    padding: .25rem .75rem;
    border-radius: 4px;
    font-size: small;
    white-space: nowrap !important;
  }

  .bg-copper {
    background-color: #B87333;
  }

  .bg-teal {
    background-color: #018786;
  }

  @media (min-width: 800px) {
    .carousel-item {
/*      display: flex;*/
      max-height: 450px;
      display: flex;
    }

    .small-carousel-item {
      display: none;
    }

    .slides-nav-container {
      margin: 1rem 5% 0;
    }

    .coming-soon-btn {
      display: flex;
    }
  }
</style>
