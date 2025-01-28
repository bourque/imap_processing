"""
Contains constants variables to support CoDICE processing.

The ``plan_id``, ``plan_step``, and ``view_id`` mentioned in this module are
derived from the packet data.

Notes
-----
SW = SunWard
NSW = Non-SunWard
PUI = PickUp Ion
ESA = ElectroStatic Analyzer
"""

# TODO: What to do in the case of a value of 255 in LOSSY_A and LOSSY_B
#       compression? (Joey uses 0x100000000)

from imap_processing.codice.utils import CODICEAPID, CoDICECompression

APIDS_FOR_SCIENCE_PROCESSING = [
    CODICEAPID.COD_HI_INST_COUNTS_AGGREGATED,
    CODICEAPID.COD_HI_INST_COUNTS_SINGLES,
    CODICEAPID.COD_HI_OMNI_SPECIES_COUNTS,
    CODICEAPID.COD_HI_SECT_SPECIES_COUNTS,
    CODICEAPID.COD_LO_INST_COUNTS_AGGREGATED,
    CODICEAPID.COD_LO_INST_COUNTS_SINGLES,
    CODICEAPID.COD_LO_SW_ANGULAR_COUNTS,
    CODICEAPID.COD_LO_NSW_ANGULAR_COUNTS,
    CODICEAPID.COD_LO_SW_PRIORITY_COUNTS,
    CODICEAPID.COD_LO_NSW_PRIORITY_COUNTS,
    CODICEAPID.COD_LO_SW_SPECIES_COUNTS,
    CODICEAPID.COD_LO_NSW_SPECIES_COUNTS,
]


# CDF-friendly names for lo data products
LO_INST_COUNTS_AGGREGATED_VARIABLE_NAMES = ["aggregated"]
LO_INST_COUNTS_SINGLES_VARIABLE_NAMES = ["apd_singles"]
LO_SW_ANGULAR_VARIABLE_NAMES = ["hplus", "heplusplus", "oplus6", "fe_loq"]
LO_NSW_ANGULAR_VARIABLE_NAMES = ["heplusplus"]
LO_SW_PRIORITY_VARIABLE_NAMES = [
    "p0_tcrs",
    "p1_hplus",
    "p2_heplusplus",
    "p3_heavies",
    "p4_dcrs",
]
LO_NSW_PRIORITY_VARIABLE_NAMES = ["p5_heavies", "p6_hplus_heplusplus"]
LO_SW_SPECIES_VARIABLE_NAMES = [
    "hplus",
    "heplusplus",
    "cplus4",
    "cplus5",
    "cplus6",
    "oplus5",
    "oplus6",
    "oplus7",
    "oplus8",
    "ne",
    "mg",
    "si",
    "fe_loq",
    "fe_hiq",
    "heplus",
    "cnoplus",
]
LO_NSW_SPECIES_VARIABLE_NAMES = [
    "hplus",
    "heplusplus",
    "c",
    "o",
    "ne_si_mg",
    "fe",
    "heplus",
    "cnoplus",
]

# CDF-friendly names for hi data products
HI_INST_COUNTS_AGGREGATED_VARIABLE_NAMES = ["aggregated"]
HI_INST_COUNTS_SINGLES_VARIABLE_NAMES = ["tcr", "ssdo", "stssd"]
HI_OMNI_SPECIES_VARIABLE_NAMES = ["h", "he3", "he4", "c", "o", "ne_mg_si", "fe", "uh"]
HI_SECT_SPECIES_VARIABLE_NAMES = ["h", "he3he4", "cno", "fe"]

# TODO: Hi products shape should be energy x ssd index x spin sector (8*12*12)
DATA_PRODUCT_CONFIGURATIONS = {
    CODICEAPID.COD_HI_INST_COUNTS_AGGREGATED: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_hi-counters-aggregated",
        "dims": [
            "epoch",
            "esa_step",
            "inst_az",
            "spin_sector",
        ],  # TODO: These will likely change
        "instrument": "hi",
        "num_counters": 1,
        "num_energy_steps": 1,  # TODO: Double check with Joey
        "num_positions": 6,  # TODO: Double check with Joey
        "num_spin_sectors": 1,
        "support_variables": [],  # TODO: Double check with Joey
        "variable_names": HI_INST_COUNTS_AGGREGATED_VARIABLE_NAMES,
    },
    CODICEAPID.COD_HI_INST_COUNTS_SINGLES: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_hi-counters-singles",
        "dims": [
            "epoch",
            "esa_step",
            "inst_az",
            "spin_sector",
        ],  # TODO: These will likely change
        "instrument": "hi",
        "num_counters": 3,
        "num_energy_steps": 1,  # TODO: Double check with Joey
        "num_positions": 12,  # TODO: Double check with Joey
        "num_spin_sectors": 1,
        "support_variables": [],  # No support variables for this one
        "variable_names": HI_INST_COUNTS_SINGLES_VARIABLE_NAMES,
    },
    CODICEAPID.COD_HI_OMNI_SPECIES_COUNTS: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_hi-omni",
        "dims": [
            "epoch",
            "esa_step",
            "inst_az",
            "spin_sector",
        ],  # TODO: These will likely change
        "instrument": "hi",
        "num_counters": 8,
        "num_energy_steps": 15,  # TODO: Double check with Joey
        "num_positions": 4,  # TODO: Double check with Joey
        "num_spin_sectors": 1,
        "support_variables": ["data_quality", "spin_period"],
        "variable_names": HI_OMNI_SPECIES_VARIABLE_NAMES,
    },
    CODICEAPID.COD_HI_SECT_SPECIES_COUNTS: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_hi-sectored",
        "dims": [
            "epoch",
            "esa_step",
            "inst_az",
            "spin_sector",
        ],  # TODO: These will likely change
        "instrument": "hi",
        "num_counters": 4,
        "num_energy_steps": 8,
        "num_positions": 12,
        "num_spin_sectors": 12,
        "support_variables": ["data_quality", "spin_period"],
        "variable_names": HI_SECT_SPECIES_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_INST_COUNTS_AGGREGATED: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_lo-counters-aggregated",
        "dims": ["epoch", "esa_step", "inst_az", "spin_sector"],
        "instrument": "lo",
        "num_counters": 1,
        "num_energy_steps": 128,
        "num_positions": 6,
        "num_spin_sectors": 6,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
        ],  # TODO: Double check with Joey
        "variable_names": LO_INST_COUNTS_AGGREGATED_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_INST_COUNTS_SINGLES: {
        "coords": [
            "epoch",
            "inst_az",
            "spin_sector",
            "esa_step",
            "energy_label",
        ],  # TODO: These will likely change
        "dataset_name": "imap_codice_l1a_lo-counters-singles",
        "dims": ["epoch", "esa_step", "inst_az", "spin_sector"],
        "instrument": "lo",
        "num_counters": 1,
        "num_energy_steps": 128,
        "num_positions": 24,
        "num_spin_sectors": 6,
        "support_variables": [
            "spin_sector_pairs",
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_INST_COUNTS_SINGLES_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_SW_ANGULAR_COUNTS: {
        "coords": ["epoch", "inst_az", "spin_sector", "esa_step"],
        "dataset_name": "imap_codice_l1a_lo-sw-angular",
        "dims": ["epoch", "inst_az", "spin_sector", "esa_step"],
        "instrument": "lo",
        "num_counters": 4,
        "num_energy_steps": 128,
        "num_positions": 5,
        "num_spin_sectors": 12,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_SW_ANGULAR_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_NSW_ANGULAR_COUNTS: {
        "coords": ["epoch", "inst_az", "spin_sector", "esa_step"],
        "dataset_name": "imap_codice_l1a_lo-nsw-angular",
        "dims": ["epoch", "inst_az", "spin_sector", "esa_step"],
        "instrument": "lo",
        "num_counters": 1,
        "num_energy_steps": 128,
        "num_positions": 19,
        "num_spin_sectors": 12,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_NSW_ANGULAR_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_SW_PRIORITY_COUNTS: {
        "coords": ["epoch", "inst_az", "spin_sector", "esa_step", "energy_label"],
        "dataset_name": "imap_codice_l1a_lo-sw-priority",
        "dims": ["epoch", "esa_step", "inst_az", "spin_sector"],
        "instrument": "lo",
        "num_counters": 5,
        "num_energy_steps": 128,
        "num_positions": 1,
        "num_spin_sectors": 12,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_SW_PRIORITY_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_NSW_PRIORITY_COUNTS: {
        "coords": ["epoch", "inst_az", "spin_sector", "esa_step", "energy_label"],
        "dataset_name": "imap_codice_l1a_lo-nsw-priority",
        "dims": ["epoch", "esa_step", "inst_az", "spin_sector"],
        "instrument": "lo",
        "num_counters": 2,
        "num_energy_steps": 128,
        "num_positions": 1,
        "num_spin_sectors": 12,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_NSW_PRIORITY_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_SW_SPECIES_COUNTS: {
        "coords": ["epoch", "inst_az", "esa_step"],
        "dataset_name": "imap_codice_l1a_lo-sw-species",
        "dims": ["epoch", "inst_az", "esa_step"],
        "instrument": "lo",
        "num_counters": 16,
        "num_energy_steps": 128,
        "num_positions": 1,
        "num_spin_sectors": 0,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_SW_SPECIES_VARIABLE_NAMES,
    },
    CODICEAPID.COD_LO_NSW_SPECIES_COUNTS: {
        "coords": ["epoch", "inst_az", "spin_sector", "esa_step", "energy_label"],
        "dataset_name": "imap_codice_l1a_lo-nsw-species",
        "dims": ["epoch", "esa_step", "inst_az", "spin_sector"],
        "instrument": "lo",
        "num_counters": 8,
        "num_energy_steps": 128,
        "num_positions": 1,
        "num_spin_sectors": 1,
        "support_variables": [
            "energy_table",
            "acquisition_time_per_step",
            "rgfo_half_spin",
            "nso_half_spin",
            "sw_bias_gain_mode",
            "st_bias_gain_mode",
            "data_quality",
            "spin_period",
        ],
        "variable_names": LO_NSW_SPECIES_VARIABLE_NAMES,
    },
}

# Compression ID lookup table for Lo data products
# The key is the view_id and the value is the ID for the compression algorithm
# (see utils.CoDICECompression to see how the values correspond)
LO_COMPRESSION_ID_LOOKUP = {
    0: CoDICECompression.LOSSY_A_LOSSLESS,
    1: CoDICECompression.LOSSY_B_LOSSLESS,
    2: CoDICECompression.LOSSY_B_LOSSLESS,
    3: CoDICECompression.LOSSY_A_LOSSLESS,
    4: CoDICECompression.LOSSY_A_LOSSLESS,
    5: CoDICECompression.LOSSY_A_LOSSLESS,
    6: CoDICECompression.LOSSY_A_LOSSLESS,
    7: CoDICECompression.LOSSY_A_LOSSLESS,
    8: CoDICECompression.LOSSY_A_LOSSLESS,
}

# Compression ID lookup table for Hi data products
# The key is the view_id and the value is the ID for the compression algorithm
# (see utils.CoDICECompression to see how the values correspond)
HI_COMPRESSION_ID_LOOKUP = {
    0: CoDICECompression.LOSSY_A,
    1: CoDICECompression.LOSSY_A,
    2: CoDICECompression.LOSSY_A,
    3: CoDICECompression.LOSSY_B_LOSSLESS,
    4: CoDICECompression.LOSSY_B_LOSSLESS,
    5: CoDICECompression.LOSSY_A_LOSSLESS,
    6: CoDICECompression.LOSSY_A_LOSSLESS,
    7: CoDICECompression.LOSSY_A_LOSSLESS,
    8: CoDICECompression.LOSSY_A_LOSSLESS,
    9: CoDICECompression.LOSSY_A_LOSSLESS,
}

# ESA Sweep table ID lookup table
# The combination of plan_id and plan_step determine the ESA sweep Table to use
# Currently, ESA sweep table 0 is used for every plan_id/plan_step combination,
# but may change in the future. These values are provided in the SCI-LUT excel
# spreadsheet
ESA_SWEEP_TABLE_ID_LOOKUP = {
    (0, 0): 0,
    (0, 1): 0,
    (0, 2): 0,
    (0, 3): 0,
    (1, 0): 0,
    (1, 1): 0,
    (1, 2): 0,
    (1, 3): 0,
    (2, 0): 0,
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 0,
    (3, 0): 0,
    (3, 1): 0,
    (3, 2): 0,
    (3, 3): 0,
    (4, 0): 0,
    (4, 1): 0,
    (4, 2): 0,
    (4, 3): 0,
    (5, 0): 0,
    (5, 1): 0,
    (5, 2): 0,
    (5, 3): 0,
    (6, 0): 0,
    (6, 1): 0,
    (6, 2): 0,
    (6, 3): 0,
    (7, 0): 0,
    (7, 1): 0,
    (7, 2): 0,
    (7, 3): 0,
}

# Lo Stepping table ID lookup table
# The combination of plan_id and plan_step determine the Lo Stepping Table to
# use. Currently, LO Stepping table 0 is used for every plan_id/plan_step
# combination, but may change in the future. These values are provided in the
# SCI-LUT excel spreadsheet
LO_STEPPING_TABLE_ID_LOOKUP = {
    (0, 0): 0,
    (0, 1): 0,
    (0, 2): 0,
    (0, 3): 0,
    (1, 0): 0,
    (1, 1): 0,
    (1, 2): 0,
    (1, 3): 0,
    (2, 0): 0,
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 0,
    (3, 0): 0,
    (3, 1): 0,
    (3, 2): 0,
    (3, 3): 0,
    (4, 0): 0,
    (4, 1): 0,
    (4, 2): 0,
    (4, 3): 0,
    (5, 0): 0,
    (5, 1): 0,
    (5, 2): 0,
    (5, 3): 0,
    (6, 0): 0,
    (6, 1): 0,
    (6, 2): 0,
    (6, 3): 0,
    (7, 0): 0,
    (7, 1): 0,
    (7, 2): 0,
    (7, 3): 0,
}

# Lookup tables for Lossy decompression algorithms "A" and "B"
# These were provided by Greg Dunn via his sohis_cdh_utils.v script and then
# transformed into python dictionaries. The values in these tables are subject
# to change, but the format is expected to stay the same.
LOSSY_A_TABLE = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    9: 10,
    10: 11,
    11: 12,
    12: 13,
    13: 14,
    14: 15,
    15: 16,
    16: 17,
    17: 18,
    18: 19,
    19: 20,
    20: 21,
    21: 22,
    22: 23,
    23: 24,
    24: 25,
    25: 26,
    26: 27,
    27: 28,
    28: 29,
    29: 30,
    30: 31,
    31: 32,
    32: 34,
    33: 36,
    34: 38,
    35: 40,
    36: 42,
    37: 44,
    38: 46,
    39: 48,
    40: 50,
    41: 52,
    42: 54,
    43: 56,
    44: 58,
    45: 60,
    46: 62,
    47: 64,
    48: 68,
    49: 72,
    50: 76,
    51: 80,
    52: 84,
    53: 88,
    54: 92,
    55: 96,
    56: 100,
    57: 104,
    58: 108,
    59: 112,
    60: 116,
    61: 120,
    62: 124,
    63: 128,
    64: 136,
    65: 144,
    66: 152,
    67: 160,
    68: 168,
    69: 176,
    70: 184,
    71: 192,
    72: 200,
    73: 208,
    74: 216,
    75: 224,
    76: 232,
    77: 240,
    78: 248,
    79: 256,
    80: 272,
    81: 288,
    82: 304,
    83: 320,
    84: 336,
    85: 352,
    86: 368,
    87: 384,
    88: 400,
    89: 416,
    90: 432,
    91: 448,
    92: 464,
    93: 480,
    94: 496,
    95: 512,
    96: 544,
    97: 576,
    98: 608,
    99: 640,
    100: 672,
    101: 704,
    102: 736,
    103: 768,
    104: 800,
    105: 832,
    106: 864,
    107: 896,
    108: 928,
    109: 960,
    110: 992,
    111: 1024,
    112: 1088,
    113: 1152,
    114: 1216,
    115: 1280,
    116: 1344,
    117: 1408,
    118: 1472,
    119: 1536,
    120: 1600,
    121: 1664,
    122: 1728,
    123: 1792,
    124: 1856,
    125: 1920,
    126: 1984,
    127: 2048,
    128: 2176,
    129: 2304,
    130: 2432,
    131: 2560,
    132: 2688,
    133: 2816,
    134: 2944,
    135: 3072,
    136: 3200,
    137: 3328,
    138: 3456,
    139: 3584,
    140: 3712,
    141: 3840,
    142: 3968,
    143: 4096,
    144: 4352,
    145: 4608,
    146: 4864,
    147: 5120,
    148: 5376,
    149: 5632,
    150: 5888,
    151: 6144,
    152: 6400,
    153: 6656,
    154: 6912,
    155: 7168,
    156: 7424,
    157: 7680,
    158: 7936,
    159: 8192,
    160: 8704,
    161: 9216,
    162: 9728,
    163: 10240,
    164: 10752,
    165: 11264,
    166: 11776,
    167: 12288,
    168: 12800,
    169: 13312,
    170: 13824,
    171: 14336,
    172: 14848,
    173: 15360,
    174: 15872,
    175: 16384,
    176: 17408,
    177: 18432,
    178: 19456,
    179: 20480,
    180: 21504,
    181: 22528,
    182: 23552,
    183: 24576,
    184: 25600,
    185: 26624,
    186: 27648,
    187: 28672,
    188: 29696,
    189: 30720,
    190: 31744,
    191: 32768,
    192: 34816,
    193: 36864,
    194: 38912,
    195: 40960,
    196: 43008,
    197: 45056,
    198: 47104,
    199: 49152,
    200: 51200,
    201: 53248,
    202: 55296,
    203: 57344,
    204: 59392,
    205: 61440,
    206: 63488,
    207: 65536,
    208: 69632,
    209: 73728,
    210: 77824,
    211: 81920,
    212: 86016,
    213: 90112,
    214: 94208,
    215: 98304,
    216: 102400,
    217: 106496,
    218: 110592,
    219: 114688,
    220: 118784,
    221: 122880,
    222: 126976,
    223: 131072,
    224: 139264,
    225: 147456,
    226: 155648,
    227: 163840,
    228: 172032,
    229: 180224,
    230: 188416,
    231: 196608,
    232: 204800,
    233: 212992,
    234: 221184,
    235: 229376,
    236: 237568,
    237: 245760,
    238: 253952,
    239: 262144,
    240: 278528,
    241: 294912,
    242: 311296,
    243: 327680,
    244: 344064,
    245: 360448,
    246: 376832,
    247: 393216,
    248: 409600,
    249: 425984,
    250: 442368,
    251: 458752,
    252: 475136,
    253: 491520,
    254: 507904,
    255: 999999,
}

LOSSY_B_TABLE = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    9: 10,
    10: 11,
    11: 12,
    12: 13,
    13: 14,
    14: 15,
    15: 16,
    16: 17,
    17: 18,
    18: 19,
    19: 20,
    20: 21,
    21: 22,
    22: 23,
    23: 24,
    24: 25,
    25: 26,
    26: 27,
    27: 28,
    28: 29,
    29: 30,
    30: 31,
    31: 32,
    32: 34,
    33: 36,
    34: 38,
    35: 40,
    36: 42,
    37: 44,
    38: 46,
    39: 48,
    40: 50,
    41: 52,
    42: 54,
    43: 56,
    44: 58,
    45: 60,
    46: 62,
    47: 64,
    48: 68,
    49: 72,
    50: 76,
    51: 80,
    52: 84,
    53: 88,
    54: 92,
    55: 96,
    56: 100,
    57: 104,
    58: 108,
    59: 112,
    60: 116,
    61: 120,
    62: 124,
    63: 128,
    64: 136,
    65: 144,
    66: 152,
    67: 160,
    68: 168,
    69: 176,
    70: 184,
    71: 192,
    72: 200,
    73: 208,
    74: 216,
    75: 224,
    76: 232,
    77: 240,
    78: 248,
    79: 256,
    80: 272,
    81: 288,
    82: 304,
    83: 320,
    84: 336,
    85: 352,
    86: 368,
    87: 384,
    88: 400,
    89: 416,
    90: 432,
    91: 448,
    92: 464,
    93: 480,
    94: 496,
    95: 512,
    96: 544,
    97: 576,
    98: 608,
    99: 640,
    100: 672,
    101: 704,
    102: 736,
    103: 768,
    104: 800,
    105: 832,
    106: 864,
    107: 896,
    108: 928,
    109: 960,
    110: 992,
    111: 1024,
    112: 1088,
    113: 1152,
    114: 1216,
    115: 1280,
    116: 1344,
    117: 1408,
    118: 1472,
    119: 1536,
    120: 1600,
    121: 1664,
    122: 1728,
    123: 1792,
    124: 1856,
    125: 1920,
    126: 1984,
    127: 2048,
    128: 2176,
    129: 2304,
    130: 2432,
    131: 2560,
    132: 2688,
    133: 2816,
    134: 2944,
    135: 3072,
    136: 3200,
    137: 3328,
    138: 3456,
    139: 3584,
    140: 3712,
    141: 3840,
    142: 3968,
    143: 4096,
    144: 4352,
    145: 4608,
    146: 4864,
    147: 5120,
    148: 5376,
    149: 5632,
    150: 5888,
    151: 6144,
    152: 6400,
    153: 6656,
    154: 6912,
    155: 7168,
    156: 7424,
    157: 7680,
    158: 7936,
    159: 8192,
    160: 8704,
    161: 9216,
    162: 9728,
    163: 10240,
    164: 10752,
    165: 11264,
    166: 11776,
    167: 12288,
    168: 12800,
    169: 13312,
    170: 13824,
    171: 14336,
    172: 14848,
    173: 15360,
    174: 15872,
    175: 16384,
    176: 17408,
    177: 18432,
    178: 19456,
    179: 20480,
    180: 21504,
    181: 22528,
    182: 23552,
    183: 24576,
    184: 25600,
    185: 26624,
    186: 27648,
    187: 28672,
    188: 29696,
    189: 30720,
    190: 31744,
    191: 32768,
    192: 36864,
    193: 40960,
    194: 45056,
    195: 49152,
    196: 53248,
    197: 57344,
    198: 61440,
    199: 65536,
    200: 73728,
    201: 81920,
    202: 90112,
    203: 98304,
    204: 106496,
    205: 114688,
    206: 122880,
    207: 131072,
    208: 147456,
    209: 163840,
    210: 180224,
    211: 196608,
    212: 212992,
    213: 229376,
    214: 245760,
    215: 262144,
    216: 294912,
    217: 327680,
    218: 360448,
    219: 393216,
    220: 425984,
    221: 458752,
    222: 491520,
    223: 524288,
    224: 589824,
    225: 655360,
    226: 720896,
    227: 786432,
    228: 851968,
    229: 917504,
    230: 983040,
    231: 1048576,
    232: 1179648,
    233: 1310720,
    234: 1441792,
    235: 1572864,
    236: 1703936,
    237: 1835008,
    238: 1966080,
    239: 2097152,
    240: 2359296,
    241: 2621440,
    242: 2883584,
    243: 3145728,
    244: 3407872,
    245: 3670016,
    246: 3932160,
    247: 4194304,
    248: 4718592,
    249: 5242880,
    250: 5767168,
    251: 6291456,
    252: 6815744,
    253: 7340032,
    254: 7864320,
    255: 9999999,
}
