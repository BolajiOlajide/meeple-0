from typing import Dict

import typer


def _add_user_profiles() -> Dict[str, Dict[str, str]]:
    profiles = {}

    typer.echo("Add users to meeple. Press enter to stop adding users.\n")
    kwargs = {"type": str, "default": " ", "show_default": False}

    while True:
        nickname = typer.prompt("What's the nickname of the user?", **kwargs).strip()  # noqa: E501
        if not nickname:
            break

        name = typer.prompt("What's the full name of the user?", **kwargs).strip()  # noqa: E501
        if not name:
            break

        email = typer.prompt("What's the email address of the user?", **kwargs).strip()  # noqa: E501
        if not email:
            break

        profiles[nickname] = dict(name=name, email=email)
        typer.echo(f"Adding {nickname} to meeple. \n")
    return profiles
