#include<stdio.h>
int main()
{//Question:- https://www.youtube.com/watch?v=kdJ3XBRKH7I&list=PL1tpeH7dkvcIuRWunQqieQx4pltcOwGE_&index=4
    int n,m,r;
    scanf("%d %d %d",&n,&m,&r);
    int sumIn=0,sumOut=0;
    int in[n] , out[m];
    for(int i=0;i<n;++i)
    {
        int value;
        scanf("%d",&value);
        in[i] = value-r;
        sumIn+=in[i];
    }
    for(int i=0;i<m;++i)
    {
        int value;
        scanf("%d",&value);
        out[i] = value-r;
        sumOut+=out[i];
    }
    if(sumIn==sumOut)
    {
        printf("Balanced Junction!!");
    }
    else if(sumIn < sumOut)
    {//We have to add an input pipe
        int result = sumOut - sumIn;//actual capacity
        result+=r;//rated capacity
        printf("%d",result);
    }
    else{
        //We have to add an output pipe
        int result = sumIn - sumOut;//actual capacity
        result+=r;//rated capacity
        printf("-%d",result);
    }

    return 0;
}
