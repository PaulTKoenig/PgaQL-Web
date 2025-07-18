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

    ModuleRegistry.registerModules([ClientSideRowModelModule]);

	export let data = {};
	export let playerData = new Map();

    const isMobile = window.innerWidth < 600;

    let columnDefs: Array<any> = [
    { headerName: 'Player', field: 'player', minWidth: 150 },
    { headerName: data.x_column_name, field: 'stat1', minWidth: 75, flex: 1 },
    { headerName: data.y_column_name, field: 'stat2', minWidth: 75, flex: 1 }
];
    let rowData: Array<any> = [];

    const darkTheme = themeQuartz.withPart(colorSchemeDarkBlue).withParams({
        backgroundColor: '#212121',
        foregroundColor: '#ffffff',
        headerBackgroundColor: '#37474f',
        headerTextColor: '#cfd8dc',
        oddRowBackgroundColor: '#263238',
        fontSize: isMobile ? 10 : 14
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
                resizable: true
            }
        };
    
        if (gridDiv) {
            createGrid(gridDiv, gridOptions);
        }
    });
</script>

<div bind:this={gridDiv} style="height: 400px; width: 100%;"></div>