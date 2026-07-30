import pandas as pd

from pypdf import PdfReader
from docx import Document


def load_document(uploaded_file):

    text = ""

    if uploaded_file.name.endswith(".pdf"):

        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    elif uploaded_file.name.endswith(".docx"):

        doc = Document(uploaded_file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    elif uploaded_file.name.endswith(".xlsx"):

        df = pd.read_excel(uploaded_file)

        text += df.to_string(index=False)

    return text