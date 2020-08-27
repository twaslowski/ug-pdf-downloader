import requests
import re
from src.parsers import search_parser
from src.parsers import lyric_parser


# Retrieves the entire webpage and returns the chunk that the song lyrics are situated in
def _retrieve_song_body(url):
    print(f"Retrieving url: {url}")
    response = requests.get(url).content.decode('utf-8')
    return lyric_parser.get_song_body_from_response(response)


def _retrieve_search_results(song_name):
    song_name = re.sub(' ', '%20', song_name)
    url = f"https://www.ultimate-guitar.com/search.php?search_type=title&value={song_name}"
    response = requests.get(url).content.decode('utf-8')
    return response


def get_search_results_for_song_name(song_name):
    response = _retrieve_search_results(song_name)
    songs = search_parser.get_songs_as_list(response)
    return songs


def get_song_by_url(url):
    body = _retrieve_song_body(url)
    cleaned_song_body = lyric_parser.clean_song_body(body)
    song_as_lines = lyric_parser.split_song_body_into_lines(cleaned_song_body)
    return song_as_lines
