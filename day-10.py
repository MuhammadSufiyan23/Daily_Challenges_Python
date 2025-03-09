# DAY-10 CHALLENGE

import re

def is_anagram(word1, word2):
    word1 = re.sub(r"[^a-zA-Z]", "", word1).lower()
    word2 = re.sub(r"[^a-zA-Z]", "", word2).lower()

    return sorted(word1) == sorted(word2)

def main():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    if is_anagram(word1, word2):
        print("✅ Yes, it's an anagram!")
    else:
        print("❌ No, it's not an anagram!")

if __name__ == "__main__":
    main()
