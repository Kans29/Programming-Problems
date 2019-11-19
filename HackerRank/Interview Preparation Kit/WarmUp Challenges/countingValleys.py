from sys import stdin


def main():
    N, ans = int(stdin.readline().strip()), 0
    hike, seaLevel = stdin.readline().strip(), 0
    for i in hike:
        if seaLevel == 0:
            if i == 'U':
                seaLevel += 1
            elif i == 'D':
                seaLevel -= 1
                ans += 1
        else:
            if i == 'U':
                seaLevel += 1
            elif i == 'D':
                seaLevel -= 1
    print(ans)


main()
