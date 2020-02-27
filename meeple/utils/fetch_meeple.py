import json

import typer


def fetch_meeple(path: str):
    kwargs = {"fg": typer.colors.RED, "bold": True}
    try:
        with open(path) as file:
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
