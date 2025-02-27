<script>
  import { onMount } from 'svelte';
  import EmblaCarousel from 'embla-carousel';
  import pgaqlSnapshot from '../assets/pgaql.png';

  export let page;
  const changePage = (value) => {
        page = value;
    }

  let embla;
  let prevButton;
  let nextButton;
  let selectedIndex = 0;
  
  const slides = [1, 2, 3,4 ];

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
	    <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
    	      <p class="text-xl">
              PgaQL
            </p>
            <p class="text-lg pt-3">
              Interpreter for the developed language 'PgaQL' that allows users to easily find trends in their favorite athletes and teams
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-purple-700">C</div>
              <div class="project-tag bg-yellow-600">Svelte</div>
              |
              <div class="project-tag bg-yellow-800">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <div class="carousel-action-btn" on:click={() => changePage("PgaQL")}>Demo</div>
          </div>
        </div>
        <img src={pgaqlSnapshot} alt="PgaQL Interpreter" class="p-3 rounded-2xl" />
	    </div>
	  </div>
    <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl">
              basket hoopz
            </p>
            <p class="text-lg pt-3">
              Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-green-600">Python</div>
              |
              <div class="project-tag bg-red-400">Data Science</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <div class="carousel-action-btn">Read More Here</div>
            <div class="carousel-action-btn coming-soon-btn">
              <div>Demo Coming Soon</div>
            </div>
          </div>
        </div>
        <img src={pgaqlSnapshot} alt="PgaQL Interpreter" class="p-3 rounded-2xl" />
      </div>
    </div>
    <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl">
              no code coding
            </p>
            <p class="text-lg pt-3">
              Exploratory data analysis, preprocessing, and testing machine learning models without having to write a line of code
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-blue-400">React</div>
              |
              <div class="project-tag bg-purple-400">Frontend</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <div class="carousel-action-btn">Read More Here</div>
            <div class="carousel-action-btn coming-soon-btn">
              <div>Demo Coming Soon</div>
            </div>
          </div>
        </div>
        <img src={pgaqlSnapshot} alt="PgaQL Interpreter" class="p-3 rounded-2xl" />
      </div>
    </div>
	  <div class="embla__slide">
	    <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl">
              SO VITS SVC clip generator
            </p>
            <p class="text-lg pt-3">
              Data collection project to automate creating AI voice clones
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-green-600">Python</div>
              |
              <div class="project-tag bg-blue-700">Backend</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <div class="carousel-action-btn">Demo</div>
          </div>
        </div>
        <img src={pgaqlSnapshot} alt="PgaQL Interpreter" class="p-3 rounded-2xl" />
      </div>
	  </div>
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

  .carousel-item-2 {
    width: 80%;
    height: 300px;
    display: flex;
    justify-content: center;
    text-align: left;
    border-radius: 10px;
    border: 5px solid #03DAC6;
    background-color: lightgrey;
  }

  .carousel-item {
    width: 80%;
    height: 300px;
    display: flex;
    justify-content: center;
    text-align: left;
    border-radius: 10px;
    border: 5px solid #03DAC6;
    background-color: lightgrey;
  }

  .slides-nav-container {
    display: flex;
    align-items: center;
    margin: 0 10%;
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
    background-color: #03DAC6; /* Highlighted color */
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
  }

  .coming-soon-btn {
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
    gap: 1rem;
    margin-top: .5rem;
    align-items: center;
  }

  .project-tag {
    color: #F0F0F0;
    padding: .25rem .75rem;
    border-radius: 4px;
    font-size: small;
  }
</style>
