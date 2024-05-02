from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string


def preprocces_text(text):
    ignoreChar = ['\r', '\n', '', ' ', '``', "'s"]
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    words_lower = [token.lower() for token in words if not token.isdigit() and not token.isnumeric(
    ) and not token.isdecimal() and token not in string.punctuation and token not in ignoreChar and token not in nums]
    words_final = [lemmatizer.lemmatize(
        word) for word in words_lower if word not in stop_words]
    return words_final
