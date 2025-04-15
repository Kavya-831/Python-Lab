sentence = "the sky is blue and the grass is green"
words = sentence.split()

seen = set()
has_duplicates = False

for word in words:
    if word in seen:
        has_duplicates = True
        break
    seen.add(word)

print("Has duplicates:" if has_duplicates else "No duplicates.")
