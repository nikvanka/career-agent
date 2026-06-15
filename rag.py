from pypdf import PdfReader

def read_pdf(uploaded_file):
    text = ""

    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text