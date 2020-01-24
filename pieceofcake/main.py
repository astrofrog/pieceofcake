import os
import json
import click
from textwrap import wrap
from jinja2 import Environment, BaseLoader

BOLD = '\033[1m'
END = '\033[0m'

@click.command()
@click.argument('template')
@click.option('--checkout', default=None, help='branch, tag or commit to checkout after git clone')
def main(template, checkout):

    from cookiecutter.config import get_user_config
    from cookiecutter.repository import determine_repo_dir

    config_dict = get_user_config(
        config_file=None,
        default_config=False
    )

    repo_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations=config_dict["abbreviations"],
        clone_to_dir=config_dict["cookiecutters_dir"],
        checkout=checkout,
        no_input=True
    )

    # TODO: make it possible to specify directories/repos as in cookiecutter itself.
    with open(os.path.join(repo_dir, 'cookiecutter.json')) as f:
        cjson = json.load(f)

    print(BOLD + "Welcome to the pieceofcake, a user-friendly cookiecutter wrapper!" + END)
    print("")
    print("This script will now ask you a series of questions to help you set up")
    print("your package.")
    print("")

    parameters = cjson.get('_parameters')

    values = {}

    for key, value in cjson.items():

        if key.startswith('_'):
            continue

        # Since default values can be jinja2 templates, we treat them as such
        # using the values collected from the user so far
        if isinstance(value, str):
            template = Environment(loader=BaseLoader).from_string(value)
            value = template.render(cookiecutter=values)

        if isinstance(value, list):
            default_value = 1
        else:
            default_value = value
        help = None
        prompt = key

        if parameters is not None and key in parameters:
            if 'default_value' in parameters[key]:
                default_value = parameters[key]['default_value']
            if 'help' in parameters[key]:
                help = parameters[key]['help']
            if 'prompt' in parameters[key]:
                prompt = parameters[key]['prompt']

        if help:
            print(os.linesep.join(wrap(help, width=70)))
        if isinstance(value, list):
            for index, item in enumerate(value):
                print(f'{index + 1} - {item}')
        values[key] = click.prompt(BOLD + '> ' + prompt + END,
                                   default=default_value)

        print("")
