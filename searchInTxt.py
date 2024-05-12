def search(t, w):
    r = 0
    count = 0
    for chr in t:
        if chr == w[count]:
            count += 1
            if count == len(w):
                r += 1
                count = 0
    return r

# TESTS #

text = 'abracadabra'
word = 'bra'

print(search(text, word))