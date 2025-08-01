# Day 12 – File Word Counter
# Aabhas Khaniya
# Counts how many words are in a text file. Foundation for NLP & file automation.

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            print(f"📄 '{filename}' has {len(words)} words.")
    except FileNotFoundError:
        print("⚠️ File not found. Make sure the path is correct.")
    except Exception as e:
        print(f"❌ Error: {e}")

file_path = input("Enter the path to the file you want to analyze: ")
count_words(file_path)
