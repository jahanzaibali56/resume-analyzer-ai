import pdfplumber
import docx

def extract_text(file, text_input):
    if file:
        if file.filename.endswith(".pdf"):
            with pdfplumber.open(file) as pdf:
                return " ".join([p.extract_text() or "" for p in pdf.pages])

        elif file.filename.endswith(".docx"):
            doc = docx.Document(file)
            return " ".join([p.text for p in doc.paragraphs])

    return text_input or ""