#include<stdio.h>
//Condition :-  a[i] = ((a[i-1] + a[i+1])/2)-2
int NthTerm(int a){
     int i,array[1+a];
     array[1]=1;
     array[2]=6;
     for(i=3;i<=a;++i)
     {
         array[i] = (2*(array[i-1]+2)-array[i-2]);
     }
     return array[a];

}

int main()
{
   int testcase;
 scanf("%d",&testcase);
  while(testcase--){
  int n;
    scanf("%d",&n);
    printf("%d\n",NthTerm(n));//<<"\n";

  }
    return 0;
}
