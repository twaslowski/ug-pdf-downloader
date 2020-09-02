import fpdf
from src import config


def initialize_pdf():
    initialized_pdf = fpdf.FPDF(format='A4', unit='mm')
    initialized_pdf.add_page()
    return initialized_pdf


def _write_title(pdf, title, conf):
    pdf.set_font(conf['font'], size=conf['size'], style=conf['style'])
    pdf.cell(200, 8, txt=title, ln=1, align="L")


def _write_artist(pdf, artist, conf):
    pdf.set_font(conf['font'], size=conf['size'], style=conf['style'])
    pdf.cell(200, 6, txt=artist, ln=1, align="L")


def _write_body(pdf, song, conf):
    pdf.set_font(conf['font'], size=conf['size'])
    for line in song:
        pdf.cell(100, 4, txt=line, ln=1, align="L")


def write_song(title, artist, song):
    pdf = initialize_pdf()

    _write_title(pdf, title, config.get_config_element('pdf.title'))
    _write_artist(pdf, artist, config.get_config_element('pdf.artist'))

    pdf.cell(200, 4, txt='', ln=1)

    _write_body(pdf, song, config.get_config_element('pdf.body'))

    pdf.output(f"../out/{artist}-{title}.pdf")
