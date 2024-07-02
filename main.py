from flask import Flask, render_template, request
from configs.pages import (form_title,about_page_title,projectSections)
from configs.site import (pageTitle, site_config ,projectDescription, navItems, socialLinks,copyright_year)
from configs.themes import (themes, theme_config)
from configs.inputs import inputsConfig
app = Flask(__name__)

@app.route("/")
def home_page():
    theme = request.args.get('theme', theme_config['default_theme'])
    if theme not in theme_config['available_themes']:
        theme = theme_config['default_theme']
    return render_template("home_page.html", 
                           inputs=inputsConfig, 
                           title=pageTitle, 
                           description=projectDescription, 
                           nav_items=navItems, 
                           social_links=socialLinks,
                           themes=themes,
                           theme_config=theme_config,
                           site_config=site_config,
                           current_theme=theme,form_title=form_title,copyright_year=copyright_year)

if(site_config["show_about_page"]):
    @app.route("/about")
    def about_project():
        if not site_config["show_about_page"]:
            return "Page not found", 404
        theme = request.args.get('theme', theme_config['default_theme'])
        if theme not in theme_config['available_themes']:
            theme = theme_config['default_theme']
        return render_template("about_project.html", 
                            title=pageTitle, 
                            description=projectDescription, 
                            nav_items=navItems, 
                            social_links=socialLinks, 
                            project_sections=projectSections,
                            themes=themes,
                            theme_config=theme_config,
                            site_config=site_config,
                            current_theme=theme,copyright_year=copyright_year,about_page_title=about_page_title)

if __name__ == "__main__":
    app.run(debug=True)