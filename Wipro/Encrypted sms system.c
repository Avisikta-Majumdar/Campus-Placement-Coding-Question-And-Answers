/*Wipro Coding Question
Input :- 1st line it will take a no and in 2nd line it will take a string

Output:- It will return a string where each characters' ascii value will be increased by input no.*/

#include<stdio.h>
int main()
{
    int no;
    char string[100],resultString[100];
    printf("Enter number :-");
    scanf("%d",&no);
    printf("Enter the string now :-");
    scanf("%s",string);
    for(int i=0;string[i]!='\0';++i)
    {
        int temp = (int)string[i] + no;
        resultString[i] += (char)temp ; 
        
    }
    printf("Result :- %s",resultString);
    
}

/*Test case 1:
Input :- 3
       as3gAsd
Output:-
       dv6jDvg*/