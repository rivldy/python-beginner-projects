def replace_word():
  str = "hi guys im tomi, and hi hi hi"
  print(str)

  word_to_replace = input("Enter word to replace: ")
  word_replacement = input("Enter word replacement: ")
  print(str.replace(word_to_replace, word_replacement))

replace_word()