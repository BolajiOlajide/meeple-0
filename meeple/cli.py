import os

import typer

from meeple import __version__ as meeple_version
from meeple.utils import initialize_meeple, add_user


app = typer.Typer()

kwargs = {"fg": typer.colors.GREEN, "bold": True}


@app.command("version")
def get_meeple_version() -> None:
    """Get current version of meeple installed."""
    typer.echo(f"meeple: version {meeple_version}")


@app.command("init")
def init() -> None:
    """Initialize meeple for your project."""
    typer.secho(f"Initializing meeple in {os.getcwd()}", **kwargs)
    initialize_meeple()


@app.command("add")
def add(nickname: str) -> None:
    """Add a user to meeple.json"""
    typer.secho(f"Adding {nickname} to meeple.json", **kwargs)
    add_user(nickname)


@app.command("delete")
def delete(nickname: str) -> None:
    """Delete a user from meeple."""
    typer.echo(f"Deleting user ---> {nickname}")


@app.command("update")
def update() -> None:
    """Delete a user from meeple."""
    typer.echo("Deleting user")


def main():
    app()
