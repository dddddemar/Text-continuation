
from preprocess import preprocess_text
from generate import generate_text
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# 加载示例数据
from nltk.corpus import gutenberg
text = gutenberg.raw('austen-emma.txt')

# 预处理文本数据
tagged_words = preprocess_text(text)

# 选择一个输入单词，并生成续写文本
input_word = 'She'
generated_text = generate_text(tagged_words, input_word, 10)

# 输出续写文本
print(generated_text)