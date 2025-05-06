<script>
  import { onMount } from 'svelte';
  import { Chart, LinearScale, PointElement, Title, Tooltip, Legend, ScatterController } from 'chart.js';

  Chart.register(LinearScale, PointElement, Title, Tooltip, Legend, ScatterController);

  export let data = [];

  let chartContainer;
  let chartInstance;
  let playerData = new Map();

  let hoveredPoint = null;

  function updateChartData() {
    if (chartInstance) {
      chartInstance.data.datasets[0].data = data.map(item => ({ playerId: item[0], x: item[1], y: item[2] }));
      chartInstance.update();
    }
  }

  async function fetchPlayerData(playerId) {
    let error = null;

    try {
      const response = await fetch("/api/get-player-details/" + playerId);

      if (!response.ok) {
        throw new Error('Sorry something went wrong. Please try again');
      }

      const responseJson = await response.json();

      return responseJson;

    } catch (err) {
      error = err.message;
      console.error(error)
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
        data: data.map(item => ({ playerId: item[0], x: item[1], y: item[2] })),
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
          },
          onHover: function(event, elements) {
            if (elements.length > 0) {
              const element = elements[0];
              const datasetIndex = element.datasetIndex;
              const index = element.index;
              const hoveredData = chartData.datasets[datasetIndex].data[index];

              hoveredPoint = hoveredData;
            } else {
              hoveredPoint = null;
            }
          }
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: function(tooltipItem) {
                const playerId = tooltipItem.raw.playerId;
                return `Player: ${playerData.get(playerId)}`;
              },
              footer: (tooltipItems) => {
                const first = tooltipItems[0];
                const x = first.raw.x;
                const y = first.raw.y;
                return `X: ${x}, Y: ${y}`;
              }
            }
          }
        }
      }
    };
    const ctx = chartContainer.getContext('2d');
    chartInstance = new Chart(ctx, config);

    async function loadPlayerData() {
      const promises = data.map(item => fetchPlayerData(item[0]));
      const players = await Promise.all(promises);
      playerData = new Map(players.map(player => [player[0], `${player[1]} ${player[2]}`]));
    }
    loadPlayerData();
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
