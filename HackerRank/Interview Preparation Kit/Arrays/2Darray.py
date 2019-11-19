from sys import stdin


def main():
    matrix, size, ans = [], 6, float('-inf')
    line = [int(x) for x in stdin.readline().strip().split()]
    while size > 0:
        matrix.append(line)
        line = [int(x) for x in stdin.readline().strip().split()]
        size -= 1
    i, j = 1, 1
    while i < 5:
        j = 1
        while j < 5:
            act = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j] + \
                matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
            if act > ans:
                ans = act
            j += 1
        i += 1
    print(ans)


main()
