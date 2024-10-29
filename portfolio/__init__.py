from flask import Flask, render_template, abort


app = Flask(__name__, static_folder="static", template_folder="templates")

projects = [
    {
        "name": "Learn vi by playing classic video games",
        "thumb": "img/vipleT.png",
        "hero": "img/viple.png",
        "categories": ["Go", "WebAsm", "GameDev"],
        "slug": "viple",
        "prod": "https://johncrane.dev/viple/viple_play.html",
        "github": "https://github.com/wearsunscreen/viple"
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
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