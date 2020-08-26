import re

def _remove_double_blank_lines(song_body):
    song_body = \
        re.sub('\\\\r\\\\n\\\\r\\\\n\\\\r\\\\n', '\\\\r\\\\n\\\\r\\\\n', song_body)
    return song_body


# Removes [tab] and [ch] tags around chords and lyrics
def _remove_tags(song_body):
    song_body_without_tags = re.sub('\[\/?tab\]|\[\/?ch\]', '', song_body)
    return song_body_without_tags


# Splits lines at \r and \n characters
# Takes a single string and returns  a list of lines consisting of both chords and lyrics
def split_song_body_into_lines(song_body):
    p = compile_regex('\\\\r\\\\n')
    lines = re.split(p, song_body)
    print(f"Split song body into {len(lines)} lines.")
    return lines


# Strips HTML tags and removes double blank lines
def clean_song_body(song_body):
    song_body = _remove_double_blank_lines(song_body)
    song_body = _remove_tags(song_body)
    return song_body


def compile_regex(regex):
    return re.compile(regex)
