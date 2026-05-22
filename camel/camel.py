def camel_to_snake(camel):
    snake_str = ""
    for char in camel:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char.lower()
    return snake_str


name = input("CamelCase: ")

snake_name = camel_to_snake(name)

print(f"Snake_case: {snake_name}")


