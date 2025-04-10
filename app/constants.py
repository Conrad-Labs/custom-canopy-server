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
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/half-walls-front-keoAhvRi7FiCU4kPBixpTVUAXfkqs0.png",
            "include_conditions": {"tent_type": "half-walls"},
        },
        {
            "name": "half-wall",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/half-walls-side-dyzU1hP5nsEefl5IxHsOoOnbHhGXon.png",
            "include_conditions": {"tent_type": "half-walls"},
        },
        {
            "name": "no-walls",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/no-walls-6PiBwvy77Bdo9LXWT6RAvoMKtETKHL.png",
            "include_conditions": {"tent_type": "no-walls"},
        },
        {
            "name": "top-view",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/top-view-nykA47xWcnyOSkN86zhAFyh8kwj1bO.png",
            "include_conditions": {"tent_type": "all"},
        },
    ],
    "add_ons": [
        {
            "name": "table",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/add-ons/table-JQzC17ZdlVq31ZJsb8azUcs0E2Dfk6.png",
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
                    "scale": 1.3,
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
                    "scale": 0.9,
                },
                "right": {
                    "coordinates": [(1948, 460), (2114, 498), (2363, 632), (2025, 551)],
                    "scale": 1.1,
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
                    "scale": 1,
                },
                "right": {
                    "coordinates": [(2051, 472), (2431, 505), (3148, 861), (2065, 795)],
                    "scale": 0.9,
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
                    "scale": 0.9,
                },
                "right": {
                    "coordinates": [(2195, 393), (2363, 434), (3053, 807), (2126, 632)],
                    "scale": 0.9,
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
                    "coordinates": [(2271, 749), (826, 1402), (2271, 1302), (2271,1026)],
                    "scale": 1,
                },
                "right": {
                    "coordinates": [(2271, 749), (3677, 1398), (2271, 1302), (2271,1026)],
                    "scale": 1,
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (655, 1412),
                            (2271, 1305),
                            (2271, 1761),
                            (655, 1811),
                        ],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [
                            (2271, 1305),
                            (3887, 1411),
                            (3887, 1811),
                            (2271, 1761),
                        ],
                        "scale": 0.5,
                    },
                }
            },
        },
        "color-coordinates": {
            "peaks": {
                "front": [(2271, 749), (826, 1402), (2271, 1302)],
                "right": [(2271, 749), (3677, 1398), (2271, 1302)],
            },
            "valences": {
                "front": [(655, 1412), (2271, 1305), (2271, 1761), (655, 1811)],
                "right": [(2271, 1305), (3887, 1411), (3887, 1811), (2271, 1761)],
            },
        },
        "masks": {},
    },
    "top-view": {
        "logos": {
            "peaks": {
                "bottom": {
                    "coordinates": [
                        (1144, 3478),
                        (2286, 2304),
                        (3426, 3478),
                        (2285, 3478),
                    ],
                    "scale": 1,
                },
                "left": {
                    "coordinates": [
                        (1113, 1339),
                        (2286, 2304),
                        (1113, 3269),
                        (1113, 2304),
                    ],
                    "scale": 1,
                    "rotation_angle": 270,
                },
                "top": {
                    "coordinates": [
                        (1147, 1132),
                        (2286, 2304),
                        (3426, 1132),
                        (2287, 1132),
                    ],
                    "scale": 1,
                    "rotation_angle": 180,
                },
                "right": {
                    "coordinates": [
                        (3460, 1339),
                        (2286, 2304),
                        (3460, 3269),
                        (3460, 2304),
                    ],
                    "scale": 1,
                    "rotation_angle": 90,
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [
                            (1091, 3483),
                            (3480, 3483),
                            (3480, 3796),
                            (1091, 3796),
                        ],
                        "scale": 0.5,
                    },
                    "left": {
                        "coordinates": [
                            (795, 1291),
                            (1111, 1291),
                            (1111, 3322),
                            (795, 3322),
                        ],
                        "scale": 0.5,
                        "rotation_angle": 270,
                    },
                    "back": {
                        "coordinates": [
                            (1093, 818),
                            (3480, 818),
                            (3479, 1130),
                            (1093, 1130),
                        ],
                        "scale": 0.5,
                    },
                    "right": {
                        "coordinates": [
                            (3462, 1291),
                            (3778, 1291),
                            (3778, 3322),
                            (3462, 3322),
                        ],
                        "scale": 0.5,
                        "rotation_angle": 90,
                    },
                }
            },
        },
        "color-coordinates": {
            "peaks": {
                "front": [(1144, 3478), (2286, 2304), (3426, 3478)],
                "left": [(1113, 1339), (2286, 2304), (1113, 3269)],
                "back": [(1147, 1132), (2286, 2304), (3426, 1132)],
                "right": [(3460, 1339), (2286, 2304), (3460, 3269)],
            },
            "valences": {
                "front": [(1091, 3483), (3480, 3483), (3480, 3796), (1091, 3796)],
                "left": [(795, 1291), (1111, 1291), (1111, 3322), (795, 3322)],
                "back": [(1093, 1130), (1093, 818), (3480, 818), (3479, 1130)],
                "right": [(3462, 1291), (3778, 1291), (3778, 3322), (3462, 3322)],
            },
        },
        "masks": {},
    },
    "add_ons": {
        "table": {
            "logos": {
                "sides": {
                    "front": {
                        "coordinates": [
                            (1044, 1948),
                            (3457, 1951),
                            (3536, 2929),
                            (963, 2929),
                        ],
                        "scale": 0.5,
                    },
                }
            },
            "color-coordinates": {
                "sides": {
                    "front": [(1042, 1949), (3455, 1949), (3539, 2927), (960, 2927)],
                    "top": [(1167, 1858), (3331, 1858), (3455, 1949), (1042, 1949)],
                    "bottom": {
                        "left": {
                            "circle": {
                                "center": [1095, 2914],
                                "axes": [49, 63],
                                "angle": 0,
                                "start_angle": 0,
                                "end_angle": 180,
                            }
                        },
                        "right": {
                            "circle": {
                                "center": [3424, 2914],
                                "axes": [49, 63],
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
