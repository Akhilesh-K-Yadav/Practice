# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/


def reverse(x):
    abs_str = str(abs(x))
    r = list(abs_str)
    r.reverse()
    if x < 0:
        r.insert(0, "-")

    abs_str = ""
    abs_str = abs_str.join(r)
    ret = int(abs_str)
    if (ret >= (2**31)) or (ret <= (-(2**31) - 1)):
        ret = 0
    return ret


def main():
    print(reverse(2147483648))


main()
