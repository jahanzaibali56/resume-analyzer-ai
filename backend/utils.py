import re

ALLOWED_EXTENSIONS = {"pdf", "docx"}

def clean_text(text):

    if not text:
        return ""

    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()


def allowed_file(filename):

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()
    return extension in ALLOWED_EXTENSIONS


def error_response(message):

    return {
        "success": False,
        "error": message
    }