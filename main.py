from pdf_processor import extract_text_from_pdf, chunk_text
from llm_query import aggregate_responses

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    user_query = input("Enter your query: ")

    try:
        text = extract_text_from_pdf(pdf_path)
        # print("text")
        # print(text)
        chunks = chunk_text(text)
        # print("chunks")
        # print(chunks)
        final_response = aggregate_responses(chunks, user_query)

        print("Final Response:")
        print(final_response)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
