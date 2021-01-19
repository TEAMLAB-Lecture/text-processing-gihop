def normalize(input_string):
    strings = input_string.split()
    normalized_string = ''
    for string in strings:
        normalized_string += string.lower() + ' '
    
    return normalized_string.rstrip()


def no_vowels(input_string):
    input_string = input_string.replace("a", "")
    input_string = input_string.replace("e", "")
    input_string = input_string.replace("i", "")
    input_string = input_string.replace("o", "")
    input_string = input_string.replace("u", "")
    input_string = input_string.replace("A", "")
    input_string = input_string.replace("E", "")
    input_string = input_string.replace("I", "")
    input_string = input_string.replace("O", "")
    input_string = input_string.replace("U", "")
    
    return input_string
