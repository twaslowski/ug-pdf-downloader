import re

chords = [
    'A', 'A#', 'B', 'C', 'C#',
    'D', 'D#', 'E', 'F', 'F#',
    'G', 'G#'
]


def _get_chord_regex():
    return re.compile('([A-G](#|b){0,2})m?(sus|maj|min)?\d?[ |\n]')


def _transpose_chord(operation, steps, chord):
    chord_index = chords.index(chord)
    chord_transposed = chords[operation(chord_index, steps) % len(chords)]
    return chord_transposed


def transpose(mode, steps, song):
    chord_regex = _get_chord_regex()
    for i in range(len(song)):
        if (res := re.search(chord_regex, song[i])) is not None:
            song[i] = re.sub(chord_regex, lambda x: _transpose_chord(increase, steps, x.group(1)), song[i])
    return song


def increase(n, m):
    return n + m


def decrease(n, m):
    return n - m
