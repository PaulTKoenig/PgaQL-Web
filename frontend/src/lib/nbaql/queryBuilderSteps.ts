const chartableStatFields = [
	{ 
		label: "Minutes", 
		value: "mins"
	},
	{ 
		label: "Field Goals Made", 
		value: "fgm"
	},
	{ 
		label: "Field Goal Attempts", 
		value: "fga"
	},
	{ 
		label: " Field Goal %", 
		value: "fg_pct"
	},
	{ 
		label: "Thee Pointers Made", 
		value: "three_pm"
	},
	{ 
		label: "Thee Point Attempts", 
		value: "three_pa"
	},
	{ 
		label: "Thee Point %", 
		value: "three_pct"
	},
	{ 
		label: "Free Throws Made", 
		value: "ftm"
	},
	{ 
		label: "Free Throw Attempts", 
		value: "fta"
	},
	{ 
		label: "Free Throw %", 
		value: "ft_pct"
	},
	{ 
		label: "Offensive Rebounds", 
		value: "o_reb"
	},
	{ 
		label: "Defensive Rebounds", 
		value: "d_reb"
	},
	{ 
		label: "Rebounds", 
		value: "reb"
	},
	{ 
		label: "Assists", 
		value: "ast"
	},
	{ 
		label: "Steals", 
		value: "stl"
	},
	{ 
		label: "Blocks", 
		value: "blk"
	},
	{ 
		label: "Turnovers", 
		value: "turnover"
	},
	{ 
		label: "Personal Fouls", 
		value: "pf"
	},
	{ 
		label: "Points", 
		value: "pts"
	},
	{ 
		label: "Plus / Minus", 
		value: "plus_minus"
	}
]

const allStatFields = [
	{ 
		label: "First Name", 
		value: "firstName"
	},
	{ 
		label: "Last Name", 
		value: "lastName"
	},
	{ 
		label: "Game Date", 
		value: "gameDate"
	},
	{ 
		label: "Player Team City", 
		value: "playerteamCity"
	},
	{ 
		label: "Player Team Name", 
		value: "playerteamName"
	},
	{ 
		label: "Opponent Team City", 
		value: "opponentteamCity"
	},
	{ 
		label: "Opponent Team Name", 
		value: "opponentteamName"
	},
	{ 
		label: "Game Type", 
		value: "gameType"
	},
	{ 
		label: "Game Label", 
		value: "gameLabel"
	},
	{ 
		label: "Game Sub Label", 
		value: "gameSubLabel"
	},
	{ 
		label: "Series Game Number", 
		value: "seriesGameNumber"
	},
	{ 
		label: "Team Won", 
		value: "win"
	},
	{ 
		label: "Home Game", 
		value: "home"
	},
	{ 
		label: "Minutes", 
		value: "mins"
	},
	{ 
		label: "Field Goals Made", 
		value: "fgm"
	},
	{ 
		label: "Field Goal Attempts", 
		value: "fga"
	},
	{ 
		label: " Field Goal %", 
		value: "fg_pct"
	},
	{ 
		label: "Thee Pointers Made", 
		value: "three_pm"
	},
	{ 
		label: "Thee Point Attempts", 
		value: "three_pa"
	},
	{ 
		label: "Thee Point %", 
		value: "three_pct"
	},
	{ 
		label: "Free Throws Made", 
		value: "ftm"
	},
	{ 
		label: "Free Throw Attempts", 
		value: "fta"
	},
	{ 
		label: "Free Throw %", 
		value: "ft_pct"
	},
	{ 
		label: "Offensive Rebounds", 
		value: "o_reb"
	},
	{ 
		label: "Defensive Rebounds", 
		value: "d_reb"
	},
	{ 
		label: "Rebounds", 
		value: "reb"
	},
	{ 
		label: "Assists", 
		value: "ast"
	},
	{ 
		label: "Steals", 
		value: "stl"
	},
	{ 
		label: "Blocks", 
		value: "blk"
	},
	{ 
		label: "Turnovers", 
		value: "turnover"
	},
	{ 
		label: "Personal Fouls", 
		value: "pf"
	},
	{ 
		label: "Points", 
		value: "pts"
	},
	{ 
		label: "Plus / Minus", 
		value: "plus_minus"
	}
]


export const queryBuilderSteps = [
    {
        step: "1",
        title: "What would you like to plot?",
        options: [
        	{ 
        		label: "Game Player Stats", 
        		value: "CHART player_stats"
        	}
        	// { 
        	// 	label: "Season Player Stats", 
        	// 	value: "CHART season_player_box_score"
        	// },
        	// { 
        	// 	label: "Game Team Stats", 
        	// 	value: "CHART game_team_box_score"
        	// },
        	// { 
        	// 	label: "Season Team Stats", 
        	// 	value: "CHART season_team_box_score"
        	// }
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
        stepType: "STAT_FIELD_STEP",
        title: "What stats would you like on each Axis?",
        options: chartableStatFields,
        queryPrefix: "FOR "
    },
    {
        step: "4",
        stepType: "WHERE_STEP",
        title: "Add any where conditions?",
        options: allStatFields
        //[
        //	{
        //		label: "Team is the Cleveland Cavaliers",
        //		value: "WHERE team_abbr = 'CLE'",
        //	}
        //]
    },
    {
        step: "5",
        title: "Your Query is Finshed!"
    },
];