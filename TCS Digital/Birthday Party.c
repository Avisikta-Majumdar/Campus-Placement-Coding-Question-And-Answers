#include<stdio.h>
int NthTerm(int a){
     int i,array[a];
     array[0]=1;
     array[1]=6;
     for(i=1;i<a;++i)
     {//array[i] = ((array[i-1] + array[i+1])/2)-2
         array[i+1] = (2*(array[i]+2)-array[i-1]);
     }
     return array[i-1];
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