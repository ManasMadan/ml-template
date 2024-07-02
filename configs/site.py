from utils import get_current_year

pageTitle = "Hello World"
projectDescription = "This is a Machine Learning application that processes user input to perform various tasks."

site_config = {
    "show_about_page": True,
    "show_nav": True,  
    "show_footer": True,
}
copyright_year=get_current_year()

navItems = [
    {"name": "Home", "url": "/"},
] + ([{"name": "About Project", "url": "/about"}] if site_config["show_about_page"] else [])

socialLinks = [
    {"name": "GitHub", "url": "https://github.com/yourusername"},
    {"name": "LinkedIn", "url": "https://linkedin.com/in/yourusername"},
    {"name": "Twitter", "url": "https://twitter.com/yourusername"},
]
