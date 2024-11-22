import google.generativeai as genai

genai.configure(api_key="AIzaSyB7m7NLwLubgkXEP_Lz5dXmpnUDSLJ81sE")

model = genai.GenerativeModel("gemini-1.5-flash")

def query_gemini(chunk, query):
    """
    Queries the Google Gemini model with a chunk of text and a query.
    """
    response = model.generate_content(
        f"Based on the following text, answer the query: {query}\n\nText: {chunk}"
    )
    return response.text.strip()

def aggregate_responses(chunks, query):
    """
    Aggregates responses from querying the model for multiple chunks.
    """
    responses = [query_gemini(chunk, query) for chunk in chunks]
    return ' '.join(responses)
