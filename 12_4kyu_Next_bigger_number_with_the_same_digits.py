import itertools
import time


def next_bigger(n):
    n_ = list(str(n))
    for i in range(len(n_) - 1, 0, -1):
        if int(n_[i]) > int(n_[i - 1]):
            for j in range(len(n_) - 1, i - 1, -1):
                if int(n_[j]) > int(n_[i - 1]):
                    n_[j], n_[i - 1] = n_[i - 1], n_[j]
                    n_ = n_[:i] + sorted(n_[i:])
                    return int("".join(n_))
    return -1


print(next_bigger(59884848459853), 59884848483559, next_bigger(59884848459853) == 59884848483559)
print(next_bigger(940596272), 940596722, next_bigger(940596272) == 940596722)
print()
print(next_bigger(1234567980), 1234568079, next_bigger(1234567980) == 1234568079)
print(next_bigger(127653), 132567, next_bigger(127653) == 132567)

print(next_bigger(9) == -1)
print(next_bigger(111) == -1)
print(next_bigger(531) == -1)
print(next_bigger(12) == 21)
print(next_bigger(513) == 531)
print(next_bigger(2017) == 2071)
print(next_bigger(414) == 441)
print(next_bigger(144) == 414)
