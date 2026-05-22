name = input("")



for char in name:
    new_name = ""
    if char == "i":
        new_name += "_" + char
print(new_name)
