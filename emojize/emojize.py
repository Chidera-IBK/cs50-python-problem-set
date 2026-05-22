import emoji

text = input("Input: ")

converted = emoji.emojize(text, language="alias")

print("Output: ", converted)
  