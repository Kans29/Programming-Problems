from sys import stdin

def main():
	inp = stdin
	dic ={}
	line = inp.readline().strip().split()
	while len(line)>1:
		dic[line[1]] = line[0]
		line = inp.readline().strip().split()

	line = inp.readline().strip()
	while len(line)>0:
		solve = dic.get(line)
		if solve == None:
			solve = "eh"
		print (solve)
		line = inp.readline().strip()
main()
