def order(sentence):
    a = list(sentence.split(' '))
    number = [int(x) for x in list(sentence) if x.isdigit()]
    result = []
    for i in range(len(list(sentence.split()))):
        N = number.index(min(number))
        result.insert(number.pop(N), a.pop(a.index(a[N])))
    return ' '.join(result)


print(order("4of Fo1r pe6ople g3ood th5e the2"))
