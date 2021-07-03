#
#	Copyright 2021 Abir Haque
#	Subject to MIT License in LICENSE file
#
#	
#
# Perfect Square Roots:
#
#	Find the square root of any given perfect square without multiplication or division.
#
#	This is possible as all perfect squares are the sum of odd integers [1].
# This arithmetic sequence can be seen below:
#
#		1 = 1
#		4 = 1 + 3
#		9 = 1 + 3 + 5
#		16 = 1 + 3 + 5 + 7
#		25 = 1 + 3 + 5 + 7 + 9
#
#	We can find a square root of a perfect square by counting the times we add odd increasing numbers to equal a perfect square.
#
#	Below is a program I wrote when introduced to this very problem in a weekly challenge at Replit.com [2].
#	Given how I am extremely into recreational mathematics, I couldn't help by give a go at this challenge!
# I also decided that I might learn a few more Python hacks, such as writing multiple statements on one line [3][4].
#
#	Links:
# [1] https://en.wikipedia.org/wiki/Square_number
# [2] https://replit.com/talk/announcements/Weekly-Challenge-1/142232
# [3] https://tutorialspoint.com/How-to-provide-multiple-statements-on-a-single-line-in-Python
# [4] https://note.nkmk.me/en/python-multi-variables-values/

def sqrt(n):
	i, j, k = 0, -1, 0
	while(k < n):
		j+=2;	k+=j; i+=1
	return(i)

n = int(input("Please enter a number: "))
print("Square root of " + str(n) + " is " + str(sqrt(n)) +".")
