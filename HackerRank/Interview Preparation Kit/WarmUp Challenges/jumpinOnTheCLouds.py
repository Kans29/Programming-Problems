from sys import stdin


def main():
    N = int(stdin.readline().strip())
    clouds = [int(x) for x in stdin.readline().strip().split()]
    ans, i = 0, 0
    while i < N-1:
        i += 1
        if i+1 < N:
            if clouds[i+1] == 0:
                i += 1
        ans += 1
    print(ans)


main()
