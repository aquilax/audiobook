import os
import click
from audiobook.metafile import init as metafile_init
from audiobook.exceptions import ExInitialized
from audiobook.consts import EXIT_OK, EXIT_ALREADY_INITIALIZED


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Initialize the current directory as audio book directory"""
    try:
        metafile_init(os.getcwd())
    except ExInitialized:
        click.echo('Current directory is already initialized')
        exit(EXIT_ALREADY_INITIALIZED)
    click.echo('Current directory is initialized')
    exit(EXIT_OK)
