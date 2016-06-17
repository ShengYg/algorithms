def count_sort(a, b, k, h):
    c = [0] * (k + 1)
    for i in range(len(a)):
        c[int(a[i][h])] = c[int(a[i][h])] + 1
    for i in range(1, k+1):
        c[i] = c[i] + c[i - 1]
    for i in range(len(a), 0, -1):
        #b[c[int(a[i - 1][h])] - 1][h] = a[i - 1][h]
        b[c[int(a[i - 1][h])] - 1] = a[i - 1]
        c[int(a[i - 1][h])] = c[int(a[i - 1][h])] - 1

def main():
    list=[21,56,63,34,43,85,37,21,64,72]
    list_new = [str(i) for i in list]
    b = [['1', '1']for i in range(10)]
    c = [['1', '1'] for i in range(10)]
    count_sort(list_new,b,7, 1)
    count_sort(b, c, 8, 0)
    print b
    print c

main()
