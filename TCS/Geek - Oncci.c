/*
QUESTION
Geek created a random series and given a name geek-onacci series. Given four integers A, B, C, N.
 A, B, C represents the first three numbers of geek-onacci series. Find the Nth number of the series.
  The nth number of geek-onacci series is a sum of the last three numbers
  (summation of N-1th, N-2th, and N-3th geek-onacci numbers)

Input:
1. The first line of the input contains a single integer T denoting
the number of test cases. The description of T test cases follows.
2. The first line of each test case contains four
space-separated integers A, B, C, and N.

Output: For each test case, print Nth geek-onacci number

Constraints:
1. 1 <= T <= 3
2. 1 <= A, B, C <= 100
3. 4 <= N <= 10

*/


#include <stdio.h>

int main() {

	int testcase;
	scanf("%d",&testcase);
	while(testcase--)
	{
	    int n,array[10];
	    scanf("%d %d %d %d",&array[0],&array[1],&array[2],&n);
	    for(int i=4;i<=n;i++)
	    {
	        array[i-1] = array[i-2]+array[i-3]+array[i-4];
	    }
	    printf("%d\n",array[n-1]);
	}

}
