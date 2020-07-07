import os
import webbrowser

import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape

from models import Solutions, SolutionsArray, Tasks

# pewee -> jinja2 -> (pdfkit, wkhtmltopdf)
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html"]),
)

pwd = os.getcwd()

solutions_array = SolutionsArray(Solutions.select().dicts())
tasks = Tasks.select()


def render_task(task):
    return env.get_template("one.html").render(
        task=task, solutions=solutions_array[task.id], pwd=pwd
    )


def render_tasks(tasks):
    return env.get_template("all.html").render(
        tasks=tasks, solutions_array=solutions_array, pwd=pwd
    )


tasks = [task for task in Tasks.select()][:100]
print(tasks)

options = {
    "page-size": "Letter",
    "no-outline": None,
    "javascript-delay": 2 * len(tasks) * 1000,
}
# html = render_tasks(tasks)
# pdfkit.from_string(html, 'out.pdf',  options=options)
