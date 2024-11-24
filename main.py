from pdf_processor import extract_text_from_pdf, chunk_text, summarize_chunks
from llm_query import query_gemini_with_summary

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    user_query = input("Enter your query: ")

    try:
        # Step 1: Extract text from the PDF
        text = extract_text_from_pdf(pdf_path)

        # Step 2: Chunk the text
        chunks = list(chunk_text(text))

        # Step 3: Summarize the chunks to reduce tokens
        summary = summarize_chunks(chunks)

        # Step 4: Query the model using the summary and user query
        final_response = query_gemini_with_summary(summary, user_query)

        print("Final Response:")
        print(final_response)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
