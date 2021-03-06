# Kopiowanie przez wartość
a = 4


def increment(x):
    x = x + 1
    return x


increment(x=a)  # kopiowanie przez wartość (do funkcji trafia wartość)

print(a)

###################################

# Kopiowanie przez referencje
b = [4]


def increment(x):
    x[0] = x[0] + 1

increment(x=b)  # Kopiowanie przez referencję (do funkcji trafia referencja)

print(b)

###################################


a = 4
b = a  # kopiowanie przez wartość

a += 1

print(b)

c = [4]
d = c  # kopiowanie przez referencje

c.append(5)
print(d)

# Inny przykład kopiowania przez referencję
a_list = [1, 2, 3]


class A:
    def powieksz(self, a):
        a.append(4)


a = A()
a.powieksz(a_list)
a.powieksz(a_list)

print(a_list)
