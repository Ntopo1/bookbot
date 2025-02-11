import os

def count_characters(file_contents):
    char_count = {} 
    for char in file_contents:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char not in char_count:
                char_count[lower_char]= 1
            else:
                char_count[lower_char] = char_count[lower_char] + 1
    return char_count


def sort_on(char_count):
    return char_count['num']


def main():
    current_dir = os.getcwd()
    print("Current working directory:", current_dir)
    
    # Build the full path to the file
    file_path = os.path.join(os.path.dirname(__file__), "books", "frankenstein.txt")
    print("Trying to open:", file_path)
    
    with open(file_path) as f:
        file_contents = f.read()
    #print(file_contents)
    word_count = len(file_contents.split())

    #get character counts
    char_count = count_characters(file_contents)   
    
    #convert to list of dict
    char_list = []
    for char, num in char_count.items():
        char_list.append({"char": char, "num": num})

    #sort the list
    char_list.sort(reverse=True, key=sort_on)

    #print report
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    print()
    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    
    print('--- End report ---')
#call report   
main()
    


    



