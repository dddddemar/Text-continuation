import random
import nltk
from nltk.tokenize import word_tokenize

def generate_text(tagged_words, input_word, length):
    # 获取输入单词的词性标注
    input_tag = [tag for word, tag in tagged_words if word == input_word][0]

    # 查找匹配前缀的单词
    matches = []
    for word, tag in tagged_words:
        if tag.startswith(input_tag):
            matches.append(word)

    # 随机选择一个匹配单词作为前缀
    prefix = [input_word, random.choice(matches)]

    # 生成续写文本
    generated_text = ''
    while len(generated_text) < length:
        # 获取前缀的词性标注
        tagged_prefix = nltk.pos_tag(prefix)

        # 获取前缀的词性模式
        pattern = ' '.join([tag for word, tag in tagged_prefix])

        # 查找匹配的单词
        matches = []
        for word, tag in tagged_words:
            if tag.startswith(pattern):
                matches.append(word)

        # 随机选择一个匹配单词
        if matches:
            next_word = random.choice(matches)
        else:
            break

        # 添加单词到生成文本中
        generated_text += ' ' + next_word

        # 更新前缀
        prefix = prefix[1:] + [next_word]

    # 返回续写的文本
    return ' '.join(prefix) + generated_text