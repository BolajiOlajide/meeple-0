import typer

from .meeple import _fetch_meeple, _create_meeple
from .profile import _add_user_profile


def add_user(nickname):
    profile = _add_user_profile(nickname)
    profiles = _fetch_meeple()

    existing_user = profiles.get("profile")

    if existing_user:
        message = f"{nickname} exists in the meeple.json. \
Do you want to update the user info?"
        kwargs = {"fg": typer.colors.RED, "bold": True}
        typer.secho(message, **kwargs)
        raise typer.Exit()

    profiles[nickname] = profile
    _create_meeple(profiles)
    kwargs = {"fg": typer.colors.GREEN, "bold": True}
    message = f"{nickname} successfully added to meeple.json"
    typer.secho(message, **kwargs)
