from typer import Typer, echo, secho

from meeple import __version__ as meeple_version


app = Typer()


@app.command("version")
def get_meeple_version():
    """Method for getting the version of meeple."""
    echo(f"meeple: version {meeple_version}")


@app.command("init")
def init():
    """Initializes meeple for your project."""
    secho("meeple_version")


def main():
    app()
