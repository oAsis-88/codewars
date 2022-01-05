def anagrams(word, words):
    result = []
    word_map = dict()
    for i in word:
        if i in word_map:
            word_map[i] = word_map[i] + 1
        else:
            word_map[i] = 1
    for i in range(len(words)):
        words_map = dict()
        for j in words[i]:
            if j in words_map:
                words_map[j] = words_map[j] + 1
            else:
                words_map[j] = 1
        if word_map == words_map:
            result.append(words[i])
    return result


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
