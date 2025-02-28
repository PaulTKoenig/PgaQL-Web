<script>
    let githubLogo = '/github-svg.svg';
    let linkedinLogo = '/linkedin-icon-logo-svg-vector.svg';
</script>

<div class="nav-bar fixed w-full flex h-14 z-10">
    <a class="nav-home my-auto ml-5 cursor-pointer" href="/">
        Paul Koenig
    </a>
    <div class="flex my-auto ml-auto mr-5 gap-3">
        <a class="nav-btn" href="/about-me">About Me</a>
        <a class="nav-btn" href="/projects">Projects</a>
        <a class="nav-btn" href="/notes">Notes</a>
        <a class="social-media-nav-logo" href="https://github.com/PaulTKoenig">
            <img src={githubLogo} alt="GitHub Logo" class="max-w-full max-h-full" />
        </a>
        <a class="social-media-nav-logo" href="https://www.linkedin.com/in/paul-koenig-">
            <img src={linkedinLogo} alt="Linkedin Logo" class="max-w-full max-h-full" />
        </a>
    </div>
</div>

<style>
    .nav-bar {
/*        background-color: #202124;*/
        background-color: rgba(32,33,36,.5);
        backdrop-filter: blur(10px);
/*        box-shadow: 0 2px 6px rgba(18, 19, 20, 0.5);*/
    }

    .nav-btn:hover {
      background-color: #333333;
    }

    .nav-btn {
        cursor: pointer;
        padding: .5rem .75rem;
        border-radius: 6px;
    }

    .nav-home {
        font-weight: bolder;
    }

    .social-media-nav-logo {
        background-color: #F0F0F0;
        border-radius: 50%;
        height: 30px;
    }
</style>