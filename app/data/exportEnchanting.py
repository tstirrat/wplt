#!/usr/bin/env python3.7

recipes = {
	"2H Weapon - Agility": {
        "ID":       27837,
        "Learn":    290,
        "Yellow":   310,
        "Green":    330,
        "Grey":     350,
        "Source":   "Reputation",
        "Reagents": {
            "Large Brilliant Shard": 10,
            "Greater Eternal Essence": 6,
			"Illusion Dust": 14,
			"Essence of Air": 4
        }
    },
    "2H Weapon - Greater Impact": {
        "ID":       13937,
        "Learn":    240,
        "Yellow":   260,
        "Green":    280,
        "Grey":     300,
        "Source":   "Trainer",
        "Reagents": {
			"Large Radiant Shard": 2,
			"Dream Dust": 2
        }
    },
    "2H Weapon - Impact": {
        "ID":       13695,
        "Learn":    200,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Vision Dust": 4,
			"Large Glowing Shard": 1
        }
    },
    "2H Weapon - Lesser Impact": {
        "ID":       13529,
        "Learn":    145,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 3,
			"Large Glimmering Shard": 1
        }
    },
    "2H Weapon - Lesser Intellect": {
        "ID":       7793,
        "Learn":    100,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Reagents": {
			"Greater Magic Essence": 3
        }
    },
    "2H Weapon - Lesser Spirit": {
        "ID":       13380,
        "Learn":    110,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Drop",
        "RecipeID": 11167,
        "Reagents": {
			"Lesser Astral Essence": 1,
			"Strange Dust": 6
        }
    },
    "2H Weapon - Minor Impact": {
        "ID":       7745,
        "Learn":    100,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 4,
			"Small Glimmering Shard": 1
        }
    },
    "2H Weapon - Superior Impact": {
        "ID":       20030,
        "Learn":    295,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Drop",
        "RecipeID": 16247,
        "Reagents": {
			"Large Brilliant Shard": 4,
			"Illusion Dust": 10
        }
    },
    "Boots - Agility": {
        "ID":       13935,
        "Learn":    235,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Nether Essence": 2
        }
    },
    "Boots - Greater Agility": {
        "ID":       20023,
        "Learn":    295,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Drop",
        "RecipeID": 16245,
        "Reagents": {
			"Greater Eternal Essence": 8
        }
    },
    "Boots - Greater Stamina": {
        "ID":       20020,
        "Learn":    260,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 16215,
        "Reagents": {
			"Dream Dust": 10
        }
    },
    "Boots - Lesser Agility": {
        "ID":       13639,
        "Learn":    160,
        "Yellow":   180,
        "Green":    200,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 1,
			"Lesser Mystic Essence": 1
        }
    },
    "Boots - Lesser Spirit": {
        "ID":       13687,
        "Learn":    190,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 11167,
        "Reagents": {
			"Greater Mystic Essence": 1,
			"Lesser Mystic Essence": 2
        }
    },
    "Boots - Lesser Stamina": {
        "ID":       13644,
        "Learn":    170,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 4
        }
    },
    "Boots - Minor Agility": {
        "ID":       7867,
        "Learn":    125,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "Reagents": {
			"Strange Dust": 6,
			"Lesser Astral Essence": 2
        }
    },
    "Boots - Minor Speed": {
        "ID":       13890,
        "Learn":    225,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Small Radiant Shard": 1,
			"Aquamarine": 1,
			"Lesser Nether Essence": 1
        }
    },
    "Boots - Minor Stamina": {
        "ID":       7863,
        "Learn":    125,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 8
        }
    },
    "Boots - Spirit": {
        "ID":       20024,
        "Learn":    275,
        "Yellow":   295,
        "Green":    315,
        "Grey":     335,
        "Source":   "Drop",
        "RecipeID": 16220,
        "Reagents": {
			"Greater Eternal Essence": 2,
			"Lesser Eternal Essence": 1
        }
    },
    "Boots - Stamina": {
        "ID":       13836,
        "Learn":    215,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
			"Vision Dust": 5
        }
    },
    "Bracer - Deflection": {
        "ID":       13931,
        "Learn":    235,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Vendor",
        "Reagents": {
			"Greater Nether Essence": 1,
			"Dream Dust": 2
        }
    },
    "Bracer - Greater Intellect": {
        "ID":       20008,
        "Learn":    255,
        "Yellow":   275,
        "Green":    295,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 16214,
        "Reagents": {
			"Lesser Eternal Essence": 3
        }
    },
    "Bracer - Greater Spirit": {
        "ID":       13846,
        "Learn":    220,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Drop",
        "RecipeID": 11204,
        "Reagents": {
			"Lesser Nether Essence": 3,
			"Vision Dust": 1
        }
    },
    "Bracer - Greater Stamina": {
        "ID":       13945,
        "Learn":    245,
        "Yellow":   165,
        "Green":    285,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 11225,
        "Reagents": {
			"Dream Dust": 5
        }
    },
    "Bracer - Greater Strength": {
        "ID":       13939,
        "Learn":    240,
        "Yellow":   260,
        "Green":    280,
        "Grey":     300,
        "Source":   "Trainer",
        "Reagents": {
			"Dream Dust": 2,
			"Greater Nether Essence": 1
        }
    },
    "Bracer - Intellect": {
        "ID":       13822,
        "Learn":    210,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Nether Essence": 2
        }
    },
    "Bracer - Lesser Deflection": {
        "ID":       13646,
        "Learn":    170,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Vendor",
        "Reagents": {
			"Lesser Mystic Essence": 1,
			"Soul Dust": 2
        }
    },
    "Bracer - Lesser Intellect": {
        "ID":       13622,
        "Learn":    150,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Astral Essence": 2
        }
    },
    "Bracer - Lesser Spirit": {
        "ID":       7859,
        "Learn":    120,
        "Yellow":   145,
        "Green":    165,
        "Grey":     185,
        "Source":   "Drop",
        "RecipeID": 6375,
        "Reagents": {
			"Lesser Astral Essence": 2
        }
    },
    "Bracer - Lesser Stamina": {
        "ID":       13501,
        "Learn":    130,
        "Yellow":   155,
        "Green":    175,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 2
        }
    },
    "Bracer - Lesser Strength": {
        "ID":       13536,
        "Learn":    140,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Vendor",
        "Reagents": {
			"Soul Dust": 2
        }
    },
    "Bracer - Mana Regeneration": {
        "ID":       23801,
        "Learn":    290,
        "Yellow":   310,
        "Green":    330,
        "Grey":     350,
        "Source":   "Reputation",
        "Reagents": {
			"Illusion Dust": 16,
			"Greater Eternal Essence": 4,
			"Essence of Water": 2
        }
    },
    "Bracer - Minor Agility": {
        "ID":       7779,
        "Learn":    80,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 2,
			"Greater Magic Essence": 1
        }
    },
    "Bracer - Minor Deflect": {
        "ID":       7428,
        "Learn":    1,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Magic Essence": 1,
			"Strange Dust": 1
        }
    },
    "Bracer - Minor Health": {
        "ID":       7418,
        "Learn":    1,
        "Yellow":   70,
        "Green":    90,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 1
        }
    },
    "Bracer - Minor Spirit": {
        "ID":       7766,
        "Learn":    60,
        "Yellow":   105,
        "Green":    125,
        "Grey":     145,
        "Source":   "Drop",
        "RecipeID": 6344,
        "Reagents": {
			"Lesser Magic Essence": 2
        }
    },
    "Bracer - Minor Stamina": {
        "ID":       7457,
        "Learn":    50,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 3
        }
    },
    "Bracer - Minor Strength": {
        "ID":       7782,
        "Learn":    80,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Drop",
        "RecipeID": 6347,
        "Reagents": {
			"Strange Dust": 5
        }
    },
    "Bracer - Spirit": {
        "ID":       13642,
        "Learn":    165,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Mystic Essence": 1
        }
    },
    "Bracer - Stamina": {
        "ID":       13648,
        "Learn":    170,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 6
        }
    },
    "Bracer - Strength": {
        "ID":       13661,
        "Learn":    180,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Vision Dust": 1
        }
    },
    "Bracer - Superior Spirit": {
        "ID":       20009,
        "Learn":    270,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 16218,
        "Reagents": {
			"Lesser Eternal Essence": 3,
			"Dream Dust": 10
        }
    },
    "Bracer - Superior Strength": {
        "ID":       20010,
        "Learn":    295,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Drop",
        "RecipeID": 16246,
        "Reagents": {
			"Illusion Dust":  6,
			"Greater Eternal Essence": 6
        }
    },
    "Brilliant Mana Oil": {
        "ID":       20748,
        "Learn":    300,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "Reagents": {
			"Large Brilliant Shard": 2,
            "Purple Lotus": 3,
            "Imbued Vial": 1
        }
    },
    "Brilliant Wizard Oil": {
        "ID":       20749,
        "Learn":    300,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "Reagents": {
			"Large Brilliant Shard": 2,
            "Firebloom": 3,
            "Imbued Vial": 1
        }
    },
    "Chest - Greater Health": {
        "ID":       13640,
        "Learn":    160,
        "Yellow":   180,
        "Green":    200,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 3
        }
    },
    "Chest - Greater Health": {
        "ID":       13640,
        "Learn":    160,
        "Yellow":   180,
        "Green":    200,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 3
        }
    },
    "Chest - Greater Mana": {
        "ID":       13663,
        "Learn":    185,
        "Yellow":   205,
        "Green":    225,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Mystic Essence": 1
        }
    },
    "Chest - Health": {
        "ID":       7857,
        "Learn":    120,
        "Yellow":   145,
        "Green":    165,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 4,
			"Lesser Astral Essence": 1
        }
    },
    "Chest - Lesser Absorption": {
        "ID":       13538,
        "Learn":    140,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 2,
			"Greater Astral Essence": 1,
			"Large Glimmering Shard": 1
        }
    },
    "Chest - Lesser Health": {
        "ID":       7748,
        "Learn":    60,
        "Yellow":   105,
        "Green":    125,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 2,
			"Lesser Magic Essence": 2
        }
    },
    "Chest - Lesser Mana": {
        "ID":       7776,
        "Learn":    80,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Vendor",
        "Reagents": {
			"Greater Magic Essence": 1,
			"Lesser Magic Essence": 1
        }
    },
    "Chest - Lesser Stats": {
        "ID":       13700,
        "Learn":    200,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Mystic Essence": 2,
			"Vision Dust": 2,
			"Large Glowing Shard": 1
        }
    },
    "Chest - Major Health": {
        "ID":       20026,
        "Learn":    275,
        "Yellow":   295,
        "Green":    315,
        "Grey":     335,
        "Source":   "Vendor",
        "Reagents": {
			"Illusion Dust": 6,
			"Small Brilliant Shard": 1
        }
    },
    "Chest - Major Mana": {
        "ID":       20028,
        "Learn":    290,
        "Yellow":   310,
        "Green":    330,
        "Grey":     350,
        "Source":   "Drop",
        "RecipeID": 16242,
        "Reagents": {
			"Greater Eternal Essence": 3,
			"Small Brilliant Shard": 1
        }
    },
    "Chest - Mana": {
        "ID":       13607,
        "Learn":    145,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Astral Essence": 1,
			"Lesser Astral Essence": 2
        }
    },
    "Chest - Minor Absorption": {
        "ID":       7426,
        "Learn":    40,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 2,
			"Lesser Magic Essence": 1
        }
    },
    "Chest - Minor Health": {
        "ID":       7420,
        "Learn":    15,
        "Yellow":   70,
        "Green":    90,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 1
        }
    },
    "Chest - Minor Mana": {
        "ID":       7443,
        "Learn":    20,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Vendor",
        "Reagents": {
			"Lesser Magic Essence": 1
        }
    },
    "Chest - Minor Stats": {
        "ID":       13626,
        "Learn":    150,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Astral Essence": 1,
			"Soul Dust": 1,
			"Large Glimmering Shard": 1
        }
    },
    "Chest - Stats": {
        "ID":       13941,
        "Learn":    245,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Trainer",
        "Reagents": {
			"Large Radiant Shard": 1,
			"Dream Dust": 3,
			"Greater Nether Essence": 2
        }
    },
    "Chest - Superior Health": {
        "ID":       13858,
        "Learn":    220,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
			"Vision Dust": 6
        }
    },
    "Chest - Superior Mana": {
        "ID":       13917,
        "Learn":    230,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Nether Essence": 1,
			"Lesser Nether Essence": 2
        }
    },
    "Cloak - Defense": {
        "ID":       13635,
        "Learn":    155,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Small Glowing Shard": 1,
			"Soul Dust": 3
        }
    },
    "Cloak - Fire Resistance": {
        "ID":       13657,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Mystic Essence": 1,
			"Elemental Fire": 1
        }
    },
    "Cloak - Greater Defense": {
        "ID":       13746,
        "Learn":    205,
        "Yellow":   225,
        "Green":    245,
        "Grey":     265,
        "Source":   "Trainer",
        "Reagents": {
			"Vision Dust": 3
        }
    },
    "Cloak - Greater Resistance": {
        "ID":       20014,
        "Learn":    265,
        "Yellow":   285,
        "Green":    305,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 16216,
        "Reagents": {
			"Lesser Eternal Essence": 2,
			"Heart of Fire": 1,
			"Core of Earth": 1,
			"Globe of Water": 1,
			"Breath of Wind": 1,
			"Ichor of Undeath": 1
        }
    },
    "Cloak - Lesser Agility": {
        "ID":       13882,
        "Learn":    225,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Drop",
        "RecipeID": 11206,
        "Reagents": {
			"Lesser Nether Essence": 2
        }
    },
    "Cloak - Lesser Fire Resistance": {
        "ID":       7861,
        "Learn":    125,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Fire Oil": 1,
			"Lesser Astral Essence": 1
        }
    },
    "Cloak - Lesser Protection": {
        "ID":       13421,
        "Learn":    115,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 6,
			"Small Glimmering Shard": 1
        }
    },
    "Cloak - Lesser Shadow Resistance": {
        "ID":       13522,
        "Learn":    135,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Drop",
        "RecipeID": 11098,
        "Reagents": {
			"Greater Astral Essence": 1,
			"Shadow Protection Potion": 1
        }
    },
    "Cloak - Minor Agility": {
        "ID":       13419,
        "Learn":    110,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Lesser Astral Essence": 1
        }
    },
    "Cloak - Minor Protection": {
        "ID":       7771,
        "Learn":    70,
        "Yellow":   110,
        "Green":    130,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 3,
			"Greater Magic Essence": 1
        }
    },
    "Cloak - Minor Resistance": {
        "ID":       7454,
        "Learn":    45,
        "Yellow":   95,
        "Green":    115,
        "Grey":     135,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 1,
			"Lesser Magic Essence": 2
        }
    },
    "Cloak - Resistance": {
        "ID":       13794,
        "Learn":    205,
        "Yellow":   225,
        "Green":    245,
        "Grey":     265,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Nether Essence": 1
        }
    },
    "Cloak - Superior Defense": {
        "ID":       20015,
        "Learn":    285,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Vendor",
        "Reagents": {
			"Illusion Dust": 8
        }
    },
    "Gloves - Advanced Herbalism": {
        "ID":       13868,
        "Learn":    225,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Drop",
        "RecipeID": 11205,
        "Reagents": {
			"Vision Dust": 3,
			"Sungrass": 3
        }
    },
    "Gloves - Advanded Mining": {
        "ID":       13841,
        "Learn":    215,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 11203,
        "Reagents": {
			"Vision Dust": 3,
			"Truesilver Bar": 3
        }
    },
    "Glvoes - Agility": {
        "ID":       13815,
        "Learn":    210,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Nether Essence": 1,
			"Vision Dust": 1
        }
    },
    "Gloves - Fishing": {
        "ID":       13620,
        "Learn":    145,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 11152,
        "Reagents": {
			"Soul Dust": 1,
			"Blackmouth Oil": 3
        }
    },
    "Gloves - Greater Agility": {
        "ID":       20012,
        "Learn":    270,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 16219,
        "Reagents": {
			"Lesser Eternal Essence": 3,
			"Illusion Dust": 3
        }
    },
    "Gloves - Greater Strength": {
        "ID":       20013,
        "Learn":    295,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Drop",
        "RecipeID": 16244,
        "Reagents": {
			"Greater Eternal Essence": 4,
			"Illusion Dust": 4
        }
    },
    "Gloves - Herbalism": {
        "ID":       13617,
        "Learn":    145,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 11151,
        "Reagents": {
			"Soul Dust": 1,
			"Kingsblood": 3
        }
    },
    "Gloves - Mining": {
        "ID":       13612,
        "Learn":    145,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 11150,
        "Reagents": {
			"Soul Dust": 1,
			"Iron Ore": 3
        }
    },
    "Gloves - Minor Haste": {
        "ID":       13948,
        "Learn":    250,
        "Yellow":   270,
        "Green":    290,
        "Grey":     310,
        "Source":   "Trainer",
        "Reagents": {
			"Large Radiant Shard": 2,
			"Wildvine": 2
        }
    },
    "Gloves - Riding Skill": {
        "ID":       13947,
        "Learn":    250,
        "Yellow":   270,
        "Green":    290,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 11226,
        "Reagents": {
			"Large Radiant Shard": 2,
			"Dream Dust": 3
        }
    },
    "Gloves - Skinning": {
        "ID":       13698,
        "Learn":    200,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 11166,
        "Reagents": {
			"Vision Dust": 1,
			"Green Whelp Scale": 3
        }
    },
    "Gloves - Strength": {
        "ID":       13887,
        "Learn":    225,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Nether Essence": 2,
			"Vision Dust": 3
        }
    },
    "Shield - Frost Resistance": {
        "ID":       13933,
        "Learn":    235,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Drop",
        "RecipeID": 11224,
        "Reagents": {
			"Large Radiant Shard": 1,
			"Frost Oil": 1
        }
    },
    "Shield - Greater Spirit": {
        "ID":       13905,
        "Learn":    230,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Nether Essence": 1,
			"Dream Dust": 2
        }
    },
    "Shield - Greater Stamina": {
        "ID":       20017,
        "Learn":    265,
        "Yellow":   285,
        "Green":    305,
        "Grey":     325,
        "Source":   "Vendor",
        "Reagents": {
			"Dream Dust": 10
        }
    },
    "Shield - Lesser Block": {
        "ID":       13689,
        "Learn":    195,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Drop",
        "RecipeID": 11168,
        "Reagents": {
			"Greater Mystic Essence": 2,
			"Vision Dust": 2,
			"Large Glowing Shard": 1
        }
    },
    "Shield - Lesser Protection": {
        "ID":       13464,
        "Learn":    115,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Drop",
        "RecipeID": 11081,
        "Reagents": {
			"Lesser Astral Essence": 1,
			"Strange Dust": 1,
			"Small Glimmering Shard": 1
        }
    },
    "Shield - Lesser Spirit": {
        "ID":       13485,
        "Learn":    130,
        "Yellow":   155,
        "Green":    175,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Astral Essence": 2,
			"Strange Dust": 4
        }
    },
    "Shield - Lesser Stamina": {
        "ID":       13631,
        "Learn":    155,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Mystic Essence": 1,
			"Soul Dust": 1
        }
    },
    "Shield - Minor Stamina": {
        "ID":       13378,
        "Learn":    105,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Lesser Astral Essence": 1,
			"Strange Dust": 2
        }
    },
    "Shield - Spirit": {
        "ID":       13659,
        "Learn":    180,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Mystic Essence": 1,
			"Vision Dust": 1
        }
    },
    "Shield - Stamina": {
        "ID":       13817,
        "Learn":    210,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Drop",
        "Reagents": {
			"Vision Dust": 5
        }
    },
    "Shield - Superior Spirit": {
        "ID":       20016,
        "Learn":    280,
        "Yellow":   300,
        "Green":    320,
        "Grey":     340,
        "Source":   "Drop",
        "RecipeID": 16222,
        "Reagents": {
			"Greater Eternal Essence": 2,
			"Illusion Dust": 4
        }
    },
    "Weapon - Agility": {
        "ID":       23800,
        "Learn":    290,
        "Yellow":   310,
        "Green":    330,
        "Grey":     350,
        "Source":   "Reputation",
        "Reagents": {
			"Large Brilliant Shard": 6,
			"Greater Eternal Essence": 6,
			"Illusion Dust": 4,
			"Essence of Air": 2
        }
    },
    "Weapon - Demonslaying": {
        "ID":       13915,
        "Learn":    230,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Drop",
        "RecipeID": 11208,
        "Reagents": {
			"Small Radiant Shard": 1,
			"Dream Dust": 2,
			"Elixir of Demonslaying": 1
        }
    },
    "Weapon - Fiery Weapon": {
        "ID":       13898,
        "Learn":    265,
        "Yellow":   285,
        "Green":    305,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 11207,
        "Reagents": {
			"Small Radiant Shard": 4,
			"Essence of Fire": 1
        }
    },
    "Weapon - Greater Striking": {
        "ID":       13943,
        "Learn":    245,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Trainer",
        "Reagents": {
			"Large Radiant Shard": 2,
			"Greater Nether Essence": 2
        }
    },
    "Weapon - Icy Chill": {
        "ID":       20029,
        "Learn":    285,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "RecipeID": 16223,
        "Reagents": {
			"Small Brilliant Shard": 4,
			"Essence of Water": 1,
			"Essence of Air": 1,
			"Icecap": 1
        }
    },
    "Weapon - Lesser Beastslaying": {
        "ID":       13653,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Drop",
        "RecipeID": 11164,
        "Reagents": {
			"Lesser Mystic Essence": 1,
			"Large Fang": 2,
			"Small Glowing Shard": 1
        }
    },
    "Weapon - Lesser Elemental Slayer": {
        "ID":       13655,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Drop",
        "RecipeID": 11165,
        "Reagents": {
			"Lesser Mystic Essence": 1,
			"Elemental Earth": 1,
			"Small Glowing Shard": 1
        }
    },
    "Weapon - Lesser Striking": {
        "ID":       13503,
        "Learn":    140,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
			"Soul Dust": 2,
			"Large Glimmering Shard": 1
        }
    },
    "Weapon - Minor Beastslayer": {
        "ID":       7786,
        "Learn":    90,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Drop",
        "RecipeID": 6348,
        "Reagents": {
			"Strange Dust": 4,
			"Greater Magic Essence": 2
        }
    },
    "Weapon - Minor Striking": {
        "ID":       7788,
        "Learn":    90,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Strange Dust": 2,
			"Greater Magic Essence": 1,
			"Small Glimmering Shard": 1
        }
    },
    "Weapon - Strength": {
        "ID":       23799,
        "Learn":    290,
        "Yellow":   310,
        "Green":    330,
        "Grey":     350,
        "Source":   "Reputation",
        "Reagents": {
			"Large Brilliant Shard": 6,
			"Greater Eternal Essence": 6,
			"Illusion Dust": 4,
			"Essence of Earth": 2
        }
    },
    "Weapon - Striking": {
        "ID":       13693,
        "Learn":    195,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
			"Greater Mystic Essence": 2,
			"Large Glowing Shard": 1
        }
    },
    "Weapon - Unholy Weapon": {
        "ID":       20033,
        "Learn":    295,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Drop",
        "RecipeID": 16248,
		"Reagents": {
			"Large Brilliant Shard": 4,
			"Essence of Undeath": 4
        }
    },
    "Weapon - Winters Might": {
        "ID":       21931,
        "Learn":    190,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Drop",
        "RecipeID": 17725,
        "Reagents": {
			"Greater Mystic Essence": 3,
			"Vision Dust": 3,
			"Large Glowing Shard": 1,
			"Wintersbite": 2
        }
    },
    "Enchanted Leather": {
        "ID":       17181,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Rugged Leather": 1,
			"Lesser Eternal Essence": 1
        }
    },
    "Enchanted Thorium": {
        "ID":       17180,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Thorium Bar": 1,
			"Dream Dust": 3
        }
    },
    "Greater Magic Wand": {
        "ID":       14807,
        "Learn":    70,
        "Yellow":   110,
        "Green":    130,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
			"Simple Wood": 1,
			"Greater Magic Essence": 1
        }
    },
    "Greater Mystic Wand": {
        "ID":       14810,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
			"Star Wood": 1,
			"Greater Mystic Essence": 1,
			"Vision Dust": 1
        }
    },
    "Lesser Magic Wand": {
        "ID":       14293,
        "Learn":    10,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Trainer",
        "Reagents": {
			"Simple Wood": 1,
			"Lesser Magic Essence": 1
        }
    },
    "Lesser Mana Oil": {
        "ID":       25127,
        "Learn-PHASE-5":    250,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Vendor",
        "Reagents": {
			"Dream Dust": 3,
			"Purple Lotus": 2,
			"Crystal Vial": 1
        }
    },
    "Lesser Mystic Wand": {
        "ID":       14809,
        "Learn":    155,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Star Wood": 1,
			"Lesser Mystic Essence": 1,
			"Soul Dust": 1
        }
    },
    "Lesser Wizard Oil": {
        "ID":       25126,
        "Learn-PHASE-5":    200,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Vendor",
        "Reagents": {
			"Vision Dust": 3,
			"Stranglethorn Seed": 2,
			"Leaded Vial": 1
        }
    },
    "Minor Mana Oil": {
        "ID":       25125,
        "Learn-PHASE-5":    150,
        "Yellow":   160,
        "Green":    170,
        "Grey":     180,
        "Source":   "Vendor",
        "Reagents": {
			"Soul Dust": 3,
			"Maple Seed": 2,
			"Leaded Vial": 1
        }
    },
    "Smoking Heart of the Mountain": {
        "ID":       15596,
        "Learn":    265,
        "Yellow":   285,
        "Green":    305,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 11813,
        "Reagents": {
			"Blood of the Mountain": 1,
			"Essence of Fire": 1,
			"Small Brilliant Shard": 3
        }
    },
    "Wizard Oil": {
        "ID":       25128,
        "Learn-PHASE-5":    275,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
			"Illusion Dust": 3,
			"Firebloom": 2,
			"Crystal Vial": 1
        }
    }
}

import json
with open('enchanting.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)