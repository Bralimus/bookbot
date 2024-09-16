def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter in characters:
                    characters[letter] += 1
                else:
                    characters[letter] = 1
    return characters

def sort(dict):
    return dict["num"]

def dict_to_list(dict):
    list =[]
    for key in dict:
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        list.append(new_dict)
    return list 

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    
    character_count = count_characters(file_contents)
    character_count = dict_to_list(character_count)
    character_count.sort(reverse=True, key=sort)
    
    for character in character_count:
        print(f"The '{character['name']}' character was found {character['num']} times")

    print("--- End Report ---")
    
    
        
main()
