year ="2013"
year=int(year)
if year%400==0 or (year%4==0 and year%100!=0):
	print '366'
else:
	print '365'