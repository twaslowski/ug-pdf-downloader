import ug_data_retriever
import pdf_writer
from parsers import chord_transposer


def main():
    title = input("Which song do you want?: \n")
    search_results = ug_data_retriever.get_search_results_for_song_name(title)

    for x in range(len(search_results)):
        print(f"{x}: {search_results[x]['artist']}: "
              f"{search_results[x]['title']}"
              f" v{search_results[x]['version']}, "
              f"Votes: {search_results[x]['votes']}")

    number = int(input("Which version do you want? \n"))

    chosen_song = search_results[number]
    chosen_song_title = chosen_song['title']
    chosen_song_artist = chosen_song['artist']
    chosen_song_url = chosen_song['url']
    chosen_song_version = chosen_song['version']

    chosen_song_body = ug_data_retriever.get_song_by_url(chosen_song_url)
    transposition = input("Transpose? Enter 0 for original, and +/- plus a number x for transposition of x semitones.\n")
    if transposition != str(0):
        operation = transposition[0]
        semis = int(transposition[1])
        chosen_song_body = chord_transposer.transpose(operation, semis, chosen_song_body)
    chosen_song['transposition'] = transposition

    pdf_writer.write_song(chosen_song_title, chosen_song_artist, chosen_song_version, chosen_song_body, transposition)


if __name__ == "__main__":
    main()
