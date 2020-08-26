import re


def _filter_search_results(response):
    p = _compile_regex('data-content.*')
    results = re.search(p, response)
    return results


def _get_number_of_results(response):
    p = _compile_regex('results_count&quot;:(.*?),')
    number_of_results = re.search(p, response)
    return number_of_results


def _map_songs_as_objects(songs):
    for x in range(len(songs)):
        songs[x] = {
            'name': _get_song_name(songs[x]),
            'artist': _get_song_artist(songs[x]),
            'version': _get_song_version(songs[x]),
            'votes': _get_song_votes(songs[x]),
            'url': _get_song_url(songs[x])
        }
    return songs


def get_songs_as_list(response):
    data_p = _compile_regex('&quot;data&quot;:.*,&quot;types&quot;:')
    data = re.search(data_p, response).group()
    split_p = _compile_regex('\},\{')
    songs = re.split(split_p, data)
    songs_filtered = _filter_songs(songs)
    songs_mapped = _map_songs_as_objects(songs_filtered)
    return songs_mapped


def _filter_songs(songs):
    # This entry is not needed as it doesn't represent chords
    del songs[0]
    songs = list(filter(_song_url_does_not_contain_pro_keyword, songs))
    songs = list(filter(_is_chords, songs))
    return songs


def _is_chords(song):
    p = _compile_regex('chords')
    res = re.search(p, song)
    return True if res is not None else False


def print_song_data(song):
    print(f"{_get_song_name(song)}: {_get_song_artist(song)} v{_get_song_version(song)}, Votes: {_get_song_votes(song)}")


def _get_song_artist(song):
    p = _compile_regex('artist_name&quot;:&quot;(.*?)&')
    return re.search(p, song).group(1)


def _get_song_name(song):
    p = _compile_regex('song_name&quot;:&quot;(.*?)&')
    return re.search(p, song).group(1)


def _get_song_version(song):
    p = _compile_regex('version&quot;:(.*?),')
    return re.search(p, song).group(1)


def _get_song_votes(song):
    p = _compile_regex('votes&quot;:(.*?),')
    return re.search(p, song).group(1)


def _get_song_url(song):
    p = _compile_regex('tab_url&quot;:&quot;(.*?)&')
    return re.search(p, song).group(1)


def _song_url_does_not_contain_pro_keyword(url):
    p = _compile_regex('/pro/')
    res = re.search(p, url)
    return True if res is None else False


def _compile_regex(regex):
    return re.compile(regex)
