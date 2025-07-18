<script>
  import { onMount } from 'svelte';
  import { Chart, LinearScale, PointElement, Title, Tooltip, Legend, ScatterController } from 'chart.js';

  Chart.register(LinearScale, PointElement, Title, Tooltip, Legend, ScatterController);

  export let data = {};
  export let playerData = new Map();

  const isMobile = window.innerWidth < 600;

  let chartContainer;
  let chartInstance;

  let hoveredPoint = null;

  function updateChartData() {
    if (chartInstance) {
      chartInstance.data.datasets[0].data = data.rowData.map(item => ({ playerId: item[0], x: item[1], y: item[2] }));
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
        data: data.rowData.map(item => ({ playerId: item[0], x: item[1], y: item[2] })),
        backgroundColor: 'rgba(75, 192, 192, 1)',
        pointRadius: 5
      }]
    };

    const config = {
      type: 'scatter',
      data: chartData,
      options: {
        responsive: true,
        scales: {
          x: {
            type: 'linear',
            maintainAspectRatio: false,
            position: 'bottom',
            title: {
              display: true,
              text: data.x_column_name,
              color: '#999999',
              font: {
                size: isMobile ? 12 : 16,
                weight: 'bold'
              },
              padding: {
                top: 10,
                bottom: 0
              }
            },
            ticks: {
              font: {
                size: isMobile ? 10 : 14
              }
            }
          },
          y: {
            type: 'linear',
            position: 'left',
            title: {
              display: true,
              text: data.y_column_name,
              color: '#999999',
              font: {
                size: isMobile ? 12 : 16,
                weight: 'bold'
              },
              padding: {
                top: 10,
                bottom: 0,
                left: 0,
                right: 10
              }
            },
            ticks: {
              font: {
                size: isMobile ? 10 : 14
              }
            }
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
                return `${data.x_column_name}: ${x}, ${data.y_column_name}: ${y}`;
              }
            },
            bodyFont: {
              size: isMobile ? 10 : 14
            },
            footerFont: {
              size: isMobile ? 10 : 14
            }
          }
        }
      }
    };
    const ctx = chartContainer.getContext('2d');
    chartInstance = new Chart(ctx, config);

  });

  $: {
    if (data.rowData.length > 0) {
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
