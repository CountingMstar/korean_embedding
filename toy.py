from konlpy.tag import Mecab
tokenizer = Mecab()
a = tokenizer.morphs("아버지가방에들어가신다")

print(a)