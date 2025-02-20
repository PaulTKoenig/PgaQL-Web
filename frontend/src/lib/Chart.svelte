<script>
  import { onMount } from 'svelte';
  import { Chart, LinearScale, PointElement, Title, Tooltip, Legend, ScatterController } from 'chart.js';

  Chart.register(LinearScale, PointElement, Title, Tooltip, Legend, ScatterController);

  export let data = [];

  let chartContainer;
  let chartInstance;

  function updateChartData() {
    console.log("1")
    if (chartInstance) {
      console.log("2")
      chartInstance.data.datasets[0].data = data.map(item => ({ x: item[0], y: item[1] }));
      chartInstance.update();
    }
  }

  let resizeTimeout;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      chartInstance.resize();
    }, 100);
  });

  onMount(() => {

    const chartData = {
      datasets: [{
        label: 'Scatter Dataset',
        data: data.map(item => ({ x: item[0], y: item[1] })),
        backgroundColor: 'rgba(75, 192, 192, 1)',
        pointRadius: 5
      }]
    };

    const config = {
      type: 'scatter',
      data: chartData,
      options: {
        scales: {
          x: {
            type: 'linear',
            position: 'bottom'
          },
          y: {
            type: 'linear',
            position: 'left'
          }
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: function(tooltipItem) {
                const x = tooltipItem.raw.x;
                const y = tooltipItem.raw.y;
                return `X: ${x}, Y: ${y}`;
              }
            }
          }
        }
      }
    };
    const ctx = chartContainer.getContext('2d');
    chartInstance = new Chart(ctx, config);
  });

  $: {
    if (data.length > 0) {
      updateChartData();
    }
  }
</script>

<style>
  canvas {
    width: 100%;
    height: 100%;
  }
</style>

<div>
  <canvas bind:this={chartContainer}></canvas>
</div>
