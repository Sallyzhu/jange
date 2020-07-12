from .clean import (
    CaseChangeOperation,
    lowercase,
    uppercase,
    LemmatizeOperation,
    lemmatize,
    ConvertToSpacyDocOperation,
    convert_to_spacy_doc,
    TokenFilterOperation,
    token_filter,
    remove_emails,
    remove_links,
    remove_numbers,
    remove_stopwords,
    remove_words_with_length_less_than,
)
from .vectors import TfIdfOperation, tfidf
