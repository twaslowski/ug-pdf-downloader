import fpdf


def initialize_pdf():
    initialized_pdf = fpdf.FPDF(format='A4', unit='mm')
    initialized_pdf.add_page()
    return initialized_pdf


def configure_main_block(initialized_pdf):
    initialized_pdf.set_font("Times", size=10)


def configure_title(initialized_pdf):
    initialized_pdf.set_font("Times", size=18, style='B')


def configure_artist(initialized_pdf):
    initialized_pdf.set_font("Times", size=12, style='I')


def write_song(title, artist, song):
    pdf = initialize_pdf()

    configure_title(pdf)
    pdf.cell(200, 8, txt=title, ln=1, align="L")

    configure_artist(pdf)
    pdf.cell(200, 6, txt=artist, ln=1, align="L")
    pdf.cell(200, 4, txt='', ln=1)

    configure_main_block(pdf)
    for line in song:
        pdf.cell(100, 4, txt=line, ln=1, align="L")

    pdf.output(f"../out/{artist}-{title}.pdf")
