from flask import Flask, render_template, abort


app = Flask(__name__, static_folder="static", template_folder="templates")

projects = [
    {
        "name": "Learn vi by playing classic video games",
        "thumb": "img/vipleT.png",
        "hero": "img/viple.png",
        "categories": ["Go", "WebAsm" "Ebiten"],
        "slug": "viple",
        "prod": "https://johncrane.dev/viple/viple_play.html",
        "repository": "https://github.com/wearsunscreen/viple",
    },
    {
        "name": "Flask Portfolio",
        "thumb": "img/portfolioT.png",
        "hero": "img/portfolio.png",
        "categories": ["Python", "Flask" "CSS"],
        "slug": "portfolio",
        "prod": "https://johncrane.dev/",
        "repository": "https://github.com/wearsunscreen/portfolio-flask",
    },
    {
        "name": "Flying Lines",
        "thumb": "img/linesT.png",
        "hero": "img/lines.png",
        "categories": ["Elm", "SVG", "Web"],
        "prod": "https://johncrane.dev/lines.html",
        "slug": "lines",
        "repository": "https://gitlab.com/johncrane/gengarden-lines",
    },
    {
        "name": "Perfect Flood",
        "thumb": "img/floodT.png",
        "hero": "img/flood.png",
        "categories": ["Elm", "Web", "GameDev"],
        "slug": "flood",
        "prod": "https://johncrane.dev/flood/flood.html",
        "repository": "https://gitlab.com/johncrane/perfect-flood",
    },
    {
        "name": "Portmanteau Quiz",
        "thumb": "img/portmanteauT.png",
        "hero": "img/portmanteau.png",
        "categories": ["Elm", "Web", "GameDev"],
        "prod": "https://johncrane.dev/portmanteau/portmanteau.html",
        "slug": "portmanteau",
        "repository": "https://github.com/wearsunscreen/Portmanteau",
    },
    {
        "name": "What Year Was It?",
        "thumb": "img/yearT.png",
        "hero": "img/year.png",
        "categories": ["Elm", "Web", "GameDev"],
        "prod": "https://johncrane.dev/yearof.html",
        "slug": "api-docs",
        "repository": "https://github.com/wearsunscreen/Year-Of-Quiz",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
