#include <stdio.h>

int main() {
	int testcase;
	scanf("%d",&testcase);
	while(testcase--)
	{
	    int n;
	    scanf("%d",&size);
	    int array[size];
	    for(int i=n-1;i>=0;--i)
	    {
	        scanf("%d",&array[i]);
	    }
	    for(int i=0;i<n;++i)
	    {
	        printf("%d ",array[i]);
	    }
	    printf("\n");
	}
	return 0;
}
