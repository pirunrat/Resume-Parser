from PyPDF2 import PdfReader
from docx import Document

class Utils:
    @staticmethod
    def read_pdf(file_path):
        try:
            text = ""
            with open(file_path, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
        except KeyError as e:
            return f'Error from pdf reading:{e}'
        return text
    
    @staticmethod
    def read_text(file_path):
        try:
            with open(file_path, "r") as f:
                text = f.read()
        except KeyError as e:
            return f'Error from txt reading:{e}'
        return text
    
    @staticmethod
    def read_docx(file_path):
        try:
            text = ""
            doc = Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except KeyError as e:
            return f'Error from doc reading:{e}'
        return text
    

    