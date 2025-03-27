CONRAD_TEXT = "CONRAD LABS | CONRADLABS.COM"
DEFAULT_TEXT = ""
DEFAULT_FONT_SIZE = 36
DEFAULT_PADDING = 10
DEFAULT_ROTATION_ANGLE = 0
DEFAULT_FONT_COLOUR = [255, 255, 255]
DEFAULT_TENT_COLOR = [0, 0, 0]
BLUE_TENT_COLOR = [255, 233, 211]
DEFAULT_FONT_URL = "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/fonts/GeliatExtralight-6YLRq-H5ccYOJVTzG6y1KwK6VRAVWQ8ZYKqQ.otf"
DEFAULT_OUTPUT_DIR = "mockups"
MOCKUP_ITEMS = {
    "tents": [
        {
            "name": "front-wall",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-front-PUClMH37WQ9ZeE441ENcj5OfQsIBeg.png",
            "include_conditions": {"tent_type": "half-walls"},
        },
        {
            "name": "half-wall",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-half-wall-YB36f9zdXBc7US0wwVkptbr8ilmGVg.png",
            "include_conditions": {"tent_type": "half-walls"},
        },
        {
            "name": "no-walls",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-no-walls-vWSBKzV0BzTsS7rv1E1JCzz5IMJ54O.png",
            "include_conditions": {"tent_type": "no-walls"},
        },
        {
            "name": "top-view",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-top-view-MDMODEv31VWZkrTotyIGGYgAhboYAH.png",
            "include_conditions": {"tent_type": "all"},
        },
    ],
    "add_ons": [
        {
            "name": "table",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/add-ons/table-mockup-yHAC8kEdXOjNWA2BC2Hx6P6K3ZKqvi.png",
            "exclude_conditions": {"add_ons": {"table": None}},
        },
    ],
}

SLOPE_CENTERS = {
    "top": (500, 258),
    "right": (726, 477),
    "bottom": (492, 695),
    "left": (275, 475),
}

OVERLAY_CONFIGURATIONS = {
    "front-wall": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [
                        (1090, 1281),
                        (2910, 1281),
                        (2910, 2621),
                        (1090, 2621),
                    ],
                    "scale": 0.9,
                },
                "left": {
                    "coordinates": [
                        (921, 2107),
                        (1040, 2047),
                        (1026, 2667),
                        (894, 2746),
                    ],
                    "scale": 1.2,
                },
                "right": {
                    "coordinates": [
                        (2974, 2092),
                        (3100, 2121),
                        (3089, 2665),
                        (2961, 2601),
                    ],
                    "scale": 1.1,
                },
            },
            "peaks": {
                "top": {
                    "coordinates": [(1665, 486), (2339, 486), (2659, 720), (1384, 720)],
                    "scale": 1.3
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (858, 829),
                            (3137, 829),
                            (3137, 1189),
                            (858, 1189),
                        ],
                        "scale": 0.5,
                    },
                }
            },
        },
        "color-coordinates": {
            "panels": {
                "left": [(891, 2012), (1061, 1947), (1046, 2663), (886, 2840)],
                "right": [(2940, 1951), (3109, 2013), (3112, 2843), (2953, 2666)],
                "back": [(1080, 1263), (2915, 1264), (2917, 2671), (1082, 2669)],
            },
            "peaks": {
                "front": [(2000, 267), (925, 814), (3065, 814)],
            },
            "valences": {
                "front": [(835, 812), (3165, 812), (3172, 1219), (830, 1220)],
            },
        },
        "masks": {
            "1": [(1079, 1885), (1124, 1930)],
            "2": [(1079, 2620), (1122, 2667)],
            "3": [(2876, 1885), (2932, 1930)],
            "4": [(2876, 2622), (2934, 2665)],
            "5": [(1048, 1998), (1070, 2047)],
            "6": [(1046, 2000), (1070, 2647)],
            "7": [(883, 2078), (900, 2130)],
            "8": [(885, 2754), (898, 2808)],
            "9": [(2940, 1999), (2951, 2600)],
            "10": [(3103, 2078), (3119, 2131)],
            "11": [(3103, 2756), (3117, 2808)],
        },
    },
    "wall-block": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [
                        (1744, 1041),
                        (2519, 994),
                        (2562, 1741),
                        (1745, 1699),
                    ],
                    "scale": 0.9,
                    "crop-type": "vertical",
                    "mask": [(1996, 863), (2882, 1810)],
                },
                "side": {
                    "coordinates": [
                        (2041, 911),
                        (2836, 999),
                        (2850, 1787),
                        (2036, 1960),
                    ],
                    "scale": 0.9,
                },
            },
            "peaks": {
                "left": {
                    "coordinates": [(1523, 469), (1879, 427), (1953, 574), (1182, 677)],
                    "scale": 0.9
                },
                "right": {
                    "coordinates": [(1948, 460), (2114, 498), (2363, 632), (2025, 551)],
                    "scale": 1.1
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (672, 762),
                            (2000, 598),
                            (2001, 788),
                            (672, 916),
                        ],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [
                            (2028, 574),
                            (2906, 796),
                            (2901, 952),
                            (2025, 801),
                        ],
                        "scale": 0.5,
                    },
                }
            },
        },
        "color-coordinates": {
            "panels": {
                "front": [(1718, 1020), (1987, 1005), (1986, 1740), (1716, 1726)],
                "right": [(2022, 808), (2857, 955), (2862, 1812), (2024, 1982)],
            },
            "peaks": {
                "front": [(1815, 296), (970, 709), (2486, 683)],
            },
            "valences": {
                "left": [(659, 749), (2023, 573), (2028, 807), (658, 938)],
                "right": [(2023, 573), (2903, 785), (2908, 964), (2028, 810)],
            },
        },
        "masks": {
            "1": [(1714, 1106), (1733, 1130)],
            "2": [(1712, 1647), (1733, 1671)],
            "3": [(2017, 1813), (2030, 1858)],
            "4": [(2015, 1810), (2035, 1850)],
            "5": [(2017, 810), (2031, 856)],
            "6": [(2010, 898), (2030, 939)],
        },
    },
    "half-wall": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [
                        (2079, 1320),
                        (3439, 1285),
                        (3410, 2662),
                        (2077, 2560),
                    ],
                    "scale": 0.8,
                    "mask": [(2019, 2065), (3527, 2002), (3528, 2781), (2024, 2950)],
                },
                "left": {
                    "coordinates": [
                        (654, 2123),
                        (1971, 2078),
                        (1968, 2609),
                        (678, 2726),
                    ],
                    "scale": 0.6,
                },
                "right": {
                    "coordinates": [
                        (2140, 2125),
                        (3438, 2073),
                        (3435, 2731),
                        (2138, 2877),
                    ],
                    "scale": 0.6,
                },
            },
            "peaks": {
                "left": {
                    "coordinates": [(1623, 535), (1975, 492), (1996, 785), (919, 861)],
                    "scale": 1
                },
                "right": {
                    "coordinates": [(2051, 472), (2431, 505), (3148, 861), (2065, 795)],
                    "scale": 0.9
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (568, 927),
                            (2006, 839),
                            (2010, 1204),
                            (567, 1253),
                        ],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [
                            (2081, 831),
                            (3492, 930),
                            (3496, 1250),
                            (2094, 1198),
                        ],
                        "scale": 0.5,
                    },
                },
            },
        },
        "color-coordinates": {
            "panels": {
                "back": [(2074, 1295), (3461, 1260), (3467, 2010), (2072, 2070)],
                "left": [
                    (608, 2006),
                    (2012, 1960),
                    (2012, 2648),
                    (600, 2776),
                ],
                "right": [
                    (2072, 2069),
                    (3484, 2009),
                    (3480, 2780),
                    (2069, 2947),
                ],
            },
            "peaks": {
                "front": [(2040, 293), (656, 911), (2038, 809)],
                "right": [(2040, 293), (2038, 809), (3374, 900)],
            },
            "valences": {
                "front": [(550, 910), (2046, 808), (2039, 1228), (546, 1277)],
                "right": [(2044, 810), (3525, 909), (3530, 1278), (2039, 1228)],
            },
        },
        "masks": {
            "1": [(604, 2058), (653, 2106)],
            "2": [(594, 2671), (652, 2718)],
            "3": [(1988, 2008), (2018, 2051)],
            "4": [(1986, 2556), (2018, 2598)],
            "5": [(2009, 2122), (2120, 2176)],
            "6": [(3452, 2060), (3504, 2107)],
            "7": [(3453, 2677), (3497, 2725)],
            "8": [(2068, 2825), (2121, 2879)],
            "9": [(3424, 1932), (3477, 1981)],
            "10": [(2007, 1982), (2080, 2035)],
            "11": [(2032, 1898), (2083, 1938)],
            "12": [(2070, 1274), (2080, 1294)],
        },
    },
    "wall-pillar": {
        "logos": {
            "panels": {
                "left": {
                    "coordinates": [
                        (702, 1175),
                        (1795, 1273),
                        (1799, 2506),
                        (693, 2633),
                    ],
                    "scale": 0.7,
                },
                "right": {
                    "coordinates": [
                        (1859, 1265),
                        (3330, 1198),
                        (3329, 2585),
                        (1854, 2481),
                    ],
                    "scale": 0.7,
                },
            },
            "peaks": {
                "left": {
                    "coordinates": [(1765, 404), (2126, 363), (2277, 632), (1027, 727)],
                    "scale": 0.9
                },
                "right": {
                    "coordinates": [(2195, 393), (2363, 434), (3053, 807), (2126, 632)],
                    "scale": 0.9
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (645, 818),
                            (2362, 676),
                            (2378, 1046),
                            (644, 1145),
                        ],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [
                            (2427, 676),
                            (3397, 872),
                            (3404, 1185),
                            (2441, 1050),
                        ],
                        "scale": 0.5,
                    },
                }
            },
        },
        "color-coordinates": {
            "panels": {
                "left": [(680, 1150), (1820, 1250), (1815, 2502), (676, 2657)],
                "right": [(1846, 1250), (3349, 1190), (3364, 2602), (1849, 2502)],
            },
            "peaks": {
                "left": [(2063, 251), (770, 803), (2370, 656)],
                "right": [(2063, 250), (2370, 656), (3192, 825)],
            },
            "valence": {
                "left": [(631, 806), (2404, 654), (2409, 1072), (624, 1168)],
                "right": [(2404, 656), (3411, 866), (3416, 1206), (2409, 1072)],
            },
        },
        "masks": {
            "1": [(668, 1177), (688, 1224)],
            "2": [(675, 1764), (720, 1810)],
            "3": [(673, 2604), (718, 2653)],
            "4": [(1795, 1760), (1851, 1798)],
            "5": [(1819, 1802), (1881, 1840)],
            "6": [(1793, 2409), (1841, 2448)],
            "7": [(1815, 2458), (1881, 2496)],
            "8": [(3341, 1763), (3376, 1806)],
            "9": [(3318, 1810), (3381, 1854)],
            "10": [(3344, 2496), (3385, 2542)],
            "11": [(2371, 1220), (2430, 2544)],
            "12": [(3319, 2548), (3381, 2594)],
        },
    },
    "no-walls": {
        "logos": {
            "peaks": {
                "left": {
                    "coordinates": [(429, 224), (522, 218), (532, 281), (255, 307)],
                    "scale": 1
                },
                "right": {
                    "coordinates": [(530, 216), (598, 221), (761, 298), (545, 286)],
                    "scale": 1
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [(161, 325), (539, 299), (539, 369), (161, 370)],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [(547, 297), (874, 322), (874, 372), (547, 372)],
                        "scale": 0.5,
                    },
                }
            },
        },
        "color-coordinates": {
            "peaks": {
                "front": {
                    "top": [(521, 170), (417, 230), (527, 228)],
                    "bottom-1": [(416, 237), (526, 226), (541, 292), (156, 321)],
                    "bottom-2": [(428, 223), (502, 222), (490, 264), (337, 263)],
                },
                "right": {
                    "top": [(523, 170), (531, 233), (662, 256)],
                    "bottom-1": [(531, 233), (690, 271), (871, 319), (543, 291)],
                    "bottom-2": [(529, 223), (606, 222), (752, 290), (540, 266)],
                },
            },
            "valences": {
                "front": [(158, 322), (542, 294), (542, 374), (157, 376)],
                "right": [(545, 293), (873, 321), (873, 374), (545, 374)],
            },
        },
        "masks": {},
    },
    "top-view": {
        "logos": {
            "peaks": {
                "bottom": {
                    "coordinates": [(397, 641), (612, 641), (612, 810), (397, 810)],
                    "scale": 1,
                },
                "left": {
                    "coordinates": [(345, 372), (345, 592), (175, 592), (175, 372)],
                    "scale": 1,
                    "rotation_angle": 270,
                },
                "top": {
                    "coordinates": [(606, 333), (393, 333), (393, 151), (606, 151)],
                    "scale": 1,
                    "rotation_angle": 180,
                },
                "right": {
                    "coordinates": [(650, 591), (650, 376), (832, 376), (832, 591)],
                    "scale": 1,
                    "rotation_angle": 90,
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [(238, 825), (766, 825), (766, 886), (238, 886)],
                        "scale": 0.5,
                    },
                    "left": {
                        "coordinates": [(101, 217), (161, 217), (161, 745), (101, 745)],
                        "scale": 0.5,
                        "rotation_angle": 270,
                    },
                    "back": {
                        "coordinates": [(767, 141), (236, 141), (236, 84), (767, 84)],
                        "scale": 0.5
                    },
                    "right": {
                        "coordinates": [(847, 220), (902, 220), (902, 758), (847, 758)],
                        "scale": 0.5,
                        "rotation_angle": 90,
                    },
                }
            },
        },
        "color-coordinates": {
            "peaks": {
                "front": {
                    "top": [(502, 485), (449, 567), (552, 565)],
                    "bottom": [(449, 567), (552, 565), (776, 817), (228, 817)],
                },
                "left": {
                    "top": [(500, 483), (410, 425), (410, 539)],
                    "bottom": [(410, 423), (417, 536), (167, 756), (167, 210)],
                },
                "back": {
                    "top": [(501, 480), (556, 395), (448, 395)],
                    "bottom": [(556, 395), (446, 395), (229, 148), (774, 148)],
                },
                "right": {
                    "top": [(502, 483), (589, 537), (589, 427)],
                    "bottom": [(589, 539), (589, 425), (837, 208), (837, 757)],
                },
            },
            "valences": {
                "front": [(233, 821), (766, 821), (768, 885), (236, 885)],
                "left": [(100, 215), (162, 215), (162, 748), (100, 748)],
                "back": [(236, 80), (768, 80), (768, 143), (236, 143)],
                "right": [(841, 217), (903, 217), (903, 751), (841, 751)],
            },
        },
        "masks": {},
    },
    "add_ons": {
        "table": {
            "logos": {
                "sides": {
                    "front": {
                        "coordinates": [(377, 361), (2917, 361), (3021, 1388), (277, 1388)],
                        "scale": 0.5,
                    },
                }
            },
            "color-coordinates": {
                "sides": {
                    "front": [(377, 361), (2917, 361), (3021, 1388), (277, 1388)],
                    "top": [(547, 266), (2751, 266), (2917, 361), (377, 361)],
                    "bottom": {
                        "left": {
                            "circle": {
                                "center": [439, 1380],
                                "axes": [71, 71],
                                "angle": 0,
                                "start_angle": 0,
                                "end_angle": 180,
                            }
                        },
                        "right": {
                            "circle": {
                                "center": [2860, 1380],
                                "axes": [71, 71],
                                "angle": 0,
                                "start_angle": 0,
                                "end_angle": 180,
                            }
                        },
                    },
                }
            },
            "masks": {},
        },
    },
}
