from src import ug_data_retriever
from src import pdf_writer


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

    pdf_writer.write_song(chosen_song_title, chosen_song_artist, ug_data_retriever.get_song_by_url(chosen_song_url))


if __name__ == "__main__":
    main()
