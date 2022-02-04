import click
from cli import commands


@click.group()
def cli():
    pass


cli.add_command(commands)
if __name__ == '__main__':
    cli()
