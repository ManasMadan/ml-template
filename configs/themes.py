theme_config = {
    "use_theme_switcher": True,  # Set to False to use a single theme
    "default_theme": "default",
    "available_themes": ["default", "dark", "light", "colorful"]
}

themes = {
    "default": {
        "name": "Default",
        "colors": {
            "primary": "#26a69a",
            "secondary": "#4db6ac",
            "background": "#ffffff",
            "text": "#000000",
            "link": "#00897b"
        }
    },
    "dark": {
        "name": "Dark",
        "colors": {
            "primary": "#37474f",
            "secondary": "#546e7a",
            "background": "#263238",
            "text": "#ffffff",
            "link": "#80cbc4"
        }
    },
    "light": {
        "name": "Light",
        "colors": {
            "primary": "#90a4ae",
            "secondary": "#b0bec5",
            "background": "#eceff1",
            "text": "#37474f",
            "link": "#00796b"
        }
    },
    "colorful": {
        "name": "Colorful",
        "colors": {
            "primary": "#ff4081",
            "secondary": "#ff80ab",
            "background": "#f3e5f5",
            "text": "#4a148c",
            "link": "#7b1fa2"
        }
    }
}