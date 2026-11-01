"""The `angio` command-line tool."""

import typer

from angio import __version__

app = typer.Typer(help="Angio: watch your model learn, from the inside.", no_args_is_help=True)


@app.command()
def version() -> None:
    """Print the installed Angio version."""
    typer.echo(f"angio {__version__}")


@app.command()
def ui(
    logdir: str = typer.Option("angio_runs", help="Folder that holds Angio runs."),
    port: int = typer.Option(8080, help="Port for the dashboard."),
) -> None:
    """Start the Angio dashboard (not implemented yet, see docs/ROADMAP.md M3)."""
    typer.echo(f"Dashboard not implemented yet (would serve {logdir} on port {port}).")


if __name__ == "__main__":
    app()