#longest-common-subsequence problem
#time:O(nlogn)
def bisearch(b, l, w):
    left = 0
    right = l - 1
    if w > b[l - 1]:
        left = l + 1
    else:
        while left <= right:
            mid = left + (right - left)/2
            if b[mid] > w:
                right = mid - 1
            elif b[mid] < w:
                left = mid + 1
            else:
                return mid
    return left


def lis(array, n, path):
    l = 1
    b = [-1] * n
    b[0] = array[0]
    for i in range(1, n):
        pos = bisearch(b, l, array[i])
        if array[i] > b[l - 1]:
            b[pos - 1] = array[i]
            l += 1
            path[i] = b[l - 2]
        else:
            b[pos] = array[i]
            path[i] = b[pos - 1]
    return l


def main():
    array = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    path = [-1] * 9
    a = -1
    length = lis(array, len(array), path)
    print "length:", length
    for i in range(len(array)):
        if path[i] > a:
            a = path[i]
            print a
    print max(array)

main()
