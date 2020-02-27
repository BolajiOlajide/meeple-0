import os

import typer

from .profile import _add_user_profiles
from .meeple import _create_meeple


def _does_meeple_exist() -> bool:
    """
    Check if `meeple.json` exists in the root of the project.
    """

    cwd = os.getcwd()
    meeple_path = f"{cwd}/meeple.json"
    return os.path.exists(meeple_path)


def initialize_meeple() -> None:
    """
    Handle meeple initialization for first time and existing users.
    """

    kwargs = {"fg": typer.colors.GREEN, "bold": True}

    if _does_meeple_exist():
        message = "meeple.json exists. Do you want to overwrite?"
        overwrite = typer.confirm(message)

        if not overwrite:
            raise typer.Exit()

    profiles = _add_user_profiles()

    if profiles:
        _create_meeple(profiles)

        no_of_users = len(profiles.keys())
        users_text = "users" if no_of_users > 1 else "user"
        message = f"Added {no_of_users} {users_text} to meeple.json."
        typer.secho(message, **kwargs)
    else:
        kwargs["fg"] = typer.colors.RED
        message = "No user added. Please try again."
        typer.secho(message, **kwargs)
