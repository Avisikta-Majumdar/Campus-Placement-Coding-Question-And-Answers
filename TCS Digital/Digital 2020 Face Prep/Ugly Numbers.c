#include<stdio.h>
int isUgly(int value){
    int temp=1;
    while(value>1){
        if(value%2==0){
            value/=2;
        }
        else if(value%3==0){
            value/=3;
        }
        else if(value%5==0){
            value/=5;
        }
        else {
            return 0;
        }
    }
    return 1;
}
int main(){
int test;
  scanf("%d",&test);
  while(test--){
  int n,i=0,j;
scanf("%d",&n);
    int ugly[n];
    ugly[i++]=1;
    for(j=2;j<2000000000;++j)
    {
        if(isUgly(j))
        {ugly[i++]=j;}

      if(i<n){continue;}
        else{break;}
    }
    printf("%d\n",ugly[n-1]);
  }



}