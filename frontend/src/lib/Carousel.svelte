<script>
  import { onMount } from 'svelte';
  import EmblaCarousel from 'embla-carousel';
  let pgaqlSnapshot = '/pgaql.png';

  let embla;
  let prevButton;
  let nextButton;
  let selectedIndex = 0;
  
  const slides = [1, 2, 3, 4, 5];

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
    	      <p class="text-xl font-bold">
              PgaQL
            </p>
            <p class="text-lg pt-3 hidden lg:block">
              Interpreter for the developed language 'PgaQL' that allows users to easily find trends in their favorite athletes and teams
            </p>
            <p class="text-lg pt-3 block lg:hidden">
              Interpreter for the developed language 'PgaQL'
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">C</div>
              <div class="project-tag bg-teal">Svelte</div>
              <div class="project-tag bg-copper dark-text">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn" href="/pgaql">Demo</a>
          </div>
        </div>
        <img src={pgaqlSnapshot} alt="PgaQL Interpreter" class="p-3 rounded-2xl hidden xl:block" />
	    </div>
	  </div>
    <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl font-bold">
              basket hoopz
            </p>
            <p class="text-lg pt-3 hidden lg:block">
              Predictive model for future NCAA basketball matchups with a 73% accuracy rate, based on analysis of 2,129 games during the 2022-23 season
            </p>
            <p class="text-lg pt-3 block lg:hidden">
              Predictive model for future basketball matchups with a 73% accuracy
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">Python</div>
              <div class="project-tag bg-copper">Data Science</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl font-bold">
              baketballs r us
            </p>
            <p class="text-lg pt-3 hidden lg:block">
              worse version of toys r us
            </p>
            <p class="text-lg pt-3 block lg:hidden">
              worse version of toys r us
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">React</div>
              <div class="project-tag bg-teal">Express.js</div>
              <div class="project-tag bg-teal">MongoDB</div>
              <div class="project-tag bg-copper">Full Stack</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="embla__slide">
      <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl font-bold">
              no code coding
            </p>
            <p class="text-lg pt-3 hidden lg:block">
              Web application enabling users to interact with datasets and experiment building and fine-tuning ML models without coding
            </p>
            <p class="text-lg pt-3 block lg:hidden">
              No code solution to machine learning model development
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">React</div>
              <div class="project-tag bg-copper">Frontend</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn coming-soon-btn">
              <div>Article Coming Soon</div>
            </a>
          </div>
        </div>
      </div>
    </div>
	  <div class="embla__slide">
	    <div class="carousel-item">
        <div class="p-10 flex flex-col">
          <div>
            <p class="text-xl font-bold">
              SO VITS SVC clip generator
            </p>
            <p class="text-lg pt-3">
              Data collection project to automate creating AI voice clones
            </p>
            <div class="project-tags-container">
              <div class="project-tag bg-teal">Python</div>
              <div class="project-tag bg-copper">Backend</div>
            </div>
          </div>
          <div class="carousel-action-btns-container">
            <a class="carousel-action-btn coming-soon-btn">
              <div>Demo Coming Soon</div>
            </a>
          </div>
        </div>
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

  .carousel-item {
    width: 80%;
    height: 310px;
    display: flex;
    justify-content: left;
    text-align: left;
    border-radius: 10px;
/*    border: 5px solid #03DAC6;*/
    background-color: lightgrey;
  }

  .slides-nav-container {
    display: flex;
    align-items: center;
    margin: 1rem 10% 0;
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
    margin-top: 1rem;
    align-items: center;
  }

  @media (max-width: 768px) {
      .project-tags-container {
          display: none;
      }
  }

  .project-tag {
    color: #F0F0F0;
    padding: .25rem .75rem;
    border-radius: 4px;
    font-size: small;
  }

  .bg-copper {
    background-color: #B87333;
  }

  .bg-teal {
    background-color: #018786;
  }
</style>
