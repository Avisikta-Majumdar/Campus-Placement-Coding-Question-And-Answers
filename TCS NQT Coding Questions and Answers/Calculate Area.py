"""
Jack is a cricket coach.He knew the radius (r in meters) of circular cricket round.
Write a program to help Jack to find the area of cricket ground .
You can use standard formulae to calculate the area of circle.

NOTE:-
fOR YOUR REFERENCE aREA(P) OF CIRCLE FORMULA IS P= PI* R^2

INPUT FORMAT:-
First line contains input integer which is radius (r) of circle.

OUTPUT FORMAT:-
output contains area of circle in float format with 2 point precession.

CONSTRAINTS:-
20<= r <= 30

Sample Input:- 22
Sample Output:- 1520.53

Sample Input:- 31
Sample Output:-"Wrong Rdius ENTRY."
"""
import math as m
def Area(r):
    return round((m.pi * (r**2)),2)

radius = int(input())
print(Area(radius) if radius>=20 and radius<=30 else "Wrong Radius ENTRY")
