<script>
    export let page;
    const changePage = (e) => {
        page = e.target.value;
    }
</script>

<div class="row">
    <select name="navigate" id="navigate-select" onchange={changePage}>
      <option value="Resume">Resume</option>
      <option value="PgaQL">PgaQL</option>
    </select>

    <div class="title">
        Paul Koenig
    </div>
</div>

<style>

    .row {
        display: flex;
        align-items: center;
        width: 100%;
    }

    .navigate {
        border-radius: 6px;
        border: 1px solid lightgray;
        padding: 0.4em 0.8em;
    }

    .title {
        font-size: large;
        font-weight: 600;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }
    
</style>