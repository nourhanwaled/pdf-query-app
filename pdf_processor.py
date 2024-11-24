import PyPDF2
from llm_query import query_gemini_summary
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

def chunk_text(text, max_length=4000):
    """
    Splits text into manageable chunks based on word count.
    """
    words = text.split()
    for i in range(0, len(words), max_length):
        yield " ".join(words[i:i + max_length])

def summarize_chunks(chunks, max_summary_length=4000):
    """
    Summarizes all chunks into a single cohesive summary.
    """
    # Concatenate all chunks to form the input for summarization
    concatenated_text = " ".join(chunks)
    return query_gemini_summary(concatenated_text, max_summary_length)
