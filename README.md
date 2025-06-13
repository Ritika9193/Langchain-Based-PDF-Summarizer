# LangChain-Based PDF Summarizer with Google Gemini

## Overview

This project is a **LangChain-based PDF Summarizer** that leverages the **Google Gemini API** to generate AI-driven summaries of PDF documents. The application is built using **Streamlit** for a user-friendly interface, allowing real-time document analysis.

## Features

- 📄 **Upload PDFs** directly through the web interface.
- 🧠 **AI-driven summarization** using Google Gemini API.
- 🎯 **Prompt engineering techniques** to enhance summarization accuracy.
- ⚡ **Streamlit-based UI** for interactive usage.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed.

### 1. Clone the Repository

```sh
git clone https://github.com/mohit-singh2003/pdf-summarizer.git
cd pdf-summarizer
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up API Key

1. Create a `.env` file in the root directory.
2. Add the following line:
   ```sh
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. Replace `your_actual_api_key_here` with your Google Gemini API key.

## Usage

### Run the Application

```sh
streamlit run app.py
```

### Upload a PDF

1. Open **[http://localhost:8501/](http://localhost:8501/)** in your browser.
2. Upload a **PDF file**.
3. Wait for the **AI-generated summary** to appear.

## Requirements

- `streamlit`
- `requests`
- `PyPDF2`
- `python-dotenv`

## Troubleshooting

- **ModuleNotFoundError: No module named 'dotenv'**
  - Run `pip install python-dotenv`
- **API Key Missing Error**
  - Ensure you have correctly set up the `.env` file and restarted your terminal.

## License

This project is licensed under the **MIT License**.

## Contributing

Feel free to submit issues or pull requests to enhance this project!

## Author

Mohit

