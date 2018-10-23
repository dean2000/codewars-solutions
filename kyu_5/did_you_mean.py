class Dictionary:
	def __init__(self,words):
		self.words=words
	def find_most_similar(self,wrong_word):
		i = (([set(set(wrong_word) & set(word)) for word in self.words]))
		if len(wrong_word) != 0: return self.words[i.index(max(i))] 
 
words_list = ['stars', 'mars', 'wars', 'codec', 'codewars']
i = Dictionary(words_list)
print(i.find_most_similar('coddwars'))

# help(str.index)