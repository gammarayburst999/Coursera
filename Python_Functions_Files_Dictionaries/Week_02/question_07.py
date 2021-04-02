#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for c in sally:
    if c not in characters:
        characters[c]=0
    characters[c]=characters[c]+1
keys=list(characters.keys())
worst_char=keys[0]
for ke in keys:
    if characters[ke] < characters[worst_char]:
        worst_char=ke
print(worst_char)
