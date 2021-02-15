
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import unidecode
stop_words = set(stopwords.words('english'))

def clean(text):
    # lower
    text = text.lower()
    # punctuation
    text = ''.join([element for element in text if element not in string.punctuation])
    # numbers
    text = ''.join([element for element in text if element not in string.digits])
    # stopwords
    token = word_tokenize(text)
    text = ' '.join([element for element in token if element not in stop_words])
    # accent
    text = unidecode.unidecode(text)
    return text



