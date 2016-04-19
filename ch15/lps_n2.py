def lps(string):
    maxlength = 0
    start = 0
    low = 0
    high =0
    for i in range(1, len(string)):
        low = i - 1
        high = i
        while (low >= 0 and high < len(string) and string[low] == string[high]):
            if(high - low + 1 > maxlength):
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while (low >= 0 and high < len(string) and string[low] == string[high]):
            if(high - low + 1 > maxlength):
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1
    return maxlength


def main():
    string = "character"
    length = lps(string)
    print length

main()
