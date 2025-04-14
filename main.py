from stats import word_count, character_count, sorted_dict
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
            
            return file_contents
        
        
    

    file_contents = get_book_text(filepath)
    chars_dict = character_count(file_contents)
    
    wc = word_count(file_contents)
    sorted_list = sorted_dict(chars_dict)

            


    
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {filepath}...")

    print("-------- Word Count ------")
    print(wc)
    print("--------Character Count --------")
    #print(character_count(file_contents))   
    #print(sorted_dict(character_count(file_contents)))
    for char in sorted_list:
        letter = char["char"]
        freq = char["count"]
        print(f"{letter}: {freq}")

    print("======== END ========")
    
    

if __name__ == "__main__":
    main()
    
