import random as random


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def random_partition(a, p, r):
    i = random.randint(p, r)
    a[i], a[r] = a[r], a[i]
    return partition(a, p, r)


def random_select(a, p, r, i):
    if p == r:
        return a[p]
    q = random_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif k > i:
        return random_select(a, p, q - 1, i)
    else:
        return random_select(a, q + 1, r, i - k)


def main():
    a = [0] * 10
    for i in range(0, 10):
        a[i] = random.randint(0, 100)
    print a
    print random_select(a, 0, 9, 2)


main()
