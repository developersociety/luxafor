"""
Constants shared across the module
"""
USB_ID_VENDOR = 0x04D8
USB_ID_PRODUCT = 0xF372

MODE_COLOUR = 1
MODE_FADE = 2
MODE_STROBE = 3
MODE_WAVE = 4
MODE_DEMO = 6

MODES = (MODE_COLOUR, MODE_FADE, MODE_STROBE, MODE_WAVE, MODE_DEMO)

PATTERN_WAVE_SINGLE_SMALL = 1
PATTERN_WAVE_SINGLE_LARGE = 2
PATTERN_WAVE_DOUBLE_SMALL = 3
PATTERN_WAVE_DOUBLE_LARGE = 4
PATTERN_WAVES = (
    PATTERN_WAVE_SINGLE_SMALL,
    PATTERN_WAVE_SINGLE_LARGE,
    PATTERN_WAVE_DOUBLE_SMALL,
    PATTERN_WAVE_DOUBLE_LARGE,
)

PATTERN_DEMO_LUXAFOR = 1
PATTERN_DEMO_RANDOM1 = 2
PATTERN_DEMO_RANDOM2 = 3
PATTERN_DEMO_RANDOM3 = 4
PATTERN_DEMO_POLICE = 5
PATTERN_DEMO_RANDOM4 = 6
PATTERN_DEMO_RANDOM5 = 7
PATTERN_DEMO_RAINBOWWAVE = 8
PATTERN_DEMOS = (
    PATTERN_DEMO_LUXAFOR,
    PATTERN_DEMO_RANDOM1,
    PATTERN_DEMO_RANDOM2,
    PATTERN_DEMO_RANDOM3,
    PATTERN_DEMO_POLICE,
    PATTERN_DEMO_RANDOM4,
    PATTERN_DEMO_RANDOM5,
    PATTERN_DEMO_RAINBOWWAVE,
)

LED_FLAG_BOTTOM = 1
LED_FLAG_MIDDLE = 2
LED_FLAG_TOP = 3
LED_POLE_BOTTOM = 4
LED_POLE_MIDDLE = 5
LED_POLE_TOP = 6

LED_FLAG_ALL = 65
LED_POLE_ALL = 66
LED_ALL = 255

LED_FLAGS = (LED_FLAG_BOTTOM, LED_FLAG_MIDDLE, LED_FLAG_TOP)
LED_POLES = (LED_POLE_BOTTOM, LED_POLE_MIDDLE, LED_POLE_TOP)
LEDS = LED_FLAGS + LED_POLES

LED_ALL_OPTIONS = (
    LED_ALL, LED_FLAG_ALL, LED_POLE_ALL,
    LED_FLAG_BOTTOM, LED_FLAG_MIDDLE, LED_FLAG_TOP,
    LED_POLE_BOTTOM, LED_POLE_MIDDLE, LED_POLE_TOP,
)

COLOUR_WHITE = (255, 255, 255)
COLOUR_NONE = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_GREEN = (0, 255, 0)
