CONRAD_TEXT = "CONRAD LABS | CONRADLABS.COM"
DEFAULT_TEXT = ""
DEFAULT_FONT_SIZE = 20
DEFAULT_PADDING = 20
DEFAULT_ROTATION_ANGLE = 0
DEFAULT_FONT_COLOUR = (28, 28, 65, 255)
DEFAULT_TENT_COLOR = [0, 0, 0]
BLUE_TENT_COLOR = [255, 233, 211]

TENT_MOCKUPS = {
    "front": "tent-mockup-front.jpg",
    "half-wall": "tent-mockup-half-wall.jpg",
    "no-walls": "tent-mockup-no-walls.jpg",
    "top-view": "tent-mockup-top-view.jpg",
    "wall-block": "tent-mockup-wall-block.jpg",
    "wall-pillar": "tent-mockup-wall-pillar.jpg"
}

OVERLAY_CONFIGURATIONS = {
    
    "front": {
        
        "logos": {
            
            "back-wall": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_y_factor": 0.4,
                "left_x_factor": 0.5
            },
            
            "top-slope": {
                "width_scale": 0.5,
                "height_scale": 0.3,
                "top_left_x_factor": 0.375,
                "top_left_y_factor": 0.115,
                "top_right_x_factor": 0.6,
                "top_right_y_factor": 0.115,
                "bottom_left_x_factor": 0.39,
                "bottom_left_y_factor": 0.29,
                "bottom_right_x_factor": 0.635,
                "bottom_right_y_factor": 0.29,
                "perspective": True
            },
            
            "left-side-wall": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_left_x_factor": 0.23,
                "top_left_y_factor": 0.67,
                "top_right_x_factor": 0.26,
                "top_right_y_factor": 0.65,
                "bottom_left_x_factor": 0.23,
                "bottom_left_y_factor": 0.84,
                "bottom_right_x_factor": 0.26,
                "bottom_right_y_factor": 0.8,
                "perspective": True
            },
            
            "right-side-wall": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_left_x_factor": 0.745,
                "top_left_y_factor": 0.65,
                "top_right_x_factor": 0.775,
                "top_right_y_factor": 0.67,
                "bottom_left_x_factor": 0.745,
                "bottom_left_y_factor": 0.8,
                "bottom_right_x_factor": 0.775,
                "bottom_right_y_factor": 0.84,
                "perspective": True
            },
            
            "text": {
                "width_scale": 1.2,
                "height_scale": 1.2,
                "top_y_factor": 0.3,
                "left_x_factor": 0.5
            }
            
        },
        
        "coordinates": {
            "slope": [(2000, 267), (925, 814), (3065, 814)],
            "canopy": [(835, 812), (3165, 812), (3172, 1219), (830, 1220)],
            "back_wall": [(1080, 1263), (2915, 1264), (2917, 2671), (1082, 2669)],
            "side_wall_left": [(891, 2012), (1061, 1947), (1046, 2663), (886, 2840)],
            "side_wall_right": [(2940, 1951), (3109, 2013), (3112, 2843), (2953, 2666)]
        },
        
        "masks": {
            "1": (1079, 1885, 1124, 1930),
            "2": (1079, 2620, 1122, 2667),
            "3": (2876, 1885, 2932, 1930),
            "4": (2876, 2622, 2934, 2665),
            "5": (1048, 1998, 1070, 2047),
            "6": (1046, 2000, 1070, 2647),
            "7": (883, 2078, 900, 2130),
            "8": (885, 2754, 898, 2808),
            "9": (2940, 1999, 2951, 2600),
            "10": (3103, 2078, 3119, 2131),
            "11": (3103, 2756, 3117, 2808)
        }
    },
    
    "half-wall": {
        
        "logos": {
            
            "back-wall": {
                "width_scale": 0.9,
                "height_scale": 0.9,
                "top_left_x_factor": 0.575,
                "top_left_y_factor": 0.45,
                "top_right_x_factor": 0.75,
                "top_right_y_factor": 0.45,
                "bottom_left_x_factor": 0.575,
                "bottom_left_y_factor": 0.715,
                "bottom_right_x_factor": 0.75,
                "bottom_right_y_factor": 0.725,
                "perspective": True
            },
            
            "side-wall-left": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.25,
                "top_left_y_factor": 0.65,
                "top_right_x_factor": 0.425,
                "top_right_y_factor": 0.635,
                "bottom_left_x_factor": 0.25,
                "bottom_left_y_factor": 0.85,
                "bottom_right_x_factor": 0.425,
                "bottom_right_y_factor": 0.835,
                "perspective": True
            },
            
            "side-wall-right": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.61,
                "top_left_y_factor": 0.675,
                "top_right_x_factor": 0.785,
                "top_right_y_factor": 0.66,
                "bottom_left_x_factor": 0.61,
                "bottom_left_y_factor": 0.875,
                "bottom_right_x_factor": 0.785,
                "bottom_right_y_factor": 0.86,
                "perspective": True
            },
            
            "left-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.41,
                "top_left_y_factor": 0.115,
                "top_right_x_factor": 0.51,
                "top_right_y_factor": 0.105,
                "bottom_left_x_factor": 0.36,
                "bottom_left_y_factor": 0.315,
                "bottom_right_x_factor": 0.46,
                "bottom_right_y_factor": 0.305,
                "perspective": True
            },
            
            "right-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.51,
                "top_left_y_factor": 0.1,
                "top_right_x_factor": 0.61,
                "top_right_y_factor": 0.11,
                "bottom_left_x_factor": 0.575,
                "bottom_left_y_factor": 0.3,
                "bottom_right_x_factor": 0.675,
                "bottom_right_y_factor": 0.31,
                "perspective": True
            },
            
            "text-right": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.54,
                "top_left_y_factor": 0.295,
                "top_right_x_factor": 0.85,
                "top_right_y_factor": 0.315,
                "bottom_left_x_factor": 0.54,
                "bottom_left_y_factor": 0.35,
                "bottom_right_x_factor": 0.85,
                "bottom_right_y_factor": 0.36,
                "perspective": True
            },
            
            "text-left": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.16,
                "top_left_y_factor": 0.32,
                "top_right_x_factor": 0.48,
                "top_right_y_factor": 0.3,
                "bottom_left_x_factor": 0.16,
                "bottom_left_y_factor": 0.36,
                "bottom_right_x_factor": 0.48,
                "bottom_right_y_factor": 0.35,
                "perspective": True
            },
            
        },
        
        "coordinates": {
            "slope-left": [(2040, 293), (656, 911), (2038, 809)],
            "slope-right": [(2040, 293), (2038, 809), (3374, 900)],
            "canopy-left": [(550, 910), (2046, 808), (2039, 1228), (546, 1277)],
            "canopy-right": [(2044, 810), (3525, 909), (3530, 1278), (2039, 1228)],
            "back-wall": [(2074, 1295), (3461, 1260), (3467, 2010), (2072, 2070)],
            "left-side-wall": [(608, 2006), (2012, 1960), (2012, 2648), (600, 2776)],
            "right-side-wall": [(2072, 2069), (3484, 2009), (3480, 2780), (2069, 2947)]
        },
        
        "masks": {
            "1": (604, 2058, 653, 2106),
            "2": (594, 2671, 652, 2718),
            "3": (1988, 2008, 2018, 2051),
            "4": (1986, 2556, 2018, 2598),
            "5": (2009, 2122, 2120, 2176),
            "6": (3452, 2060, 3504, 2107), 
            "7": (3453, 2677, 3497, 2725),
            "8": (2068, 2825, 2121, 2879), 
            "9": (3424, 1932, 3477, 1981),
            "10": (2007, 1982, 2080, 2035),
            "11": (2032, 1898, 2083, 1938),
        }
    
    },
    
    "wall-block": {
        
        "logos": {
            
            "back-wall": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.5,
                "top_left_y_factor": 0.45,
                "top_right_x_factor": 0.5675,
                "top_right_y_factor": 0.45,
                "bottom_left_x_factor": 0.5,
                "bottom_left_y_factor": 0.65,
                "bottom_right_x_factor": 0.5675,
                "bottom_right_y_factor": 0.65,
                "perspective": True,
                "crop_type": "vertical"
            },
            
            "side-wall": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.61,
                "top_left_y_factor": 0.425,
                "top_right_x_factor": 0.8,
                "top_right_y_factor": 0.455,
                "bottom_left_x_factor": 0.61,
                "bottom_left_y_factor": 0.655,
                "bottom_right_x_factor": 0.8,
                "bottom_right_y_factor": 0.635,
                "perspective": True
            },
            
            "left-slope": {
                "width_scale": 0.3,
                "height_scale": 0.3,
                "top_left_x_factor": 0.465,
                "top_left_y_factor": 0.14,
                "top_right_x_factor": 0.525,
                "top_right_y_factor": 0.125,
                "bottom_left_x_factor": 0.405,
                "bottom_left_y_factor": 0.31,
                "bottom_right_x_factor": 0.505,
                "bottom_right_y_factor": 0.29,
                "perspective": True
            },
            
            "right-slope": {
                "width_scale": 0.4,
                "height_scale": 0.4,
                "top_left_x_factor": 0.555,
                "top_left_y_factor": 0.15,
                "top_right_x_factor": 0.595,
                "top_right_y_factor": 0.17,
                "bottom_left_x_factor": 0.58,
                "bottom_left_y_factor": 0.345,
                "bottom_right_x_factor": 0.67,
                "bottom_right_y_factor": 0.3,
                "perspective": True
            },
            
            "text-right": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.6,
                "top_left_y_factor": 0.26,
                "top_right_x_factor": 0.82,
                "top_right_y_factor": 0.33,
                "bottom_left_x_factor": 0.6,
                "bottom_left_y_factor": 0.31,
                "bottom_right_x_factor": 0.82,
                "bottom_right_y_factor": 0.365,
                "perspective": True
            },
            
            "text-left": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.21,
                "top_left_y_factor": 0.32,
                "top_right_x_factor": 0.535,
                "top_right_y_factor": 0.26,
                "bottom_left_x_factor": 0.21,
                "bottom_left_y_factor": 0.355,
                "bottom_right_x_factor": 0.535,
                "bottom_right_y_factor": 0.305,
                "perspective": True
            },
        
        },
        
        "coordinates": {
            "slope": [(1815, 296), (970, 709), (2486, 683)],
            "canopy-left": [(659, 749), (2023, 573), (2028, 807), (658, 938)],
            "canopy-right": [(2023, 573), (2903, 785), (2908, 962), (2028, 810)],
            "side-wall": [(2022, 808), (2857, 955), (2862, 1812), (2024, 1982)],
            "back-wall": [(1718, 1020), (1987, 1005), (1986, 1740), (1716, 1726)],
        },
        
        "masks": {
            "1": (1714, 1106, 1733, 1130),
            "2": (1712, 1647, 1733, 1671),
            "3": (2017, 1813, 2030, 1858),
            "4": (2015, 1810, 2035, 1850),
            "5": (2017, 810, 2031, 856),
            "6": (2010, 898, 2030, 939)
        }
    },
    
    "wall-pillar": {
        
        "logos": {
            
            "back-wall": {
                "width_scale": 0.9,
                "height_scale": 0.9,
                "top_left_x_factor": 0.535,
                "top_left_y_factor": 0.445,
                "top_right_x_factor": 0.75,
                "top_right_y_factor": 0.44,
                "bottom_left_x_factor": 0.535,
                "bottom_left_y_factor": 0.675,
                "bottom_right_x_factor": 0.75,
                "bottom_right_y_factor": 0.695,
                "perspective": True
            },
            
            "side-wall": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.21,
                "top_left_y_factor": 0.44,
                "top_right_x_factor": 0.425,
                "top_right_y_factor": 0.455,
                "bottom_left_x_factor": 0.21,
                "bottom_left_y_factor": 0.695,
                "bottom_right_x_factor": 0.425,
                "bottom_right_y_factor": 0.67,
                "perspective": True
            },
            
            "left-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.4,
                "top_left_y_factor": 0.155,
                "top_right_x_factor": 0.525,
                "top_right_y_factor": 0.13,
                "bottom_left_x_factor": 0.325,
                "bottom_left_y_factor": 0.255,
                "bottom_right_x_factor": 0.525,
                "bottom_right_y_factor": 0.235,
                "perspective": True
            },
            
            "right-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.575,
                "top_left_y_factor": 0.13,
                "top_right_x_factor": 0.64,
                "top_right_y_factor": 0.155,
                "bottom_left_x_factor": 0.595,
                "bottom_left_y_factor": 0.255,
                "bottom_right_x_factor": 0.71,
                "bottom_right_y_factor": 0.25,
                "perspective": True
            },
            
            "text-right": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.64,
                "top_left_y_factor": 0.25,
                "top_right_x_factor": 0.83,
                "top_right_y_factor": 0.3,
                "bottom_left_x_factor": 0.64,
                "bottom_left_y_factor": 0.31,
                "bottom_right_x_factor": 0.83,
                "bottom_right_y_factor": 0.34,
                "perspective": True
            },
            
            "text-left": {
                "width_scale": 0.7,
                "height_scale": 0.7,
                "top_left_x_factor": 0.2,
                "top_left_y_factor": 0.285,
                "top_right_x_factor": 0.535,
                "top_right_y_factor": 0.25,
                "bottom_left_x_factor": 0.2,
                "bottom_left_y_factor": 0.335,
                "bottom_right_x_factor": 0.535,
                "bottom_right_y_factor": 0.31,
                "perspective": True
            },
        
        },
        
        "coordinates": {
            "left-slope": [(2063, 252), (770, 803), (2370, 656)],
            "right-slope": [(2063, 250), (2370, 656), (3192, 825)],
            "left-canopy": [(631, 806), (2404, 654), (2409, 1072), (624, 1168)],
            "right-canopy": [(2404, 656), (3411, 866), (3416, 1206), (2409, 1072)],
            "left-wall": [(680, 1150), (1820, 1250), (1815, 2502), (676, 2657)],
            "right-wall": [(1846, 1250), (3349, 1190), (3364, 2602), (1849, 2502)]
        },
        
        "masks": {
            "1": (668, 1177, 688, 1224),
            "2": (675, 1764, 720, 1810),
            "3": (673, 2604, 718, 2653),
            "4": (1795, 1760, 1851, 1798),
            "5": (1819, 1802, 1881, 1840),
            "6": (1793, 2409, 1841, 2448),
            "7": (1815, 2458, 1881, 2496),
            "8": (3341, 1763, 3376, 1806),
            "9": (3318, 1810, 3381, 1854),
            "10": (3344, 2496, 3385, 2542),
            "11": (2371, 1220, 2430, 2544),
            "12": (3319, 2548, 3381, 2594)
        }
    },
    
    "no-walls": {
        
        "logos": {
            
            "left-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.43,
                "top_left_y_factor": 0.18,
                "top_right_x_factor": 0.53,
                "top_right_y_factor": 0.16,
                "bottom_left_x_factor": 0.375,
                "bottom_left_y_factor": 0.305,
                "bottom_right_x_factor": 0.475,
                "bottom_right_y_factor": 0.3,
                "perspective": True
            },
            
            "right-slope": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.525,
                "top_left_y_factor": 0.16,
                "top_right_x_factor": 0.61,
                "top_right_y_factor": 0.18,
                "bottom_left_x_factor": 0.59,
                "bottom_left_y_factor": 0.3,
                "bottom_right_x_factor": 0.675,
                "bottom_right_y_factor": 0.305,
                "perspective": True
            },
            
            "text-left": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.19,
                "top_left_y_factor": 0.325,
                "top_right_x_factor": 0.49,
                "top_right_y_factor": 0.3,
                "bottom_left_x_factor": 0.19,
                "bottom_left_y_factor": 0.375,
                "bottom_right_x_factor": 0.49,
                "bottom_right_y_factor": 0.37,
                "perspective": True
            },
            
            "text-right": {
                "width_scale": 0.5,
                "height_scale": 0.5,
                "top_left_x_factor": 0.6,
                "top_left_y_factor": 0.3,
                "top_right_x_factor": 0.84,
                "top_right_y_factor": 0.32,
                "bottom_left_x_factor": 0.6,
                "bottom_left_y_factor": 0.37,
                "bottom_right_x_factor": 0.84,
                "bottom_right_y_factor": 0.37,
                "perspective": True
            },
            
        },
        
        "coordinates": {
            "left-slope-top": [(521, 170), (417, 230), (527, 228)],
            "left-slope-bottom-1": [(416, 237), (526, 226), (541, 292), (156, 321)],
            "left-slope-bottom-2": [(428, 223), (502, 222), (490, 264), (337, 263)],
            "right-slope-top": [(523, 170), (531, 233), (662, 256)],
            "right-slope-bottom-1": [(531, 233), (690, 271), (871, 319), (543, 291)],
            "right-slope-bottom-2": [(529, 223), (606, 222), (752, 290), (540, 266)],
            "canopy-left": [(158, 322), (542, 294), (542, 374), (157, 376)],
            "canopy-right": [(545, 293), (873, 321), (873, 374), (545, 374)]
        },
        
        "masks": {},
        
    },
    
    "top-view": {
        
        "logos": {
            
            "slope-bottom": {
                "width_scale": 0.15,
                "height_scale": 0.15,
                "top_y_factor": 0.575,
                "left_x_factor": 0.5
            },
            
            "slope-left": {
                "width_scale": 0.15,
                "height_scale": 0.15,
                "top_y_factor": 0.37,
                "left_x_factor": 0.28,
                "rotation_angle": 270
            },
            
            "slope-top": {
                "width_scale": 0.15,
                "height_scale": 0.15,
                "top_y_factor": 0.15,
                "left_x_factor": 0.5,
                "rotation_angle": 180
            },
            
            "slope-right": {
                "width_scale": 0.15,
                "height_scale": 0.15,
                "top_y_factor": 0.37,
                "left_x_factor": 0.73,
                "rotation_angle": 90
            },
            
            "text-bottom": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_y_factor": 0.84,
                "left_x_factor": 0.5
            },
            
            "text-left": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_y_factor": 0.25,
                "left_x_factor": 0.13,
                "rotation_angle": 270
            },
            
            "text-top": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_y_factor": 0.1,
                "left_x_factor": 0.5,
                "rotation_angle": 180
            },
            
            "text-right": {
                "width_scale": 0.25,
                "height_scale": 0.25,
                "top_y_factor": 0.25,
                "left_x_factor": 0.87,
                "rotation_angle": 90
            },
                
        },
        
        "coordinates": {
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
