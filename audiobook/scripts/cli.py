import os
import click
from audiobook.metafile import init as metafile_init, meta_data_template
from audiobook.exceptions import ExInitialized
from audiobook.consts import EXIT_OK, EXIT_ALREADY_INITIALIZED

@click.group()
def cli():
    pass


@cli.command()
@click.option('--title', default='')
@click.option('--author', multiple=True)
@click.option('--isbn', default='')
@click.option('--tag', multiple=True)
@click.option('--rating', default=0)
def init(title: str, author: list, isbn: str, tag: list, rating: int):
    """Initialize the current directory as audio book directory"""
    try:
        meta_data = meta_data_template
        meta_data['title'] = title
        meta_data['authors'] = list(author)
        meta_data['ISBN'] = isbn
        meta_data['tags'] = list(tag)
        meta_data['rating'] = rating
        metafile_init(os.getcwd(), meta_data)
    except ExInitialized:
        click.echo('Current directory is already initialized')
        exit(EXIT_ALREADY_INITIALIZED)
    click.echo('Current directory is initialized')
    exit(EXIT_OK)
