def pig_it(text):
    x = []
    for i in list(text.split()):
        if i.isalpha():
            x.append(i[1:] + i[0] + "ay")
        else:
            x.append(i[1:] + i[0])
    return " ".join(x)


'''
return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split()])
'''


print(pig_it('Pig latin is cool'), '-> igPay atinlay siay oolcay')
print(pig_it('This is my string'), '-> hisTay siay ymay tringsay')
print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Hello world !'))  # elloHay orldway !
