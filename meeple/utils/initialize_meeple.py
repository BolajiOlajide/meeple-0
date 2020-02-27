import os
import json
from typing import Dict

import typer

from meeple.utils.profile import _add_user_profiles


def _does_meeple_exist(meeple_path: str) -> bool:
    """
    Check if `meeple.json` exists in the root of the project.
    """

    return os.path.exists(meeple_path)


def _create_meeple(
    meeple_path: str, profiles: Dict[str, Dict[str, str]]
) -> None:  # noqa: #501
    """
    Create `meeple.json` and add the profiles of users to it.
    """

    try:
        with open(meeple_path, "w+") as meeple:
            json.dump(
                profiles, meeple, indent=4,
            )
    except Exception:
        kwargs = {"fg": typer.colors.RED, "bold": True}
        typer.secho("unable to create meeple.json", **kwargs)
        raise typer.Abort()


def initialize_meeple() -> None:
    """
    Handle meeple initialization for first time and existing users.
    """

    cwd = os.getcwd()
    meeple_path = f"{cwd}/meeple.json"
    kwargs = {"fg": typer.colors.GREEN, "bold": True}

    if _does_meeple_exist(meeple_path):
        message = "meeple.json exists. Do you want to overwrite?"
        overwrite = typer.confirm(message)

        if not overwrite:
            raise typer.Exit()

    profiles = _add_user_profiles()

    if profiles:
        _create_meeple(meeple_path, profiles)

        no_of_users = len(profiles.keys())
        users_text = "users" if no_of_users > 1 else "user"
        message = f"Added {no_of_users} {users_text} to meeple.json."
        typer.secho(message, **kwargs)
    else:
        kwargs["fg"] = typer.colors.RED
        message = "No user added. Please try again."
        typer.secho(message, **kwargs)
