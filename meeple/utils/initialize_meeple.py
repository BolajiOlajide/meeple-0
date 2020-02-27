import os
import json
from typing import Dict

import typer

from meeple.utils.profile import _add_user_profiles


def _does_meeple_exist(meeple_path: str) -> bool:
    return os.path.exists(meeple_path)


def _create_meeple(meeple_path: str, profiles: Dict[str, Dict[str, str]]) -> None:  # noqa: #501
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
    cwd = os.getcwd()
    meeple_path = f"{cwd}/meeple.json"

    if _does_meeple_exist(meeple_path):
        message = "meeple.json exists. Do you want to overwrite?"
        overwrite = typer.confirm(message)

        if not overwrite:
            raise typer.Exit()

    profiles = _add_user_profiles()
    _create_meeple(meeple_path, profiles)
