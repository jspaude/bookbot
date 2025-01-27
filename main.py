
def main(): 
    file_path = "/home/jspaude/boot_dev/workspace/github.com/jspaude/bookbot/books/frankenstein.txt"
    text = contents(file_path)
    count = wordcount(text)
    lower_case = case_conversion(count)
    letter_count = dictionary_count(lower_case)
    
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
    

def dictionary_count(lower_case):
    letters = {}
    for l in lower_case:
        for l in l:
            #letters[l] : 0
            print(type(l))
        

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
