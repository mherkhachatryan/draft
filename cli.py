import click


@click.group("example")
def commands():
    """
    Example for using group of functionalities
    """


@commands.command("echo", help="Output something in console")
@click.option('-s', '--string-to-echo', help="String to output")
def echo(string_to_echo):
    click.echo(string_to_echo)
