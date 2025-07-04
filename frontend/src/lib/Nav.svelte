<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import { page } from '$app/state';
    let githubLogo = '/github-svg.svg';
    let linkedinLogo = '/icons8-linkedin.svg';
    let downloadIcon = '/download-icon.svg';
    let whiteDownloadIcon = '/white-download-icon.svg';
    let resumePdf = '/Resume-Paul-Koenig-25.pdf';

    let showPreview = false;
    const togglePreview = () => {
        showPreview = !showPreview;
        closeNav();
    }

    let showNav = false;
    const toggleNav = () => {
        showNav = !showNav;
        updateBlur();
    }
    const closeNav = () => {
        showNav = false;
        updateBlur();
    }

    function updateBlur() {
        const body = document.querySelector('.page-body');
        if (body) {
            if (showNav || showPreview) {
                body.classList.add('blurred');
            } else {
                body.classList.remove('blurred');
            }
        }
    }

    let resumePreviewElem: HTMLElement;

    function handleClickOutside(event: MouseEvent) {
        if (resumePreviewElem && !resumePreviewElem.contains(event.target as Node) && event.target.id !== "resume-preview-btn") {
            togglePreview();
            updateBlur();
        }
    }

    function handleResizeBlur() {
        if (showNav) {
            const currentWidth = window.innerWidth;

            if (currentWidth > 799) {
                closeNav();
            }
        }
    }

    function downloadResume() {
        const link = document.createElement('a');
        link.href = resumePdf;
        link.download = 'Paul_Koenig_Resume.pdf';
        link.click();
        document.body.removeChild(link);
    }

    onMount(() => {
        document.addEventListener('click', handleClickOutside);
        window.addEventListener('resize', handleResizeBlur);
    });

    onDestroy(() => {
        if (typeof document !== 'undefined') {
            document.removeEventListener('click', handleClickOutside);
            window.removeEventListener('resize', handleResizeBlur);
        }
    });
</script>


<div class="nav-bar fixed w-full flex h-14 z-10">
    <a class="nav-home my-auto ml-5 hover:underline cursor-pointer" href="/">
        Paul Koenig
    </a>
    <div class="default-nav-buttons">
            <a
                class="nav-btn"
                href="/projects"
                class:active={page.url.pathname === '/projects'}
            >
                Projects
            </a>
            <!-- <a
                class="nav-btn"
                href="/articles"
                class:active={page.url.pathname === '/articles'}
            >
                Articles
            </a> -->
            <a
                class="nav-btn"
                href="/nbaql/build-a-query"
                class:active={page.url.pathname.includes('/nbaql')}
            >
                NbaQL
            </a>
            <div
                id="resume-preview-btn"
                class="nav-btn"
                onclick={togglePreview}
            >
                Resume
            </div>
        </div>
    <div class="flex my-auto ml-auto mr-5 gap-1">
        <div tabindex="0" onblur={closeNav}>
            <button class="nav-dropdown-btn" class:nav-dropdown-btn-close={showNav} onclick={toggleNav}>
                {#if showNav}
                    ✕
                {:else}
                    ☰
                {/if}
            </button> 
            <div class="nav-dropdown" class:show-nav-dropdown={showNav}>
                <a
                    class="nav-btn nav-dropdown-item"
                    href="/"
                    class:active={page.url.pathname === '/'}
                    onclick={closeNav}
                >
                    Home
                </a>
                <a
                    class="nav-btn nav-dropdown-item"
                    href="/projects"
                    class:active={page.url.pathname === '/projects'}
                    onclick={closeNav}
                >
                    Projects
                </a>
                <!-- <a
                    class="nav-btn nav-dropdown-item"
                    href="/articles"
                    class:active={page.url.pathname === '/articles'}
                    onclick={closeNav}
                >
                    Articles
                </a> -->
                <a
                    class="nav-btn nav-dropdown-item"
                    href="/nbaql/build-a-query"
                    class:active={page.url.pathname.includes('/nbaql')}
                    onclick={closeNav}
                >
                    NbaQL
                </a>
                <div
                    id="resume-preview-btn"
                    class="nav-btn"
                    onclick={togglePreview}
                >
                    Resume
                </div>
                <div class="small-screen-nav-logos">
                    <a class="small-screen-social-media-nav-logo" href="https://www.linkedin.com/in/paul-koenig-">
                        <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 30 30" width="40px" height="100%">    
                            <path class="linkedin-icon" d="M24,4H6C4.895,4,4,4.895,4,6v18c0,1.105,0.895,2,2,2h18c1.105,0,2-0.895,2-2V6C26,4.895,25.105,4,24,4z M10.954,22h-2.95 v-9.492h2.95V22z M9.449,11.151c-0.951,0-1.72-0.771-1.72-1.72c0-0.949,0.77-1.719,1.72-1.719c0.948,0,1.719,0.771,1.719,1.719 C11.168,10.38,10.397,11.151,9.449,11.151z M22.004,22h-2.948v-4.616c0-1.101-0.02-2.517-1.533-2.517 c-1.535,0-1.771,1.199-1.771,2.437V22h-2.948v-9.492h2.83v1.297h0.04c0.394-0.746,1.356-1.533,2.791-1.533 c2.987,0,3.539,1.966,3.539,4.522V22z"/>
                        </svg>
                    </a>
                    <a class="small-screen-social-media-nav-logo" href="mailto:paul.koenig.002@gmail.com">
                        <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M3.75 5.25L3 6V18L3.75 18.75H20.25L21 18V6L20.25 5.25H3.75ZM4.5 7.6955V17.25H19.5V7.69525L11.9999 14.5136L4.5 7.6955ZM18.3099 6.75H5.68986L11.9999 12.4864L18.3099 6.75Z" fill="#EDEDED"/>
                        </svg>
                    </a>
                    <a class="small-screen-social-media-nav-logo" href="https://github.com/PaulTKoenig">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" width="33px" height="100%">
                            <path class="github-icon" d="M17.791,46.836C18.502,46.53,19,45.823,19,45v-5.4c0-0.197,0.016-0.402,0.041-0.61C19.027,38.994,19.014,38.997,19,39c0,0-3,0-3.6,0c-1.5,0-2.8-0.6-3.4-1.8c-0.7-1.3-1-3.5-2.8-4.7C8.9,32.3,9.1,32,9.7,32c0.6,0.1,1.9,0.9,2.7,2c0.9,1.1,1.8,2,3.4,2c2.487,0,3.82-0.125,4.622-0.555C21.356,34.056,22.649,33,24,33v-0.025c-5.668-0.182-9.289-2.066-10.975-4.975c-3.665,0.042-6.856,0.405-8.677,0.707c-0.058-0.327-0.108-0.656-0.151-0.987c1.797-0.296,4.843-0.647,8.345-0.714c-0.112-0.276-0.209-0.559-0.291-0.849c-3.511-0.178-6.541-0.039-8.187,0.097c-0.02-0.332-0.047-0.663-0.051-0.999c1.649-0.135,4.597-0.27,8.018-0.111c-0.079-0.5-0.13-1.011-0.13-1.543c0-1.7,0.6-3.5,1.7-5c-0.5-1.7-1.2-5.3,0.2-6.6c2.7,0,4.6,1.3,5.5,2.1C21,13.4,22.9,13,25,13s4,0.4,5.6,1.1c0.9-0.8,2.8-2.1,5.5-2.1c1.5,1.4,0.7,5,0.2,6.6c1.1,1.5,1.7,3.2,1.6,5c0,0.484-0.045,0.951-0.11,1.409c3.499-0.172,6.527-0.034,8.204,0.102c-0.002,0.337-0.033,0.666-0.051,0.999c-1.671-0.138-4.775-0.28-8.359-0.089c-0.089,0.336-0.197,0.663-0.325,0.98c3.546,0.046,6.665,0.389,8.548,0.689c-0.043,0.332-0.093,0.661-0.151,0.987c-1.912-0.306-5.171-0.664-8.879-0.682C35.112,30.873,31.557,32.75,26,32.969V33c2.6,0,5,3.9,5,6.6V45c0,0.823,0.498,1.53,1.209,1.836C41.37,43.804,48,35.164,48,25C48,12.318,37.683,2,25,2S2,12.318,2,25C2,35.164,8.63,43.804,17.791,46.836z"/>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <div class="large-screen-nav-logos">
            <a class="social-media-nav-logo" href="https://www.linkedin.com/in/paul-koenig-">
                <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 30 30" width="30px" height="100%">    
                    <path class="linkedin-icon" d="M24,4H6C4.895,4,4,4.895,4,6v18c0,1.105,0.895,2,2,2h18c1.105,0,2-0.895,2-2V6C26,4.895,25.105,4,24,4z M10.954,22h-2.95 v-9.492h2.95V22z M9.449,11.151c-0.951,0-1.72-0.771-1.72-1.72c0-0.949,0.77-1.719,1.72-1.719c0.948,0,1.719,0.771,1.719,1.719 C11.168,10.38,10.397,11.151,9.449,11.151z M22.004,22h-2.948v-4.616c0-1.101-0.02-2.517-1.533-2.517 c-1.535,0-1.771,1.199-1.771,2.437V22h-2.948v-9.492h2.83v1.297h0.04c0.394-0.746,1.356-1.533,2.791-1.533 c2.987,0,3.539,1.966,3.539,4.522V22z"/>
                </svg>
            </a>
            <a class="social-media-nav-logo" href="mailto:paul.koenig.002@gmail.com">
                <svg width="32px" height="32px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.75 5.25L3 6V18L3.75 18.75H20.25L21 18V6L20.25 5.25H3.75ZM4.5 7.6955V17.25H19.5V7.69525L11.9999 14.5136L4.5 7.6955ZM18.3099 6.75H5.68986L11.9999 12.4864L18.3099 6.75Z" fill="#EDEDED"/>
                </svg>
            </a>
            <a class="social-media-nav-logo" href="https://github.com/PaulTKoenig">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" width="25px" height="100%">
                    <path class="github-icon" d="M17.791,46.836C18.502,46.53,19,45.823,19,45v-5.4c0-0.197,0.016-0.402,0.041-0.61C19.027,38.994,19.014,38.997,19,39c0,0-3,0-3.6,0c-1.5,0-2.8-0.6-3.4-1.8c-0.7-1.3-1-3.5-2.8-4.7C8.9,32.3,9.1,32,9.7,32c0.6,0.1,1.9,0.9,2.7,2c0.9,1.1,1.8,2,3.4,2c2.487,0,3.82-0.125,4.622-0.555C21.356,34.056,22.649,33,24,33v-0.025c-5.668-0.182-9.289-2.066-10.975-4.975c-3.665,0.042-6.856,0.405-8.677,0.707c-0.058-0.327-0.108-0.656-0.151-0.987c1.797-0.296,4.843-0.647,8.345-0.714c-0.112-0.276-0.209-0.559-0.291-0.849c-3.511-0.178-6.541-0.039-8.187,0.097c-0.02-0.332-0.047-0.663-0.051-0.999c1.649-0.135,4.597-0.27,8.018-0.111c-0.079-0.5-0.13-1.011-0.13-1.543c0-1.7,0.6-3.5,1.7-5c-0.5-1.7-1.2-5.3,0.2-6.6c2.7,0,4.6,1.3,5.5,2.1C21,13.4,22.9,13,25,13s4,0.4,5.6,1.1c0.9-0.8,2.8-2.1,5.5-2.1c1.5,1.4,0.7,5,0.2,6.6c1.1,1.5,1.7,3.2,1.6,5c0,0.484-0.045,0.951-0.11,1.409c3.499-0.172,6.527-0.034,8.204,0.102c-0.002,0.337-0.033,0.666-0.051,0.999c-1.671-0.138-4.775-0.28-8.359-0.089c-0.089,0.336-0.197,0.663-0.325,0.98c3.546,0.046,6.665,0.389,8.548,0.689c-0.043,0.332-0.093,0.661-0.151,0.987c-1.912-0.306-5.171-0.664-8.879-0.682C35.112,30.873,31.557,32.75,26,32.969V33c2.6,0,5,3.9,5,6.6V45c0,0.823,0.498,1.53,1.209,1.836C41.37,43.804,48,35.164,48,25C48,12.318,37.683,2,25,2S2,12.318,2,25C2,35.164,8.63,43.804,17.791,46.836z"/>
                </svg>
            </a>
        </div>
    </div>
</div>
{#if showPreview}
    <div
        class="resume-preview"
        bind:this={resumePreviewElem}
    >
        <div class="resume-preview-header">
            <button 
                class="nav-btn"
                onclick={downloadResume}
            >
                <img src={downloadIcon} alt="Download Icon" />
            </button>
            <button 
                class="nav-btn resume-preview-close"
                onclick={togglePreview}
            >
                ✕
            </button>
        </div>
        <iframe
            src={resumePdf}
            height="100%"
            width="100%"
        ></iframe>
    </div>
{/if}

<style>

    @media (min-width: 800px) {
        .nav-dropdown-btn, .nav-dropdown {
            display: none;
        }

        .social-media-nav-logo:first-of-type {
            margin-left: 1.25rem;
        }

        .nav-dropdown {
            display: none !important;
        }

        :global(.pdf-blurred) {
            filter: blur(3px) !important;
            -webkit-filter: blur(3px) !important;
        }

        :global(.nav-blurred) {
            filter: blur(3px) !important;
            -webkit-filter: blur(3px) !important;
        }
    }

    @media (max-width: 799px) {
        .default-nav-buttons {
            display: none !important;
        }

        .large-screen-nav-logos {
            display: none !important;
        }

        .nav-home::before {
            display: none;
        }

        .nav-btn {
            font-size: 20px;
        }

        .nav-dropdown-item:hover {
            background-color: #555555 !important;

        }

        .social-media-nav-logo:first-of-type {
            margin-left: 0.75rem;
        }
    }

    .large-screen-nav-logos {
        display: contents;
    }

    .nav-dropdown-btn {
        position: relative;
        font-size: x-large;
        padding: 0.15rem 0.65rem 0.25rem;
        text-align: center;
        z-index: 2;
        border: none;
    }

    .nav-dropdown-btn-close {
        padding: 0.25rem 0.65rem;
    }

    .nav-dropdown-btn:hover {
        background-color: #333333 !important;
        border: none;
    }

    .nav-bar {
        background-color: rgba(32,33,36,.5);
        backdrop-filter: blur(10px);
    }

    .nav-btn {
        cursor: pointer;
        padding: .5rem .75rem;
        border-radius: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .nav-btn:hover, .social-media-nav-logo:hover, .small-screen-social-media-nav-logo:hover {
      background-color: #333333;
    }

    .nav-btn.active {
        color: #03DAC6;
    }

    .nav-home {
        position: relative;
        display: flex;
        font-weight: bolder;
        font-size: 20px;
    }

    .nav-home::before {
        content: "";
        position: absolute;
        top: 4px;
        right: -24px;
        border: 0.5px solid #888888;
        height: calc(100% - 8px);
    }

    .social-media-nav-logo, .small-screen-social-media-nav-logo {
        padding: 0 .5rem;
        border-radius: 4px;
        display: flex;
        align-items: center;
    }

    .github-icon, .linkedin-icon {
        fill: #F0F0F0;
    }

    .nav-dropdown {
        position: absolute;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #333333;
        top: 0;
        right: 0;
        z-index: 1;
        padding-top: 50px;
        height: 100vh;
        width: 40vw;
        min-width: 250px;
        box-shadow: -6px 0 8px rgba(0, 0, 0, 0.2);

        transform: translateX(100%);
        transition: transform 200ms ease-in-out;
    }

    .nav-dropdown.show-nav-dropdown {
        transform: translateX(0);
    }

    .default-nav-buttons {
        display: flex;
        align-items: center;
        margin-left: 36px;
    }

    .small-screen-nav-logos {
        position: relative;
        display: flex;
        margin-top: 2.5rem;
    }

    .small-screen-nav-logos::before {
        content: "";
        position: absolute;
        top: -20px;
        border: 1px solid #222222;
        left: 0;
        width: 100%;
    }

    .nav-btn-download-resume {
        margin: 1rem 0 1.5rem;
        border: 2px solid #222222;
        border-radius: 8px;
        padding: .5rem .75rem;
        cursor: pointer;
        color: black;
        background-color: white;
        display: flex;
        gap: 4px;
    }

    .resume-preview {
        position: fixed;
        top: 50px;
        height: calc(100% - 120px);
        width: 90%;
        left: 5%;
        border: none;
        margin-top: 1rem;
        z-index: 3;
    }

    .resume-preview-header {
        padding: 8px;
        height: 44px;
        background-color: #999999;
        display: flex;
        justify-content: right;
        gap: 12px;

        button {
            padding: 4px 6px;
        }
    }

    .resume-preview-close {
        color: black;
        font-weight: 0;
        margin-right: 6px;
    }

    :global(.blurred) {
        filter: blur(3px) !important;
        -webkit-filter: blur(3px) !important;
    }
</style>