import fpdf
import yaml


def read_config():
    with open('../config.yml') as file:
        return yaml.safe_load(file)


def initialize_pdf():
    initialized_pdf = fpdf.FPDF(format='A4', unit='mm')
    initialized_pdf.add_page()
    return initialized_pdf


def _write_title(pdf, title, config):
    pdf.set_font(config['font'], size=config['size'], style='B')
    pdf.cell(200, 8, txt=title, ln=1, align="L")


def _write_artist(pdf, artist, config):
    pdf.set_font(config['font'], size=config['size'], style='B')
    pdf.cell(200, 6, txt=artist, ln=1, align="L")


def _write_body(pdf, song, config):
    pdf.set_font(config['font'], size=config['size'])
    for line in song:
        pdf.cell(100, 4, txt=line, ln=1, align="L")


def write_song(title, artist, song):
    config = read_config()
    pdf = initialize_pdf()

    _write_title(pdf, title, config['pdf']['title'])
    _write_artist(pdf, artist, config['pdf']['artist'])

    pdf.cell(200, 4, txt='', ln=1)

    _write_body(pdf, song, config['pdf']['body'])

    pdf.output(f"../out/{artist}-{title}.pdf")
