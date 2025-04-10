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
            "name": "half-walls-front",
            "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/half-walls-front-lkWLhrmmJ5RkG8nkEiV3mlDKinN099.png",
            "include_conditions": {"tent_type": "half-walls"},
        },
        {
          "name": "full-walls-front",
          "url": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/canopy-mockups/full-walls-front-AClRtynCRsbMp2oHF5EpagTMIT6XR9.png",
          "include_conditions": {"tent_type": "full-walls"}
        },
        {
            "name": "half-walls-side",
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
    "half-walls-front": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [
                        (1207, 1851),
                        (3401, 1853),
                        (3406, 3476),
                        (1228, 3473),
                    ],
                    "scale": 0.8,
                },
                "left": {
                    "coordinates": [
                        (998, 2988),
                        (1121, 2802),
                        (1113, 3461),
                        (990, 3447),
                    ],
                    "scale": 1.2,
                },
                "right": {
                    "coordinates": [
                        (3500, 2802),
                        (3613, 2988),
                        (3620, 3487),
                        (3507, 3481),
                    ],
                    "scale": 1.2,
                },
            },
            "peaks": {
                "top": {
                    "coordinates": [
                        (1910, 809),
                        (2712, 809),
                        (3124, 1128),
                        (1457, 1128)
                        ],
                    "scale": 1.3
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [(884, 1240), (3728, 1240), (3728, 1725), (885, 1725)],
                        "scale": 0.8,
                    },
                }
            },
        },
        "color-coordinates": {
            "panels": {
                "left": [(963, 2860), (1133, 2762), (1133, 3522), (968, 3710)],
                "right": [(3488, 2757), (3640, 2846), (3643, 3690), (3488, 3516)],
                "back": [(1185, 1818), (3437, 1818), (3437, 3513), (1185, 3512)],
            },
            "peaks": {
                "front": [(2307, 616), (978, 1240), (3630, 1239)],
            },
            "valences": {
                "front": [(884, 1240), (3728, 1240), (3728, 1725), (885, 1725)],
            },
        },
        "masks": {
            "1": [(958, 2853), (976, 2909)],
            "2": [(954, 3614), (976, 3673)],
            "3": [(1128, 2732), (1186, 2776)],
            "4": [(1129, 3359), (1187, 3401)],
            "5": [(3635, 2853), (3658, 2910)],
            "6": [(3635, 3614), (3660, 3673)],
            "7": [(3435, 3360), (3493, 3402)],
            "8": [(3435, 2734), (3492, 2776)],
            "9": [(1123, 1819), (1186, 1854)],
            "10": [(3435, 1813), (3498, 1853)],
            "11": [(1129, 3459), (1228, 3502)],
            "12": [(3396, 3459), (3494, 3502)]
        },
    },
    "full-walls-front": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [
                        (1207, 1851),
                        (3401, 1853),
                        (3406, 3476),
                        (1228, 3473),
                    ],
                    "scale": 0.8,
                },
                "left": {
                    "coordinates": [
                        (998, 1962),
                        (1121, 1966),
                        (1113, 3344),
                        (990, 3415),
                    ],
                    "scale": 1.2,
                },
                "right": {
                    "coordinates": [
                        (3500, 1966),
                        (3613, 1962),
                        (3620, 3415),
                        (3507, 3344),
                    ],
                    "scale": 1.2,
                },
            },
            "peaks": {
                "top": {
                    "coordinates": [
                        (1910, 809),
                        (2712, 809),
                        (3124, 1128),
                        (1457, 1128)
                        ],
                    "scale": 1.3
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [(884, 1240), (3728, 1240), (3728, 1725), (885, 1725)],
                        "scale": 0.8,
                    },
                }
            },
        },
        "color-coordinates": {
            "panels": {
                "left": [(971, 1755), (1138, 1813), (1133, 3522), (968, 3710)],
                "right": [(3490, 1807), (3639, 1756), (3643, 3690), (3488, 3516)],
                "back": [(1185, 1818), (3437, 1818), (3437, 3513), (1185, 3512)],
            },
            "peaks": {
                "front": [(2307, 616), (978, 1240), (3630, 1239)],
            },
            "valences": {
                "front": [(884, 1240), (3728, 1240), (3728, 1725), (885, 1725)],
            },
        },
        "masks": {
            "1": [(901, 3515), (976, 3569)],
            "2": [(917, 1748), (977, 1769)],
            "3": [(1128, 3310), (1187, 3352)],
            "4": [(3436, 3313), (3493, 3353)],
            "5": [(3635, 3513), (3716, 3568)],
            "6": [(3635, 1740), (3689, 1768)],
            "7": [(1128, 1812), (1187, 1854)],
            "8": [(3435, 1813), (3493, 1853)],
            "9": [(1129, 3459), (1228, 3502)],
            "10": [(3396, 3459), (3494, 3502)]
        },
    },
    "half-walls-side": {
        "logos": {
            "panels": {
                "back": {
                    "coordinates": [(2279, 1848), (3778, 1813), (3788, 3172), (2279, 3139)],
                    "scale": 0.8,
                    "mask": [
                        (2279, 2778),
                        (3787, 2687),
                        (3788, 3432),
                        (2282, 3616),
                    ],                },
                "left": {
                    "coordinates": [
                        (717, 2610),
                        (2162, 2568),
                        (2195, 3288),
                        (717, 3423),
                    ],
                    "scale": 0.6,
                },
                "right": {
                    "coordinates": [
                        (2279, 2788),
                        (3787, 2696),
                        (3790, 3432),
                        (2282, 3616),
                    ],
                    "scale": 0.6,
                },
            },
            "peaks": {
                "left": {
                    "coordinates": [(1881, 938), (2231, 917), (2204, 1255), (1123, 1350)],
                    "scale": 1
                },
                "right": {
                    "coordinates": [(2268, 928), (2602, 961), (3370, 1366), (2290, 1286)],
                    "scale": 1
                },
            },
            "valences": {
                "text": {
                    "front": {
                        "coordinates": [(635, 1413), (2251, 1305), (2251, 1760), (635, 1810)],
                        "scale": 0.9,
                    },
                    "right": {
                        "coordinates": [(2251, 1305), (3868, 1413), (3867, 1811), (2251, 1760)],
                        "scale": 0.9,
                    },
                },
            },
        },
        "color-coordinates": {
            "panels": {
                "back": [(2279, 1848), (3784, 1813), (3788, 3172), (2279, 3139)],
                "left": [
                    (706, 2598),
                    (2198, 2554),
                    (2197, 3298),
                    (705, 3428),
                ],
                "right": [
                    (2279, 2778),
                    (3787, 2687),
                    (3788, 3432),
                    (2282, 3616),
                ],
            },
            "peaks": {
                "front": [(2251, 748), (804, 1402), (2247, 1307)],
                "right": [(2251, 748), (2248, 1305), (3657, 1398)],
            },
            "valences": {
                "front": [(635, 1413), (2251, 1305), (2251, 1760), (635, 1810)],
                "right": [(2251, 1305), (3868, 1413), (3867, 1811), (2251, 1760)],
            },
        },
        "masks": {
            "1": [(660, 2652), (714, 2714)],
            "2": [(675, 3262), (713, 3321)],
            "3": [(2192, 2605), (2218, 2654)],
            "4": [(2192, 3168), (2218, 3217)],
            "5": [(2242, 2842), (2286, 2903)],
            "6": [(2249, 3450), (2287, 3513)],
            "7": [(3779, 1807), (3867, 1872)],
            "8": [(3779, 2749), (3862, 2810)],
            "9": [(3778, 3260), (3866, 3322)]
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
