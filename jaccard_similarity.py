from nltk import word_tokenize
from PyPDF2 import PdfReader
# nltk.download('punkt')

def jaccard_similarity(data1, data2):
    token1 = word_tokenize(data1)
    token2 = word_tokenize(data2)
    irisan = set(token1).intersection(set(token2))
    gabungan = set(token1).union(set(token2))
    return len(irisan) / len(gabungan)

def read_data(data):
    pdf_reader = PdfReader(open(data, 'rb'))
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

if __name__ == "__main__":
    data1 = read_data("data1.pdf")
    data2 = read_data("data2.pdf")
    similarity_score = jaccard_similarity(data1, data2)

    # print(f"Skor kemiripan antara dua dokumen adalah {similarity_score} atau sekitar {round(similarity_score * 100, 2)}%")
    print(f"Persentase kemiripan antara dua dokumen adalah {round(similarity_score * 100, 2)}%")