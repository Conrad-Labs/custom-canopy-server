CONRAD_TEXT = "CONRAD LABS | CONRADLABS.COM"
DEFAULT_TEXT = ""
DEFAULT_FONT_SIZE = 25
DEFAULT_PADDING = 10
DEFAULT_ROTATION_ANGLE = 0
DEFAULT_FONT_COLOUR = [255, 255, 255]
DEFAULT_TENT_COLOR = [0, 0, 0]
BLUE_TENT_COLOR = [255, 233, 211]
DEFAULT_IS_PATTERNED='false'
DEFAULT_FONT_URL = "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/fonts/arial-B9hR4qfr9oEZX8IcjHDXp6HFNq4yzz.ttf"
# DEFAULT_TEMPLATE_URL="https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/templates/wave-pattern-pQssnp9mX6krbfvdUCB9tWlE1N8qyA.jpg"
DEFAULT_TEMPLATE_URL="https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/templates/wave-pattern-bUfoUtRUqIcWw9nKAAv2X0fxFUsp81.png"
TENT_MOCKUPS = {
    "front": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-front-PUClMH37WQ9ZeE441ENcj5OfQsIBeg.png",
    "half-wall": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-half-wall-YB36f9zdXBc7US0wwVkptbr8ilmGVg.png",
    "top-view": "https://xyvvsdhvfprf3oqa.public.blob.vercel-storage.com/custom-canopy-server-static/images/tent-mockup-top-view-MDMODEv31VWZkrTotyIGGYgAhboYAH.png"
}
DEFAULT_OUTPUT_DIR = "mockups"

SLOPE_CENTERS = {
    "top": (500, 258),
    "right": (726, 477),
    "bottom": (492, 695),
    "left": (275, 475)
}

OVERLAY_CONFIGURATIONS = {
    
    "front": {
        
        "logos": {
            
            "top-slope": {
                "coordinates": [(1665, 536), (2339, 536), (2659, 808), (1384, 808)],
                "scale": 1.1,
            },
            "template": {
                "coordinates": [(1080, 1263), (2915, 1264), (2917, 2671), (1082, 2669)],
                "scale": 1
            },
            "back-wall": {
                "coordinates": [(1090, 1281), (2910, 1281), (2910, 2621), (1090, 2621)],
                "scale": 0.7
            },
            "left-side-wall": {
                "coordinates": [(906, 2091), (1047, 2037), (1050, 2665), (912, 2804)],
                "scale": 0.9
            },
            "right-side-wall": {
                "coordinates": [(2966, 2050), (3097, 2099), (3093, 2801), (2961, 2655)],
                "scale": 0.9
            },
            "canopy-text": {
                "coordinates": [(858, 829), (3137, 829), (3137, 1189), (858, 1189)],
                "scale": 0.5
            }
            
        },
        
        "color-coordinates": {
            
            "slope": [(2000, 267), (925, 814), (3065, 814)],
            "canopy": [(835, 812), (3165, 812), (3172, 1219), (830, 1220)],
            "back_wall": [(1080, 1263), (2915, 1264), (2917, 2671), (1082, 2669)],
            "side_wall_left": [(891, 2012), (1061, 1947), (1046, 2663), (886, 2840)],
            "side_wall_right": [(2940, 1951), (3109, 2013), (3112, 2843), (2953, 2666)]
            
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
            "11": [(3103, 2756), (3117, 2808)]
            
        }
        
    },
    
    "wall-block": {
        
        "logos": {
            
    
            "left-slope": {
                "coordinates": [(1523, 469), (1879, 427), (1953, 574), (1182, 677)],
                "scale": 0.90,
            },
            "right-slope": {
                "coordinates": [(1948, 460), (2114, 498), (2363, 632), (2025, 551)],
                "scale": 1.1,
            },
            "canopy-left-text": {
                "coordinates": [(672, 762), (2000, 598), (2001, 788), (672, 916)],
                "scale": 0.5
            },
            "canopy-right-text": {
                "coordinates": [(2028, 574), (2906, 796), (2901, 952), (2025, 801)],
                "scale": 0.5
            },
            "template": {
                "coordinates": [(1718, 1020), (1987, 1005), (1986, 1740), (1716, 1726)],
                "scale": 1,
                "crop-type": "vertical",
                "mask": [(1996, 863), (2882, 1810)]
            },
            "back-wall": {
                "coordinates": [(1744, 1041), (2519, 994), (2562, 1741), (1745, 1699)],
                "scale": 0.9,
                "crop-type": "vertical",
                "mask": [(1996, 863), (2882, 1810)]
            },
            "right-side-wall": {
                "coordinates": [(2041, 911), (2836, 999), (2850, 1787), (2036, 1960)],
                "scale": 0.9,
            },
            
        },
        
        "color-coordinates": {
            
            "back-wall": [(1718, 1020), (1987, 1005), (1986, 1740), (1716, 1726)],
            "slope": [(1815, 296), (970, 709), (2486, 683)],
            "canopy-left": [(659, 749), (2023, 573), (2028, 807), (658, 938)],
            "canopy-right": [(2023, 573), (2903, 785), (2908, 964), (2028, 810)],
            "side-wall": [(2022, 808), (2857, 955), (2862, 1812), (2024, 1982)],
            
        },
    
        "masks": {
            
            "1": [(1714, 1106), (1733, 1130)],
            "2": [(1712, 1647), (1733, 1671)],
            "3": [(2017, 1813), (2030, 1858)],
            "4": [(2015, 1810), (2035, 1850)],
            "5": [(2017, 810), (2031, 856)],
            "6": [(2010, 898), (2030, 939)]
            
        },
        
    },
    
    "half-wall": {
        
        "logos": {
            
            "left-slope": {
                "coordinates": [(1673, 535), (2015, 492), (1996, 805), (919, 881)],
                "scale": 1
            },
            "right-slope": {
                "coordinates": [(2051, 472), (2431, 505), (3148, 861), (2065, 795)],
                "scale": 0.9,
            },
            "left-canopy-text": {
                "coordinates": [(568, 927), (2006, 839), (2010, 1204), (567, 1253)],
                "scale": 0.5
            },
            "right-canopy-text": {
                "coordinates": [(2081, 831), (3492, 930), (3496, 1250), (2094, 1198)],
                "scale": 0.5
            },
            "template": {
                "coordinates": [(2070, 1274), (3468, 1275), (3467, 2710), (2072, 2770)],
                "scale": 1,
                "mask": [(2019, 2065), (3527, 2002), (3528, 2781), (2024, 2950)]
            },
            "back-wall": {
                "coordinates": [(2079, 1320), (3439, 1285), (3410, 2662), (2077, 2560)],
                "scale": 0.8,
                "mask": [(2019, 2065), (3527, 2002), (3528, 2781), (2024, 2950)]
            },
            "left-side-wall": {
                "coordinates": [(654, 2123), (1971, 2078), (1968, 2609), (678, 2726)],
                "scale": 0.6,
            },
            "right-side-wall": {
                "coordinates": [(2140, 2125), (3438, 2073), (3435, 2731), (2138, 2877)],
                "scale": 0.6
            },
            
        },
        
        "color-coordinates": {
            
            "slope-left": [(2040, 293), (656, 911), (2038, 809)],
            "slope-right": [(2040, 293), (2038, 809), (3374, 900)],
            "canopy-left": [(550, 910), (2046, 808), (2039, 1228), (546, 1277)],
            "canopy-right": [(2044, 810), (3525, 909), (3530, 1278), (2039, 1228)],
            "back-wall": [(2074, 1295), (3461, 1260), (3467, 2010), (2072, 2070)],
            "left-side-wall": [(608, 2006), (2012, 1960), (2012, 2648), (600, 2776)],
            "right-side-wall": [(2072, 2069), (3484, 2009), (3480, 2780), (2069, 2947)]
            
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
            "12": [(2070, 1274), (2080, 1294)]
            
        },
        
    },
    
    "wall-pillar": {
        
        "logos": {
            
            "left-side-wall": {
                "coordinates": [(702, 1175), (1795, 1273), (1799, 2506), (693, 2633)],
                "scale": 0.7
            },
            "left-slope": {
                "coordinates": [(1765, 404), (2126, 363), (2277, 632), (1027, 727)],
                "scale": 0.9
            },
            "right-slope": {
                "coordinates": [(2195, 393), (2363, 434), (3053, 807), (2126, 632)],
                "scale": 0.9
            },
            "left-canopy-text": {
                "coordinates": [(645, 818), (2362, 676), (2378, 1046), (644, 1145)],
                "scale": 0.5
            },
            "right-canopy-text": {
                "coordinates": [(2427, 676), (3397, 872), (3404, 1185), (2441, 1050)],
                "scale": 0.5
            },
            "right-side-wall": {
                "coordinates": [(1859, 1265), (3330, 1198), (3329, 2585), (1854, 2481)],
                "scale": 0.7,
            },
            
        },
        
        "color-coordinates": {
            
            "left-slope": [(2063, 251), (770, 803), (2370, 656)],
            "right-slope": [(2063, 250), (2370, 656), (3192, 825)],
            "left-canopy": [(631, 806), (2404, 654), (2409, 1072), (624, 1168)],
            "right-canopy": [(2404, 656), (3411, 866), (3416, 1206), (2409, 1072)],
            "left-wall": [(680, 1150), (1820, 1250), (1815, 2502), (676, 2657)],
            "right-wall": [(1846, 1250), (3349, 1190), (3364, 2602), (1849, 2502)]
            
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
            "12": [(3319, 2548), (3381, 2594)]
            
        }
        
    },

    "no-walls": {
        
        "logos": {
            
            "left-slope": {
                "coordinates": [(411, 235), (525, 226), (540, 289), (191, 314)],
                "scale": 0.9
            },
            "right-slope": {
                "coordinates": [(532, 225), (629, 235), (814, 315), (545, 290)],
                "scale": 0.9
            },
            "left-canopy-text": {
                "coordinates": [(161, 325), (539, 299), (539, 369), (161, 370)],
                "scale": 0.5
            },
            "right-canopy-text": {
                "coordinates": [(547, 297), (874, 322), (874, 372), (547, 372)],
                "scale": 0.5
            }
            
        },
        
        "color-coordinates": {
            
            "left-slope-top": [(521, 170), (417, 230), (527, 228)],
            "left-slope-bottom-1": [(416, 237), (526, 226), (541, 292), (156, 321)],
            "left-slope-bottom-2": [(428, 223), (502, 222), (490, 264), (337, 263)],
            "right-slope-top": [(523, 170), (531, 233), (662, 256)],
            "right-slope-bottom-1": [(531, 233), (690, 271), (871, 319), (543, 291)],
            "right-slope-bottom-2": [(529, 223), (606, 222), (752, 290), (540, 266)],
            "canopy-left": [(158, 322), (542, 294), (542, 374), (157, 376)],
            "canopy-right": [(545, 293), (873, 321), (873, 374), (545, 374)]
            
        },
    
        "masks": {}
        
    },
    
    "top-view": {
        
        "logos": {
            
            "bottom-slope": {
                "coordinates": [(397, 641), (612, 641), (612, 810), (397, 810)],
                "scale": 1
            },
            "left-slope": {
                "coordinates": [(345, 372), (345, 592), (175, 592), (175, 372)],
                "scale": 1,
                "rotation_angle": 270
            },
            "top-slope": {
                "coordinates": [(606, 333), (393, 333), (393, 151), (606, 151)],
                "scale": 1,
                "rotation_angle": 180
            },
            "right-slope": {
                "coordinates": [(650, 591), (650, 376), (832, 376), (832, 591)],
                "scale": 1,
                "rotation_angle": 90
            },
            "bottom-canopy-text": {
                "coordinates": [(238, 825), (766, 825), (766, 886), (238, 886)],
                "scale": 0.5
            },
            "left-canopy-text": {
                "coordinates": [(161, 217), (161, 745), (101, 745), (101, 217)],
                "scale": 0.5,
                "rotation_angle": 270
            },
            "top-canopy-text": {
                "coordinates": [(767, 141), (236, 141), (236, 84), (767, 84)],
                "scale": 0.5,
                "rotation_angle": 180
            },
            "right-canopy-text": {
                "coordinates": [(847, 758), (847, 220), (902, 220), (902, 758)],
                "scale": 0.5,
                "rotation_angle": 90
            }
            
        },
        
        "color-coordinates": {
            
            "slope-top-1": [(502, 485), (449, 567), (552, 565)],
            "slope-bottom-1": [(449, 567), (552, 565), (776, 817), (228, 817)],
            "canopy-1": [(233, 821), (766, 821), (768, 885), (236, 885)],
            
            "slope-top-2": [(500, 483), (410, 425), (410, 539)],
            "slope-bottom-2": [(410, 423), (417, 536), (167, 756), (167, 210)],
            "canopy-2": [(100, 215), (162, 215), (162, 748), (100, 748)],
            
            "slope-top-3": [(501, 480), (556, 395), (448, 395)],
            "slope-bottom-3": [(556, 395), (446, 395), (229, 148), (774, 148)],
            "canopy-3": [(236, 80), (768, 80), (768, 143), (236, 143)],
            
            "slope-top-4": [(502, 483), (589, 537), (589, 427)],
            "slope-bottom-4": [(589, 539), (589, 425), (837, 208), (837, 757)],
            "canopy-4": [(841, 217), (903, 217), (903, 751), (841, 751)]
            
        },
    
        "masks": {}
        
    }
}
