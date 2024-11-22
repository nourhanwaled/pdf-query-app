import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def chunk_text(text, max_length=1000):
    """
    Splits text into manageable chunks for the LLM.
    """
    words = text.split()
    for i in range(0, len(words), max_length):
        yield " ".join(words[i:i + max_length])