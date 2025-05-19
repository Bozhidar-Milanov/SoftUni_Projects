# 🧵 Python Text Transformation Toolkit

print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

choice = int(input("Enter the number corresponding to your choice: "))
print(f"You chose option {choice}.")

if choice not in range(1, 10):
    print("❌ Invalid choice! Please restart the program.")
    quit()

text = input("Enter the text: ")
print(f"You choose {text}.")

if choice == 1:
   print(f"🤗 This is your converted word: {text[::-1]}")

elif choice == 2:
    text = text.upper()
    print(f"😀 This is your capitalize word: {text}")

elif choice == 3:
    text = text.lower()
    print(f"😃 This is your lowered word: {text}")

elif choice == 4:
    text = text.title()
    print(f"😌 This is your word with the first capital letter: {text}")

elif choice == 5:
    number_of_vowels = 0

    for vowel in text:
        if vowel.lower() in "aeiou":
            number_of_vowels += 1

    print(f"🙂 Sum of the vowels is: {number_of_vowels}")

elif choice == 6:
    text = text.replace(" ", "")
    print(f"😉 Your connected word is: {text}")

elif choice == 7:
    new_text = ""

    for vowels in text:
        if vowels.lower() in "aeiou":
            new_text += "*"
        else:
            new_text += vowels

    print(f"🧐 Your new word is looking like that {new_text}")

elif choice == 8:
    text = text.replace(" ", "")
    text = text.lower()

    if text == text[::-1]:
        print("😀 Text is a palindrome.")
    else:
        print("☹️ Text is not a palindrome.")

elif choice == 9:
    words = text.split()
    word_count = {}

    for word in words:
        word = word.lower()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word}: {count}")

