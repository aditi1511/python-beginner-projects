def add_item(dict,word):
  temp = dict.get(word, None)
  if temp is None:
    dict[word] = 1
  else:
    dict[word] += 1
  return dict[word]
  
def build_dictionary(list):
  new = {}
  for word in list:
    add_item(new,word)
  return new
  

def build_word_counter(list):
  new = {}
  for word in list:
    add_item(new,word.lower())
  return new
  
def build_letter_distribution(list):
  new = {}
  for word in list:
    word = word.lower()
    for letter in word:
      add_item(new,letter)
  return new