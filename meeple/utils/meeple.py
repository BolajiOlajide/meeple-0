import os
import json
from typing import Dict

import typer


def _fetch_meeple() -> Dict[str, Dict[str, str]]:
    cwd = os.getcwd()
    meeple_path = f"{cwd}/meeple.json"

    kwargs = {"fg": typer.colors.RED, "bold": True}
    try:
        with open(meeple_path) as file:
            return json.load(file)
    except FileNotFoundError:
        typer.secho(
            "Can't find 'meeple.json' in directory. Are you \
in the right directory?",
            **kwargs
        )
        raise typer.Exit()
    except json.decoder.JSONDecodeError:
        typer.secho(
            "Meeple is malformed. Ensure 'meeple.json' \
is a valid JSON.",
            **kwargs
        )
        raise typer.Exit()


def _create_meeple(
    profiles: Dict[str, Dict[str, str]]
) -> None:  # noqa: #501
    """
    Create `meeple.json` and add the profiles of users to it.
    """

    try:
        cwd = os.getcwd()
        meeple_path = f"{cwd}/meeple.json"

        with open(meeple_path, "w+") as meeple:
            json.dump(
                profiles, meeple, indent=4,
            )
    except Exception:
        kwargs = {"fg": typer.colors.RED, "bold": True}
        typer.secho("unable to create meeple.json", **kwargs)
        raise typer.Abort()
