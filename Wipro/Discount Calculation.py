"""
An e-commerce company plans to give their customers a discount for the christmas holiday. The discount will be calculated
on the basis of the bill amount of the order placed.
The discount amount is the product of the sum of all the odd digits and the sum od all the even digits of the customer's total bill amount.

Test case 1 :-
Input :- 2514795
Output :- 162
Explanation :- (5+1+7+9+5) * (2+4)
                27 * 6
                162
"""

def Discount_Price(BillAmount):
    oddAddition=0
    evenAddition=0
    r=0
    while BillAmount>0:
        r = BillAmount%10
        oddAddition+= r if r&1 else 0
        evenAddition += r if not r&1 else 0
        BillAmount//=10
    #Just for cheking
    print(oddAddition , evenAddition)
    return oddAddition * evenAddition


Input = int(input("Enter bill amount:-"))
print(Discount_Price(Input))
