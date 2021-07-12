//Question :-https://www.youtube.com/watch?v=OOYaQdurwIA&list=PL1tpeH7dkvcIuRWunQqieQx4pltcOwGE_&index=1

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n,digonal1=0,digonal2=0;
    scanf("%d",&n);
    for(int i=0;i<n;++i){
            int j,value;
        for(j=0;j<n;++j){

            scanf("%d",&value);

        if (i==j)
        {
            if(i==(n-1)/2)//The middle element which we have to add in both digonal
            {
                digonal1+=value;
                digonal2+=value;
            }
            else{
                digonal1+=value;
            }
        }
        else if(i+j ==n-1)
        {
            digonal2+=value;
        }
        }
    }//printf("Digonal1 :- %d Digonal2 :-%d",digonal1,digonal2);
    printf("\nDifference between this 2 digonal is %d",abs(digonal1-digonal2));

}
