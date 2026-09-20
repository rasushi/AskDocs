import fitz

def extract_text(pdf_path):
    with fitz.open(pdf_path) as document:
        text = ""

        for page in document:
            text += page.get_text()

    return text