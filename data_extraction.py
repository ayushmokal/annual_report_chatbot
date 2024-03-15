import pypdf2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = pypdf2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        all_text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            all_text += page_text

    return all_text

# VERY basic placeholder for finding an answer  
def find_answer_in_data(question, report_text):
    if "revenue" in question.lower():
        return "Placeholder: Revenue data would be extracted here" 
    else:
        return "Sorry, I couldn't find an answer to that yet." 
