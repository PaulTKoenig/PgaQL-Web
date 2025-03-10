export const queryBuilderSteps = [
    {
        step: "1",
        title: "What would you like to plot?",
        options: [
        	{ 
        		label: "Player Game Stats", 
        		value: "CHART box_score"
        	}
        ]
    },
    {
        step: "2",
        title: "What type of Chart would you like to use?",
        options: [
        	{
        		label: "Scatter Plot",
        		value: "IN scatter_plot",
        	}
        ]
    },
    {
        step: "3",
        title: "What stat would you like on the X-Axis?",
        options: [
        	{ 
        		label: "Field Goal Attempts", 
        		value: "FOR fga"
        	}
        ]
    },
    {
        step: "4",
        title: "What stat would you like on the Y-Axis?",
        options: [
        	{
        		label: "Field Goals Made",
        		value: "VS fgm",
        	}
        ]
    },
    {
        step: "5",
        title: "Add any where conditions?",
        options: [
        	{
        		label: "Team is the Cleveland Cavaliers",
        		value: "WHERE team_abbr = 'CLE'",
        	}
        ]
    },
    {
        step: "6",
        title: "Your Query is Finshed!"
    },
];