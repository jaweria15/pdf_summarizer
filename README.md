# PDF Text Extractor and Summarizer

This Python project is designed to extract text from PDF documents and summarize it into a concise form using Natural Language Processing (NLP) techniques. It is ideal for extracting and analyzing the content of large PDF files, providing quick insights through summarization.

## Features

1. **PDF Text Extraction**: 
   - Reads and extracts text from all pages of a PDF file.
   - Handles errors gracefully, such as missing files or unreadable content.

2. **Text Summarization**:
   - Summarizes the extracted text into a specified number of key sentences.
   - Uses word frequency analysis to identify and rank the most relevant sentences.


## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.9,3.10,3.11,3.12**
2. Required Python libraries:
   - `pypdf` (for reading PDF files)
   - `nltk` (for natural language processing)

To install the necessary libraries, use:

```bash
pip install pypdf nltk
```

3. Download NLTK data files:
   The script will automatically download the required data files for tokenization and stopwords. Ensure you have an internet connection for the first run.

---

## How to Use

1. Place your PDF file in the project directory.
2. Update the file path in the `file_path` variable in the script:
   ```python
   file_path = 'example.pdf'
   ```
3. Run the script:
   ```bash
   python pdfread.py
   ```
4. If text extraction is successful, the full text and a summary (default: 10 sentences) will be displayed in the console.

---

## Code Structure

1. **`extract_text_from_pdf(file_path)`**:
   - Reads the specified PDF file and extracts text from all pages.
   - Returns an error message if the file is missing or unreadable.

2. **`summarize_text(text, max_sentences=10)`**:
   - Summarizes the input text into the specified number of sentences.
   - Leverages NLTK for tokenization and word frequency analysis.

3. **Main Workflow**:
   - Extracts text from the PDF.
   - Summarizes the text if extraction is successful.
   - Handles errors and displays meaningful messages for invalid input.

---

## Example Output

### Full Text (Snippet)
```
Full Text Extracted:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eget tortor urna. ...
**************************************************
```

### Summary
```
Summary:
1. Quisque eget tortor urna. 
2. Lorem ipsum dolor sit amet. 
3. Sed varius consectetur velit. ...
```

---

## Customization

- **Number of Sentences in Summary**:
   - Change the `max_sentences` parameter in the `summarize_text` function to adjust the length of the summary.

- **Input PDF File**:
   - Update the `file_path` variable to point to your desired PDF file.

---

## Limitations

1. The script may not perform well with PDFs containing:
   - Non-text content (e.g., scanned images).
   - Complex layouts or embedded fonts.

2. Summarization relies on frequency-based ranking and may not always capture contextual nuances.

---

## Future Enhancements

1. Add support for image-based text extraction using OCR (e.g., `pytesseract`).
2. Improve summarization using advanced NLP models like BERT or GPT.
3. Develop a GUI for easier interaction.

---

## License

This project is open-source and available under the MIT License. Contributions are welcome!
