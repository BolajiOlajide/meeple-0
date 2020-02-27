import os

import typer

from meeple import __version__ as meeple_version
from meeple.utils import initialize_meeple


app = typer.Typer()


@app.command("version")
def get_meeple_version():
    """Get current version of meeple installed."""
    typer.echo(f"meeple: version {meeple_version}")


@app.command("init")
def init():
    """Initialize meeple for your project."""
    kwargs = {"fg": typer.colors.GREEN, "bold": True}
    typer.secho(f"Initializing meeple in {os.getcwd()}", **kwargs)
    initialize_meeple()


@app.command("add")
def add():
    """Add a user to meeple."""
    typer.echo("Adding user")


@app.command("delete")
def delete(nickname: str):
    """Delete a user from meeple."""
    typer.echo(f"Deleting user ---> {nickname}")


@app.command("update")
def update():
    """Delete a user from meeple."""
    typer.echo("Deleting user")


def main():
    app()
