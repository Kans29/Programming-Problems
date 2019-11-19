from sys import stdin


def main():
    inputString = stdin.readline().strip()
    n = int(stdin.readline().strip())
    initialAs, cantWords, leftLetters = inputString.count(
        'a'), n//len(inputString), n % len(inputString)
    ans = (initialAs*cantWords) + (inputString[:leftLetters].count('a'))
    print(ans)


main()
