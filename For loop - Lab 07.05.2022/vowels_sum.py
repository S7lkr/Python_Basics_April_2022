text = input()
# The sum we will use in our for loop
sm = 0

# Here we will transform the text into the number of its letters. Note: space is also a symbol
# Where 'len(text)' means the AMOUNT of symbols in the text, represented in number
# i.e. if text = peter -> len(peter) = 5; 5 letters in peter -> p, e, t, e, r
for i in range(len(text)):
    if text[i] == 'a':
        sm += 1
    if text[i] == 'e':
        sm += 2
    if text[i] == 'i':
        sm += 3
    if text[i] == 'o':
        sm += 4
    if text[i] == 'u':
        sm += 5
print(sm)