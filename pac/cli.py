"""Console script for pac."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("python-pac-package")
    click.echo("=" * len("python-pac-package"))
    click.echo("Python package pac with MPI Evolutionary Biology branding.")


if __name__ == "__main__":
    main()  # pragma: no cover
