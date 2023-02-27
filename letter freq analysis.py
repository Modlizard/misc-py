letter_frequency = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}

def word_score(word):
    score = 0
    for letter in word:
        score += letter_frequency[letter] if letter in letter_frequency else 0
    return score

target_string = 'uol thu hal aol zjybtwapvbz hcvjhkv'
topScore = 0
for offset in range(26):
    test_string = "".join([chr(((ord(x)-97+offset)%26)+97) if x != ' ' else ' ' for x in target_string])
    score = word_score(test_string)
    if score > topScore:
        topScore = score
        print(''.join(test_string), score)
