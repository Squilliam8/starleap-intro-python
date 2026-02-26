n1 = 'emily'
n2 = 'austin'
n1c = n1.casefold()
n2c = n2.casefold()
if n1c == n2c:
    print("same")
elif n1c < n2c:
    print("less than")
elif n1c > n2c:
    print("greater than")


def is_reverse(word1, word2):
    flip1 = ''
    index =len(word1) -1
    while index >= 0:
        l = word1[index]
        flip1 += 1
        index -= 1
    print('flip1', flip1)
    return flip1 == word2

print(is_reverse('emily', 'ylime'))