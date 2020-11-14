text = "Today Have been a very strange day, with the look of thing i don'T think it could be anyless Werid... Thou it has been oroductive thou."
count = {}

for character in text.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)