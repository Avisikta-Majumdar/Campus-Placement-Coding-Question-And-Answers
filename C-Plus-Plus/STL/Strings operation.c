#include<stdio.h>
#include <string.h>
int main(){
  char str[20];
  printf("Enter string: ");
  scanf("%s",str);//reads string from console
  printf("String is: %s",str);
  printf("\nLower String is: %s",strlwr(str));
  printf("\nReverse String :- %s",strrev(str));
  printf("\nUpper String :- %s",strupr(str));
 return 0;
}
