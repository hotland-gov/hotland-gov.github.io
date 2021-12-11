import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

SOURCES = Path.cwd() / "src"
OUTPUT = Path.cwd() / "public"

ENVIRONMENT = Environment(loader=FileSystemLoader(SOURCES))


def copy(path):
    file = path.relative_to(Path.cwd())
    output = OUTPUT / file

    shutil.copy(path, output)


def render(path, values=None):
    if values is None:
        values = {}

    file = str(path.relative_to(SOURCES))
    template = ENVIRONMENT.get_template(file)
    output = OUTPUT / file

    if not output.parent.exists():
        output.parent.mkdir(parents=True)

    output.write_text(template.render(**values))


if __name__ == "__main__":
    render(SOURCES / "index.html")
    render(SOURCES / "404.html")

    copy(Path.cwd() / ".nojekyll")
    copy(Path.cwd() / "favicon.ico")
    copy(Path.cwd() / "flag.png")
    copy(Path.cwd() / "index.css")
