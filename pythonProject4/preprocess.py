import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def preprocess_text(text):
    # 分割文本成句子
    sentences = sent_tokenize(text)

    # 分割每个句子成单词
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))

    # 标注单词的词性
    tagged_words = nltk.pos_tag(words)

    return tagged_words