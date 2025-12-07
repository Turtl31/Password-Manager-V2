currentTheme = {}

THEMES = {
    "blue": {
        "BG_MAIN": "#161A20",           # Main window background
        "BG_PANEL": "#1C2129",          # Side panels / detail panel
        "BG_LIST": "#181C24",           # List area behind cards
        "BG_CARD": "#222832",           # Individual list items / cards
        "BG_INPUT": "#2A303A",          # Search bar / entry fields
        "BG_BUTTON": "#2D3440",         # Neutral buttons
        "BG_BUTTON_ALT": "#3A4250",     # Secondary buttons (settings, logout, etc.)

        "FG_PRIMARY": "#E8ECF2",        # Main text
        "FG_SECONDARY": "#B9C0CC",      # Sub text
        "FG_MUTED": "#8691A2",          # Hints / helper text

        "ACCENT_BLUE": "#4A8CFF",       # Main accent (links, focus, primary actions)
        "ACCENT_BLUE_SOFT": "#3D6FD1",  # Softer accent (hover, subtle outlines)
        "ACCENT_BLUE_GLOW": "#66A3FF",  # Strong highlight / glow
    },

    "dark": {
        "BG_MAIN": "#1C1C1C",
        "BG_PANEL": "#222222",
        "BG_LIST": "#1A1A1A",
        "BG_CARD": "#2A2A2A",
        "BG_INPUT": "#333333",
        "BG_BUTTON": "#3A3A3A",
        "BG_BUTTON_ALT": "#4A4A4A",

        "FG_PRIMARY": "#FFFFFF",
        "FG_SECONDARY": "#CFCFCF",
        "FG_MUTED": "#9A9A9A",

        "ACCENT_BLUE": "#4A8CFF",
        "ACCENT_BLUE_SOFT": "#3D6FD1",
        "ACCENT_BLUE_GLOW": "#66A3FF",
    },

    "light": {
        "BG_MAIN": "#FFFFFF",
        "BG_PANEL": "#F3F3F3",
        "BG_LIST": "#F8F8F8",
        "BG_CARD": "#FFFFFF",
        "BG_INPUT": "#FFFFFF",
        "BG_BUTTON": "#E5E5E5",
        "BG_BUTTON_ALT": "#D5D5D5",

        "FG_PRIMARY": "#1A1A1A",
        "FG_SECONDARY": "#555555",
        "FG_MUTED": "#7A7A7A",

        "ACCENT_BLUE": "#4A8CFF",
        "ACCENT_BLUE_SOFT": "#3D6FD1",
        "ACCENT_BLUE_GLOW": "#66A3FF",
    }, 
    "red": {
        "BG_MAIN": "#201618",
        "BG_PANEL": "#261A1D",
        "BG_LIST": "#1A1113",
        "BG_CARD": "#2C1E21",
        "BG_INPUT": "#332327",
        "BG_BUTTON": "#3A272C",
        "BG_BUTTON_ALT": "#4A2F35",

        "FG_PRIMARY": "#F8E9EB",
        "FG_SECONDARY": "#D9C0C4",
        "FG_MUTED": "#A78A8F",

        "ACCENT_BLUE": "#4A8CFF",
        "ACCENT_BLUE_SOFT": "#3D6FD1",
        "ACCENT_BLUE_GLOW": "#66A3FF",
    },

    "purple": {
        "BG_MAIN": "#1D1623",
        "BG_PANEL": "#231A2B",
        "BG_LIST": "#18121F",
        "BG_CARD": "#2A1E37",
        "BG_INPUT": "#302242",
        "BG_BUTTON": "#37274A",
        "BG_BUTTON_ALT": "#432D5C",

        "FG_PRIMARY": "#EEE8F4",
        "FG_SECONDARY": "#CFC3D8",
        "FG_MUTED": "#9B8AA9",

        "ACCENT_BLUE": "#4A8CFF",
        "ACCENT_BLUE_SOFT": "#3D6FD1",
        "ACCENT_BLUE_GLOW": "#66A3FF",
    },

    "green": {
        "BG_MAIN": "#142017",
        "BG_PANEL": "#19261D",
        "BG_LIST": "#0F1A13",
        "BG_CARD": "#1E3323",
        "BG_INPUT": "#24402A",
        "BG_BUTTON": "#2A4A31",
        "BG_BUTTON_ALT": "#335A3C",

        "FG_PRIMARY": "#E4F2E7",
        "FG_SECONDARY": "#C1D9C7",
        "FG_MUTED": "#96B39C",

        "ACCENT_BLUE": "#4A8CFF",
        "ACCENT_BLUE_SOFT": "#3D6FD1",
        "ACCENT_BLUE_GLOW": "#66A3FF",
    },
}

def loadTheme(theme_name: str):
    global current_theme

    if theme_name not in THEMES:
        theme_name = "blue"
    return THEMES[theme_name]
