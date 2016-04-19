def preprocess(s):
    stack = []
    stack.append('$')   #begin
    stack.append('#')
    for i in range(len(s)):
        stack.append(s[i])
        stack.append('#')
    stack.append('^')     #end
    return stack


def lps(s):
    # type: (object) -> object
    if len(s) <= 1:
        return s
    stack = preprocess(s)
    mx = 0
    p = [0] * len(stack)
    for i in range(1, len(stack) - 1):
        p[i] = mx > i and min(p[2 * id - i], mx - i) or 1
        while stack[i + p[i]] == stack[i - p[i]]:
            p[i] += 1
        if i + p[i] > mx:
            mx = i + p[i]
            id = i
    index = 0
    maxlen = 0
    for i in range(1, len(stack)):
        if p[i] > maxlen:
            maxlen = p[i]
            index = i
    return s[(index - maxlen)/2:((index - maxlen)/2 + maxlen - 1)]


def main():
    s = "12212321"
    s_new = lps(s)
    print s_new


main()
