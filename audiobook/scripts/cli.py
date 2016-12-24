import yaml
import os
import click
from audiobook.metafile import (init as metafile_init, meta_data_template,
                                scan_direcory)
from audiobook.exceptions import ExInitialized
from audiobook.consts import EXIT_OK, EXIT_ALREADY_INITIALIZED
from audiobook.filter import get_filter
from typing import List


@click.group()
def cli():
    pass


@cli.command()
@click.option('--title', default='')
@click.option('--author', multiple=True)
@click.option('--isbn', default='')
@click.option('--tag', multiple=True)
@click.option('--rating', default=0.0)
@click.option('--language', default='English')
@click.option('--cover', default='')
def init(title: str, author: list, isbn: str, tag: list, rating: float,
         language: str, cover: str):
    """Initialize the current directory as audio book directory"""
    try:
        meta_data = meta_data_template
        meta_data['title'] = title
        meta_data['authors'] = list(author)
        meta_data['ISBN'] = isbn
        meta_data['tags'] = list(tag)
        meta_data['rating'] = rating
        meta_data['language'] = language
        meta_data['cover'] = cover
        metafile_init(os.getcwd(), meta_data)
    except ExInitialized:
        click.echo('Current directory is already initialized')
        exit(EXIT_ALREADY_INITIALIZED)
    click.echo('Current directory is initialized')
    exit(EXIT_OK)

@cli.command()
@click.argument('directory')
@click.option('--filter', multiple=True)
def scan(directory: str, filter: List[str]):
    """Scans directory for audio books and prints the meta information"""
    books = scan_direcory(directory)
    filter_func = get_filter(list(filter))
    for book in books:
        book = filter_func(book)
        if book:
            print('- - -')
            print(yaml.dump(book))
