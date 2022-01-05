from termcolor import colored, cprint


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        text = list(text)
        result = ""
        for INDEX in range(len(text)):
            if text[INDEX] in self.alphabet:
                # print(ord(text[INDEX]), INDEX, text[INDEX], self.alphabet.index(text[INDEX]), self.key[INDEX % len(self.key)], self.alphabet.index(self.key[INDEX % len(self.key)]))
                # result += chr((ord(text[INDEX]) + ord(self.key[INDEX % len(self.key)]) - 194) % len(self.alphabet) + 97)
                result += self.alphabet[(self.alphabet.index(text[INDEX]) +
                                         self.alphabet.index(self.key[INDEX % len(self.key)]))
                                        % len(self.alphabet)]
            else:
                result += text[INDEX]
        return result

    def decode(self, text):
        text = list(text)
        result = ""
        for INDEX in range(len(text)):
            if text[INDEX] in self.alphabet:
                if ord(text[INDEX]) <= ord(self.key[INDEX % len(self.key)]):
                    # result += chr((26 - ord(self.key[index % len(self.key)]) + ord(text[index])) % len(self.alphabet) + 97)
                    result += self.alphabet[(len(self.alphabet) -
                                             self.alphabet.index(self.key[INDEX % len(self.key)]) +
                                             self.alphabet.index(text[INDEX]))
                                            % len(self.alphabet)]
                else:
                    # result += chr((ord(text[INDEX]) - ord(self.key[INDEX % len(self.key)]) - 1) % len(self.alphabet))
                    result += self.alphabet[(self.alphabet.index(text[INDEX]) -
                                             self.alphabet.index(self.key[INDEX % len(self.key)]) )
                                            % len(self.alphabet)]
            else:
                result += text[INDEX]
        return result


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
# key = "abcdefghijklmnopqrstuvwxyz"
c = VigenereCipher(key, abc)

cprint("   encode", 'red')
print(c.encode('codewars'), 'rovwsoiv')
cprint("   decode", 'red')
print(c.decode('rovwsoiv'), 'codewars')
print("-----------------")
cprint("   encode", 'red')
print(c.encode('waffles'), 'laxxhsj')
cprint("   decode", 'red')
print(c.decode('laxxhsj'), 'waffles')
print("-----------------")
cprint("   encode", 'red')
print(c.encode('CODEWARS'), 'CODEWARS')
cprint("   decode", 'red')
print(c.decode('CODEWARS'), 'CODEWARS')
# print("-----------------")
# cprint("   encode", 'red')
# print(c.encode('oasisoasiso'), 'CODEWARS')
# cprint("   decode", 'red')
# print(c.decode('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'), 'CODEWARS')
#
# for i in range(96, 123):
#     print(chr(i), end=" ")
# # for i in range(90, 130):
# #     print(chr(i), i - 96)
'''
print("        ", end="")
for i in range(65, 91):
    print(chr(i), end=" ")
print()
for i in range(97, 123):
    if i - 96 < 10:
        print(end=" ")
    print(str(i - 96) + ")", chr(i - 32), end=" : ")
    for j in abc[i - 97: 123] + abc[0: i - 123]:
        print(j, end=" ")
    print()
'''
