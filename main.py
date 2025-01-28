
def main(): 
    file_path = "/home/jspaude/boot_dev/workspace/github.com/jspaude/bookbot/books/frankenstein.txt"
    text = contents(file_path)
    count = wordcount(text)
    lower_case = case_conversion(count)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {file_path} ---")
    print(f"{count} words found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
def contents(file_path):    
    with open(file_path) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def wordcount(text):
    count = text.split()
    return count

def case_conversion(count):
    lowered_list = []
    for c in count:
        lowered_string = c.lower()
        lowered_list.append(lowered_string)
    return(lowered_list)
    
'''
def dictionary_count(lower_case):
    alphabet =  {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,' ': 0 }

    for l in lower_case:
        for l in l:
            if l in alphabet:
                alphabet[l] +=1  
    return alphabet
'''
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

    


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
    #print(chars_list)



main()
'''

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
  '''
