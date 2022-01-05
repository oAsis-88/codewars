# from collections import Counter
def is_valid_walk(walk):
    # c = Counter(walk)
    # return c['n'] == c['s'] and c['w'] == c['e'] and len(walk) == 10
    # без импорта from collections import Counter
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
