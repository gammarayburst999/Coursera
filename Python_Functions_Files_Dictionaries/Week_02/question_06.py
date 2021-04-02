#Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"
characters={}
for c in sally:
    if c not in characters:
        characters[c]=0
    characters[c]=characters[c]+1
for y in characters:
    print(characters[y])
keys=list(characters.keys())
best_char=keys[0]
for ke in keys:
    if characters[ke] > characters[best_char]:
        best_char=ke
print(best_char)
