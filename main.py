def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        print(f"--- Begin report of {f.name} ---")
        print(f"{word_count} words found in the document.")
        print("\n")


        for i in char_count:
            name = i["name"]
            num = i["num"]
            print(f"The '{name}' character was found {num} times.")


        print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    sorted = []
    for char in text.lower():
        if char.isalpha():
            try:
                char_count[char] += 1
            except KeyError:
                char_count[char] = 1

    for i in char_count:
        sorted.append({"name": i, "num": char_count[i]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["num"]

main()
