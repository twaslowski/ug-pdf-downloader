# ug-pdf-downloader

This is a script, written in Python, that will allow you to download songs
from the Ultimate Guitar website and save them as PDF files.
Simply input a song title and it will look up the most popular results and let 
you choose among them!

## Getting Started

You can install this script on your machine by cloning this Github repository:

    git clone https://github.com/TobiasWaslowski/ug-pdf-downloader.git

You may need to install the requests_html library; if so, run:

    python3 -m pip install requests_html


### Usage

Next up, you can just run the program! Simply run

    python3 main.py

### Configuration

Among the features that I'm looking to add, configurability is high on the list.
Right now, if you want a different font or colours, you'll have to modify the code yourself.
However, if you're looking to contribute, you're very welcome to do so!

## Contributing

I'm not expecting anyone to contribute here, but if you'd like to correct a typo 
(or actually help me implement a feature – you never know), just open a pull request. :)

### Bugs

I'm aware of some issues right now, such as the program not working if the "[Verse]" annotation
is not used, or it not correctly filtering out all the "&quot" HTML remains.
If you find anything else, open an issue and I'll address it as quickly as possible.