from pypdf import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):

    try:
        reader = PdfReader(file_path)
        all_text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
        return all_text if all_text.strip() else "No readable text found in the PDF."
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to summarize text
def summarize_text(text, max_sentences=10):


    if not text.strip():
        return "No content to summarize."

    # Preprocess text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Create a frequency table for words
    freq_table = {}
    for word in words:
        word = word.lower()
        if word.isalpha() and word not in stop_words:  # Include only alphabetic, non-stop words
            freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences based on word frequencies
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in freq_table:
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_table[word]

    # Sort and select top sentences
    ranked_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)
    top_sentences = [sentence for sentence, _ in ranked_sentences[:max_sentences]]

    # Join top sentences to form the summary
    summary = " ".join(top_sentences)
    return summary if summary.strip() else "The text could not be summarized meaningfully."

# Main workflow
if __name__ == "__main__":
    # Path to the PDF file
    file_path = 'example.pdf'

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)
    if text.startswith("Error") or text == "No readable text found in the PDF.":
        print(text)  # Print error or notification about empty text
    else:
        print("Full Text Extracted:")
        print(text[:1000] + "...")  # Display first 1000 characters of the extracted text
        print("\n" + "*" * 50 + "\n")

        # Summarize the text (targeting ~10 sentences)
        summary = summarize_text(text, max_sentences=10)
        print("Summary:")
        print(summary)
