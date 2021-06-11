#include <stdio.h>

int main() {
	int testcase;
	scanf("%d",&testcase);
	while(testcase--)
	{
	    int size,rotation;
	    scanf("%d %d",&size,&rotation);
	    int array[size];
	    for(int i=0;i<size;++i)
        {
            int index = (i+rotation)%size;
            scanf("%d",&array[index]);
            printf("index %d array[index] %d\n",index,array[index]);
            //This line is for understanding purpose

        }
printf("\n\n");
	    //printing the array
	    for(int i=0;i<size;++i)
	       printf("%d ",array[i]);
	 printf("\n");
	}
	return 0;
}
