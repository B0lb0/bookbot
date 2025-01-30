import string

def count_words(s):
    w_mode = True
    w_count = 0
    for c in s:
        if c.isspace():
            if not w_mode:
                w_mode = True
        else:
            if w_mode:
                w_mode = False
                w_count += 1
    return w_count

def get_char_counts(s):
    counts = {}
    s_lowercase = s.lower()

    for c in s_lowercase:
        if not c in counts:
            counts[c] = 1
        else:
            counts[c] +=1
    return counts

def print_report(s):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(s)} words were found in the document\n")

    char_counts = get_char_counts(s)
    for c in string.ascii_lowercase:
        if c.isalpha():
            print(f"The '{c}' character was found {char_counts[c]} times")

    print("--- End report ---")

def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

main()
