from src import ug_data_retriever
from src import pdf_writer

# title = "I want i"
# artist = "Linkin Park"
# url = "https://tabs.ultimate-guitar.com/tab/backstreet-boys/i-want-it-that-way-chords-827123"


def main():
    title = input("Which song do you want?: \n")
    search_results = ug_data_retriever.search_song(title)
    for x in range(len(search_results)):
        print(f"{x}: {search_results[x]['artist']}: {search_results[x]['name']}"
              f" v{search_results[x]['version']}, Votes: {search_results[x]['votes']}")
    number = int(input("Which version do you want? \n"))
    your_song = search_results[number]
    pdf_writer.write_song(your_song['name'], your_song['artist'], ug_data_retriever.get_song(your_song['url']))


main()
