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
    p = _compile_regex('\\\\r\\\\n')
    lines = re.split(p, song_body)
    print(f"Split song body into {len(lines)} lines.")
    return lines


# Strips HTML tags and removes double blank lines
def clean_song_body(song_body):
    song_body = _remove_double_blank_lines(song_body)
    song_body = _remove_tags(song_body)
    return song_body


def _compile_regex(regex):
    return re.compile(regex)


def get_song_body_from_response(response):
    p = _compile_regex('(\[Verse.* ?)\[/tab\]')
    content = re.search(p, response)

    # If the lyrics don't contain a [Verse] at the beginning, search for an "Intro"
    if content is None:
        alternative_p = _compile_regex('\\\\n(\[?Intro.*\[/tab\])')
        content = re.search(alternative_p, response)

    if content is None:
        alternative_p = _compile_regex('(\[ch.*)\[/tab\]')
        content = re.search(alternative_p, response)

    if content is None:
        print(f"Song could not be parsed: {response}")
        exit(0)

    return content.group(1)
