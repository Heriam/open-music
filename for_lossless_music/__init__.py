
from .moresound import Moresound, Source
from .song import songs2table
from .download import download

__version__ = '0.0.1'


def find_best_quality(songs):
    ranks = ['FLAC', 'APE', '320MP3', '192AAC', '192OGG', '128MP3', '96AAC', '48AAC', '24AAC']
    for r in ranks:
        if r in songs:
            return r
    return None