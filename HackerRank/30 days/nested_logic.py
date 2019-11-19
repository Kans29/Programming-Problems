from sys import stdin

def book_fee(ret_date,exp_date):
	'''
	Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

	If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)
	If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, . fine = 15 x days off
	If the book is returned after the expected return month but still within the same calendar year as the expected return date, the . fine = 500 x days off
	If the book is returned after the calendar year in which it was expected, there is a fixed fine of . 10000
	'''
	d,m,y = ret_date
	de,me,ye = exp_date
	fee = 0
	if ye >= y:
		ME = me + ((ye - y)*12)
		if ME >= m:
			if de + ((ME - m)*31) >= d:
				fee = 0
			else:
				fee = (15 * (d - de))
		else:
			fee = (500 * (m - me))
	else:
		fee = 10000
	return fee

def main():
	inp = stdin
	ret_date = [int(x) for x in inp.readline().strip().split()]
	exp_date = [int(x) for x in inp.readline().strip().split()]
	print(book_fee(ret_date,exp_date))

main()