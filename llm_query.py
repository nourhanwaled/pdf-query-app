import google.generativeai as genai

genai.configure(api_key="AIzaSyB7m7NLwLubgkXEP_Lz5dXmpnUDSLJ81sE")

model = genai.GenerativeModel("gemini-1.5-flash")

def query_gemini_summary(text, max_summary_length=4000):
    """
    Summarizes a long text using the Google Gemini model.
    """
    response = model.generate_content(
        f"Summarize the following text in {max_summary_length} words or less:\n\n{text}"
    )
    return response.text.strip()

def query_gemini_with_summary(summary, query):
    """
    Queries the LLM with a summarized text and the user's query.
    """
    response = model.generate_content(
        f"Based on the following summarized text, answer the query: {query}\n\nSummary: {summary}"
    )
    return response.text.strip()
