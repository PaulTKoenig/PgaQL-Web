<script lang="ts">
  import { onMount } from 'svelte';
  import { Chart, Grid, NbaqlHeader, NbaqlSidebar, QueryBuilder, QueryNotebook } from '$lib';

  let submittedQuery = $state("");
  let queryTab = $state(0);

  const updateQueryTab = (updatedTab) => {
      queryTab=updatedTab;
  }

  let data = $state({});
  let error = $state(null);
  let loading = $state(false);
  let playerData = new Map();

  async function fetchPlayerData(playerIds) {
    let error = null;

    try {
      const response = await fetch("/api/get-player-details", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ player_ids: playerIds })
      });

      if (!response.ok) {
        throw new Error('Sorry something went wrong. Please try again');
      }

      const responseJson = await response.json();
      return responseJson;
    } catch (err) {
      error = err.message;
      console.error(error);
    }
  }

  async function loadPlayerData() {
    const playerIds = data.rowData.map(item => item[0]);
    // const players = fetchPlayerData(playerIds);
    const players = [
  {
    "firstName": "Jimmy",
    "lastName": "Butler",
    "playerId": "202710",
    "playerTeamCity": "Golden State",
    "playerTeamName": "Warriors"
  },
  {
    "firstName": "Shake",
    "lastName": "Milton",
    "playerId": "1629003",
    "playerTeamCity": "Los Angeles",
    "playerTeamName": "Lakers"
  },
  {
    "firstName": "Mike",
    "lastName": "Conley",
    "playerId": "201144",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Rudy",
    "lastName": "Gobert",
    "playerId": "203497",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Joe",
    "lastName": "Ingles",
    "playerId": "204060",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Donte",
    "lastName": "DiVincenzo",
    "playerId": "1628978",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Nickeil",
    "lastName": "Alexander-Walker",
    "playerId": "1629638",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Naz",
    "lastName": "Reid",
    "playerId": "1629675",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Anthony",
    "lastName": "Edwards",
    "playerId": "1630162",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Jaden",
    "lastName": "McDaniels",
    "playerId": "1630183",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Luka",
    "lastName": "Garza",
    "playerId": "1630568",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Leonard",
    "lastName": "Miller",
    "playerId": "1631159",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Josh",
    "lastName": "Minott",
    "playerId": "1631169",
    "playerTeamCity": "Minnesota",
    "playerTeamName": "Timberwolves"
  },
  {
    "firstName": "Alec",
    "lastName": "Burks",
    "playerId": "202692",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Kyle",
    "lastName": "Anderson",
    "playerId": "203937",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Bam",
    "lastName": "Adebayo",
    "playerId": "1628389",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Duncan",
    "lastName": "Robinson",
    "playerId": "1629130",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Kentavious",
    "lastName": "Caldwell-Pope",
    "playerId": "203484",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Gary",
    "lastName": "Harris",
    "playerId": "203914",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Marcus",
    "lastName": "Smart",
    "playerId": "203935",
    "playerTeamCity": "Washington",
    "playerTeamName": "Wizards"
  },
  {
    "firstName": "Malcolm",
    "lastName": "Brogdon",
    "playerId": "1627763",
    "playerTeamCity": "Washington",
    "playerTeamName": "Wizards"
  },
  {
    "firstName": "Jonathan",
    "lastName": "Isaac",
    "playerId": "1628371",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Wendell",
    "lastName": "Carter Jr.",
    "playerId": "1628976",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "ga",
    "lastName": "Bitadze",
    "playerId": "1629048",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Cole",
    "lastName": "Anthony",
    "playerId": "1630175",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Franz",
    "lastName": "Wagner",
    "playerId": "1630532",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Paolo",
    "lastName": "Banchero",
    "playerId": "1631094",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Caleb",
    "lastName": "Houstan",
    "playerId": "1631216",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Anthony",
    "lastName": "Black",
    "playerId": "1641710",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Jett",
    "lastName": "Howard",
    "playerId": "1641724",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Isaiah",
    "lastName": "Hartenstein",
    "playerId": "1628392",
    "playerTeamCity": "Oklahoma City",
    "playerTeamName": "Thunder"
  },
  {
    "firstName": "DeAndre",
    "lastName": "Jordan",
    "playerId": "201599",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Jordan",
    "lastName": "McLaughlin",
    "playerId": "1629162",
    "playerTeamCity": "San Antonio",
    "playerTeamName": "Spurs"
  },
  {
    "firstName": "Jalen",
    "lastName": "Pickett",
    "playerId": "1629618",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Zeke",
    "lastName": "Nnaji",
    "playerId": "1630192",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Peyton",
    "lastName": "Watson",
    "playerId": "1631212",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Hunter",
    "lastName": "Tyson",
    "playerId": "1641816",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Caris",
    "lastName": "LeVert",
    "playerId": "1627747",
    "playerTeamCity": "Atlanta",
    "playerTeamName": "Hawks"
  },
  {
    "firstName": "Georges",
    "lastName": "Niang",
    "playerId": "1627777",
    "playerTeamCity": "Atlanta",
    "playerTeamName": "Hawks"
  },
  {
    "firstName": "Caleb",
    "lastName": "Martin",
    "playerId": "1628997",
    "playerTeamCity": "Dallas",
    "playerTeamName": "Mavericks"
  },
  {
    "firstName": "Jaylen",
    "lastName": "Brown",
    "playerId": "1627759",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  },
  {
    "firstName": "Jayson",
    "lastName": "Tatum",
    "playerId": "1628369",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  },
  {
    "firstName": "Derrick",
    "lastName": "White",
    "playerId": "1628401",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  },
  {
    "firstName": "Luke",
    "lastName": "Kornet",
    "playerId": "1628436",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  },
  {
    "firstName": "Tristan",
    "lastName": "Thompson",
    "playerId": "202684",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Karl-Anthony",
    "lastName": "Towns",
    "playerId": "1626157",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Donovan",
    "lastName": "Mitchell",
    "playerId": "1628378",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "OG",
    "lastName": "Anunoby",
    "playerId": "1628384",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Jarrett",
    "lastName": "Allen",
    "playerId": "1628386",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Josh",
    "lastName": "Hart",
    "playerId": "1628404",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Max",
    "lastName": "Strus",
    "playerId": "1629622",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Darius",
    "lastName": "Garland",
    "playerId": "1629636",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Isaac",
    "lastName": "Okoro",
    "playerId": "1630171",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Precious",
    "lastName": "Achiuwa",
    "playerId": "1630173",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Sam",
    "lastName": "Merrill",
    "playerId": "1630241",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Evan",
    "lastName": "Mobley",
    "playerId": "1630596",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "James",
    "lastName": "Johnson",
    "playerId": "201949",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "T.J.",
    "lastName": "McConnell",
    "playerId": "204456",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Myles",
    "lastName": "Turner",
    "playerId": "1626167",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Pascal",
    "lastName": "Siakam",
    "playerId": "1627783",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "DaQuan",
    "lastName": "Jeffries",
    "playerId": "1629610",
    "playerTeamCity": "Charlotte",
    "playerTeamName": "Hornets"
  },
  {
    "firstName": "Andrew",
    "lastName": "Nembhard",
    "playerId": "1629614",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Obi",
    "lastName": "Toppin",
    "playerId": "1630167",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Tyrese",
    "lastName": "Haliburton",
    "playerId": "1630169",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Aaron",
    "lastName": "Nesmith",
    "playerId": "1630174",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Jarace",
    "lastName": "Walker",
    "playerId": "1641716",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Ben",
    "lastName": "Sheppard",
    "playerId": "1641767",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Doug",
    "lastName": "McDermott",
    "playerId": "203926",
    "playerTeamCity": "Sacramento",
    "playerTeamName": "Kings"
  },
  {
    "firstName": "Markelle",
    "lastName": "Fultz",
    "playerId": "1628365",
    "playerTeamCity": "Sacramento",
    "playerTeamName": "Kings"
  },
  {
    "firstName": "Aaron",
    "lastName": "Gordon",
    "playerId": "203932",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Nikola",
    "lastName": "Jokic",
    "playerId": "203999",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Christian",
    "lastName": "Braun",
    "playerId": "1631128",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Jalen",
    "lastName": "Smith",
    "playerId": "1630188",
    "playerTeamCity": "Chicago",
    "playerTeamName": "Bulls"
  },
  {
    "firstName": "Kyle",
    "lastName": "Lowry",
    "playerId": "200768",
    "playerTeamCity": "Philadelphia",
    "playerTeamName": "76ers"
  },
  {
    "firstName": "Monte",
    "lastName": "Morris",
    "playerId": "1628420",
    "playerTeamCity": "Phoenix",
    "playerTeamName": "Suns"
  },
  {
    "firstName": "Al",
    "lastName": "Horford",
    "playerId": "201143",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  },
  {
    "firstName": "Wendell",
    "lastName": "Moore Jr.",
    "playerId": "1631111",
    "playerTeamCity": "Charlotte",
    "playerTeamName": "Hornets"
  },
  {
    "firstName": "Miles",
    "lastName": "McBride",
    "playerId": "1630540",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Michael",
    "lastName": "Porter Jr.",
    "playerId": "1629008",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Kevin",
    "lastName": "Love",
    "playerId": "201567",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Jamal",
    "lastName": "Murray",
    "playerId": "1627750",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Robert",
    "lastName": "Williams III",
    "playerId": "1629057",
    "playerTeamCity": "Portland",
    "playerTeamName": "Trail Blazers"
  },
  {
    "firstName": "Jalen",
    "lastName": "Brunson",
    "playerId": "1628973",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Moritz",
    "lastName": "Wagner",
    "playerId": "1629021",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Jalen",
    "lastName": "Suggs",
    "playerId": "1630591",
    "playerTeamCity": "Orlando",
    "playerTeamName": "Magic"
  },
  {
    "firstName": "Chuma",
    "lastName": "Okeke",
    "playerId": "1629643",
    "playerTeamCity": "Philadelphia",
    "playerTeamName": "76ers"
  },
  {
    "firstName": "Jericho",
    "lastName": "Sims",
    "playerId": "1630579",
    "playerTeamCity": "Milwaukee",
    "playerTeamName": "Bucks"
  },
  {
    "firstName": "Julian",
    "lastName": "Strawther",
    "playerId": "1631124",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Isaiah",
    "lastName": "Jackson",
    "playerId": "1630543",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Reggie",
    "lastName": "Jackson",
    "playerId": "202704",
    "playerTeamCity": "Philadelphia",
    "playerTeamName": "76ers"
  },
  {
    "firstName": "T.J.",
    "lastName": "Warren",
    "playerId": "203933",
    "playerTeamCity": "New York",
    "playerTeamName": "Knicks"
  },
  {
    "firstName": "Cody",
    "lastName": "Zeller",
    "playerId": "203469",
    "playerTeamCity": "Atlanta",
    "playerTeamName": "Hawks"
  },
  {
    "firstName": "Kendall",
    "lastName": "Brown",
    "playerId": "1631112",
    "playerTeamCity": "Indiana",
    "playerTeamName": "Pacers"
  },
  {
    "firstName": "Mamadi",
    "lastName": "Diakite",
    "playerId": "1629603",
    "playerTeamCity": "Phoenix",
    "playerTeamName": "Suns"
  },
  {
    "firstName": "Justin",
    "lastName": "Holiday",
    "playerId": "203200",
    "playerTeamCity": "Denver",
    "playerTeamName": "Nuggets"
  },
  {
    "firstName": "Mike",
    "lastName": "Muscala",
    "playerId": "203488",
    "playerTeamCity": "Oklahoma City",
    "playerTeamName": "Thunder"
  },
  {
    "firstName": "Marcus",
    "lastName": "Morris Sr.",
    "playerId": "202694",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Damian",
    "lastName": "Jones",
    "playerId": "1627745",
    "playerTeamCity": "Cleveland",
    "playerTeamName": "Cavaliers"
  },
  {
    "firstName": "Udonis",
    "lastName": "Haslem",
    "playerId": "2617",
    "playerTeamCity": "Miami",
    "playerTeamName": "Heat"
  },
  {
    "firstName": "Blake",
    "lastName": "Griffin",
    "playerId": "201933",
    "playerTeamCity": "Boston",
    "playerTeamName": "Celtics"
  }
];

    playerData = new Map((await players).map(player => [player.playerId, `${player.firstName} ${player.lastName}`]));
  }

  async function fetchData(e) {
    loading = true;
    error = null;
    let input = e.detail.input;

    try {
      // const encodedQuery = encodeURIComponent(input);
      // const response = await fetch(`/api/interpret-query?query=${encodedQuery}`);
      
      // if (!response.ok) {
      //   if (response.status === 400) {
      //     throw new Error('Invalid grammar');
      //   } else {
      //     throw new Error('Sorry something went wrong. Please try again');
      //   }
      // }

      // data = await response.json();
      data = {
  "rowData": [
    [
      "201144",
      38.0,
      10.0
    ],
    [
      "201599",
      "",
      0.0
    ],
    [
      "202704",
      5.0,
      0.0
    ],
    [
      "203200",
      9.0,
      0.0
    ],
    [
      "203484",
      39.0,
      5.0
    ],
    [
      "203497",
      35.0,
      13.0
    ],
    [
      "203932",
      42.0,
      4.0
    ],
    [
      "203933",
      "",
      0.0
    ],
    [
      "203937",
      4.0,
      2.0
    ],
    [
      "203999",
      46.0,
      34.0
    ],
    [
      "1626157",
      39.0,
      23.0
    ],
    [
      "1627750",
      42.0,
      35.0
    ],
    [
      "1628420",
      "",
      0.0
    ],
    [
      "1629008",
      34.0,
      7.0
    ],
    [
      "1629162",
      "",
      0.0
    ],
    [
      "1629618",
      "",
      0.0
    ],
    [
      "1629638",
      17.0,
      0.0
    ],
    [
      "1629675",
      21.0,
      11.0
    ],
    [
      "1630162",
      43.0,
      16.0
    ],
    [
      "1630183",
      39.0,
      23.0
    ],
    [
      "1630192",
      "",
      0.0
    ],
    [
      "1630568",
      "",
      0.0
    ],
    [
      "1631111",
      "",
      0.0
    ],
    [
      "1631124",
      "",
      0.0
    ],
    [
      "1631128",
      19.0,
      5.0
    ],
    [
      "1631159",
      "",
      0.0
    ],
    [
      "1631169",
      "",
      0.0
    ],
    [
      "1631212",
      "",
      0.0
    ],
    [
      "1641816",
      "",
      0.0
    ],
    [
      "201949",
      "",
      0.0
    ],
    [
      "202692",
      27.0,
      26.0
    ],
    [
      "203926",
      "",
      0.0
    ],
    [
      "204456",
      23.0,
      12.0
    ],
    [
      "1626167",
      32.0,
      17.0
    ],
    [
      "1627783",
      36.0,
      20.0
    ],
    [
      "1628384",
      4.0,
      5.0
    ],
    [
      "1628392",
      29.0,
      0.0
    ],
    [
      "1628404",
      36.0,
      10.0
    ],
    [
      "1628973",
      29.0,
      17.0
    ],
    [
      "1628978",
      41.0,
      39.0
    ],
    [
      "1629003",
      0.0,
      0.0
    ],
    [
      "1629603",
      0.0,
      0.0
    ],
    [
      "1629610",
      0.0,
      0.0
    ],
    [
      "1629614",
      33.0,
      20.0
    ],
    [
      "1630167",
      15.0,
      3.0
    ],
    [
      "1630169",
      32.0,
      26.0
    ],
    [
      "1630173",
      27.0,
      4.0
    ],
    [
      "1630174",
      28.0,
      19.0
    ],
    [
      "1630188",
      "",
      0.0
    ],
    [
      "1630540",
      40.0,
      8.0
    ],
    [
      "1630543",
      10.0,
      9.0
    ],
    [
      "1630579",
      0.0,
      0.0
    ],
    [
      "1631112",
      0.0,
      0.0
    ],
    [
      "1641716",
      0.0,
      0.0
    ],
    [
      "1641767",
      24.0,
      4.0
    ],
    [
      "202684",
      6.0,
      0.0
    ],
    [
      "202694",
      7.0,
      0.0
    ],
    [
      "203914",
      27.0,
      6.0
    ],
    [
      "204060",
      5.0,
      0.0
    ],
    [
      "1627745",
      "",
      0.0
    ],
    [
      "1627747",
      29.0,
      15.0
    ],
    [
      "1627777",
      3.0,
      0.0
    ],
    [
      "1628365",
      13.0,
      8.0
    ],
    [
      "1628371",
      18.0,
      2.0
    ],
    [
      "1628378",
      45.0,
      39.0
    ],
    [
      "1628386",
      "",
      0.0
    ],
    [
      "1628976",
      34.0,
      13.0
    ],
    [
      "1629021",
      11.0,
      3.0
    ],
    [
      "1629048",
      "",
      0.0
    ],
    [
      "1629622",
      32.0,
      13.0
    ],
    [
      "1629636",
      30.0,
      12.0
    ],
    [
      "1629643",
      "",
      0.0
    ],
    [
      "1630171",
      33.0,
      8.0
    ],
    [
      "1630175",
      13.0,
      8.0
    ],
    [
      "1630241",
      11.0,
      8.0
    ],
    [
      "1630532",
      34.0,
      6.0
    ],
    [
      "1630591",
      39.0,
      10.0
    ],
    [
      "1630596",
      41.0,
      11.0
    ],
    [
      "1631094",
      41.0,
      38.0
    ],
    [
      "1631216",
      "",
      0.0
    ],
    [
      "1641710",
      "",
      0.0
    ],
    [
      "1641724",
      "",
      0.0
    ],
    [
      "2617",
      "",
      0.0
    ],
    [
      "200768",
      24.0,
      7.0
    ],
    [
      "201143",
      34.0,
      8.0
    ],
    [
      "201567",
      "",
      0.0
    ],
    [
      "201933",
      "",
      0.0
    ],
    [
      "202710",
      43.0,
      28.0
    ],
    [
      "203469",
      "",
      0.0
    ],
    [
      "203488",
      2.0,
      3.0
    ],
    [
      "203935",
      35.0,
      9.0
    ],
    [
      "1627759",
      43.0,
      19.0
    ],
    [
      "1627763",
      7.0,
      0.0
    ],
    [
      "1628369",
      41.0,
      14.0
    ],
    [
      "1628389",
      42.0,
      12.0
    ],
    [
      "1628401",
      36.0,
      18.0
    ],
    [
      "1628436",
      2.0,
      0.0
    ],
    [
      "1628997",
      44.0,
      26.0
    ],
    [
      "1629057",
      13.0,
      8.0
    ],
    [
      "1629130",
      20.0,
      10.0
    ]
  ],
  "x_column_name": "mins",
  "y_column_name": "pts"
};
      submittedQuery=input;

      await loadPlayerData();
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>


<NbaqlHeader />
<div class="lg:flex">
  <div class="w-full xl:w-1/3 2xl:w-1/4 mx-auto pb-10">
    <NbaqlSidebar />
  </div>

  <div class="flex flex-col gap-10 w-full lg:w-2/3 xl:w-3/4 mx-auto">
    <div class="nbaql-main-container">
      <div class="nbaql-tabs flex mb-10">
        <div class="nbaql-query-tab" class:nbaql-query-tab-active={queryTab === 0} onclick={() => updateQueryTab(0)}>
          Query Builder
        </div>
        <div 
          class="nbaql-query-tab" class:nbaql-query-tab-active={queryTab === 1} onclick={() => updateQueryTab(1)}
        >Query Notebook</div>
        <!-- <div 
          class="w-1/3 border-b hover:shadow-lg focus:shadow-lg cursor-pointer p-3 transition-all"
        >NL Search</div> -->
      </div>

      <div class="p-5">
        {#if queryTab === 0}
          <QueryBuilder on:submit={fetchData} />
        {:else if queryTab === 1}
          <QueryNotebook on:submit={fetchData} />
        {:else}
          ah shit
        {/if}
        
      </div>
    </div>

    <div class="nbaql-chart-container mx-auto" class:hidden={!loading && !error && (!("rowData" in data) || data.rowData?.length === 0)}>
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.rowData?.length > 0}
      <div>
        <Chart {data} {playerData} />
      </div>
      {/if}
    </div>

    <div class="nbaql-grid-container mx-auto" class:hidden={error || (!loading && (!("rowData" in data) || data.rowData?.length === 0))}>
      {#if loading}
        <p>Loading...</p>
      {:else if error}
        <p><b>Error:</b> {error}</p>
      {:else if data.rowData?.length > 0}
      <div>
        <Grid {data} {playerData} />
      </div>
      {/if}
    </div>
  </div>
</div>

<style>

    .nbaql-main-container, .nbaql-menu-container, .nbaql-chart-container, .nbaql-grid-container {
      padding: 2rem;
      margin: 0 1rem;
      border-radius: 16px;
      background-color: #333333;
    }

    @media (max-width: 600px) {
        .nbaql-chart-container {
          padding: 1rem 1.5rem 1rem 0.5rem;
        }
    }

    .pt-nav {
        padding-top: max(3.5rem, 10vh);
    }

    .nbaql-tabs {
      border: 1px solid #222222;
      border-radius: 4px;
    }

    .nbaql-query-tab {
      width: 50%;
      cursor: pointer;
      padding: 0.75rem;
      display: flex;
      justify-content: center;
      border-radius: 4px;
    }

    .nbaql-query-tab:hover {
      text-decoration: underline;
    }

    .nbaql-query-tab-active {
      transition-property: all;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
      transition-duration: 150ms;

      --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 1);
      box-shadow: var(--tw-ring-offset-shadow, 0 0 #fff), var(--tw-ring-shadow, 0 0 #fff), var(--tw-shadow);
    }
    .nbaql-query-tab-active:hover {
      border: initial;
    }
</style>