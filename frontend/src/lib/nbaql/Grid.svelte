<script lang="ts">
    import { onMount } from 'svelte';
    import {
        createGrid,
        ModuleRegistry,
        ClientSideRowModelModule,
        type GridOptions,
        themeQuartz,
        colorSchemeDarkBlue
    } from 'ag-grid-community';

    // Register AG Grid Modules
    ModuleRegistry.registerModules([ClientSideRowModelModule]);

	export let data = {};
	export let playerData = new Map();
    let columnDefs: Array<any> = [
        { headerName: 'Player', field: 'player' },
        { headerName: data.x_column_name, field: 'stat1'},
        { headerName: data.y_column_name, field: 'stat2' }
    ];
    let rowData: Array<any> = [];

    const darkTheme = themeQuartz.withPart(colorSchemeDarkBlue).withParams({
        backgroundColor: '#212121',
        foregroundColor: '#ffffff',
        headerBackgroundColor: '#37474f',
        headerTextColor: '#cfd8dc',
        oddRowBackgroundColor: '#263238'
    });

    let gridDiv: HTMLDivElement;

    onMount(() => {
		rowData = data.rowData.map((row) => {
			return { 
				player: playerData.get(row[0]),
				stat1: row[1],
				stat2: row[2]
			};
		});

        const gridOptions: GridOptions<any> = {
            theme: darkTheme,
            columnDefs,
            rowData,
            defaultColDef: {
                sortable: true,
                filter: true,
                flex: 1
            }
        };

        if (gridDiv) {
            createGrid(gridDiv, gridOptions);
        }
    });
</script>

<div bind:this={gridDiv} style="height: 400px; width: 100%;"></div>