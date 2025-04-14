def word_count(file_contents):
        num_words = 0
        frankenstein_split = file_contents.split()
        count = (len(frankenstein_split))
        return f"Found {count} total words"
        #return frankenstein_split

def character_count(file_contents):
        char_dict = {}
        characters = list(file_contents)
        for char in characters:
            lower = char.lower()
            if lower in char_dict:
                   char_dict[lower] +=1
            else: char_dict[lower] = 1
        return char_dict

def sort_on(char_dict):
      return char_dict["count"]

def sorted_dict(char_dict):
    chars_list = []
    for char,count in char_dict.items():
        char_info = {"char": char, "count": count}
        x = char_info["char"]
        if x.isalpha():
            chars_list.append(char_info)
            
            
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    


          
    
    


