import os
import shutil
from pathlib import Path

import click
import colorama


@click.group()
def cli():
    pass


APP_NAME_IDENTIFIER = "##app-name##"
SVELTE_APP_IDENTIFIER = "##svelte-app##"

library_path = Path(os.path.dirname(os.path.realpath(__file__)))


def touch_file(filename):
    with open(filename, "w") as f:
        f.write("")


def copy_file_with_replace(src, dest, replacements={}):
    with open(src, "r") as f:
        content = f.read()
    for key, value in replacements.items():
        content = content.replace(key, value)
    with open(dest, "w") as f:
        f.write(content)


@click.command()
@click.argument("name")
@click.pass_context
def create(ctx, name="project"):
    """
    Creates a new project with the given name.
    """
    print("Creating project...")

    # Creating the folder structure
    root_path = Path(os.getcwd()) / name
    flask_app_path = root_path / "app"
    templates_path = flask_app_path / "templates"
    svelte_path = flask_app_path / "static" / "svelte"
    svelte_apps_path = flask_app_path / "svelte"
    global_css_path = svelte_path / "global.css"

    for path in [
        root_path,
        flask_app_path,
        templates_path,
        svelte_path,
        svelte_apps_path,
    ]:
        path.mkdir(parents=True, exist_ok=True)

    # Creating the package.json file
    copy_file_with_replace(
        library_path / "data/sample-package.json",
        root_path / "package.json",
        {APP_NAME_IDENTIFIER: name},
    )

    # Copying rollup.config.js
    copy_file_with_replace(
        library_path / "data/sample-rollup.config.js",
        root_path / "rollup.config.js",
    )

    # Copying the tailwind.config.js
    copy_file_with_replace(
        library_path / "data/sample-tailwind.config.js",
        root_path / "tailwind.config.js",
    )

    # Creating sample flask app
    copy_file_with_replace(
        library_path / "data/sample-app.py",
        flask_app_path / "__init__.py",
    )
    touch_file(global_css_path)

    os.chdir(root_path)

    ctx.invoke(add_page, name="index")

    print()
    print("Your project is ready! Run: ")
    print(colorama.Fore.GREEN + "cd " + name)
    print("npm install")
    print("Then run `npm run dev` to start the development server.")
    print(colorama.Style.RESET_ALL)


@click.command()
@click.argument("name")
def add_page(name):
    """
    Adds a new page with the given name. Run this command from the root of the project.
    """
    # Creating the folder structure
    root_path = Path(os.getcwd())
    print("Root path:", root_path)
    flask_app_path = root_path / "app"
    templates_path = flask_app_path / "templates"
    static_path = flask_app_path / "static"
    svelte_path = flask_app_path / "svelte"
    app_dir = svelte_path / name
    html_file = templates_path / f"{name}.html"
    static_folder = static_path / "svelte" / name

    for path in [static_folder]:
        path.mkdir(parents=True, exist_ok=True)

    # Copying sample app
    shutil.copytree(
        library_path / "data/svelte-app",
        app_dir,
    )

    # Copying sample html file
    copy_file_with_replace(
        library_path / "data/template.html",
        html_file,
        {SVELTE_APP_IDENTIFIER: name},
    )

    # Updating rollup.config.js
    update_rollup_config(name, root_path / "rollup.config.js")
    print(f"Added page: {name}!")


def update_rollup_config(app_name, config_filepath):
    with open(config_filepath, "r") as f:
        lines = f.readlines()
    updated_lines = []
    for line in lines:
        updated_line = line
        if line.startswith("let svelte_apps"):
            current_apps = line.split("=")[1].strip()
            current_apps = current_apps.replace(";", "").strip()
            current_apps = current_apps[1:-1].strip().split(",")
            current_app_names = []
            for app in current_apps:
                app = app.replace('"', "").replace("'", "").strip()
                if app:
                    current_app_names.append(app)
            current_app_names.append(app_name)
            updated_line = f"let svelte_apps = {current_app_names};\n"
        updated_lines.append(updated_line)
    with open(config_filepath, "w") as f:
        f.writelines(updated_lines)


cli.add_command(create)
cli.add_command(add_page)
