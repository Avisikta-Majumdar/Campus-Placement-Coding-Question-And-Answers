#include<stdio.h>
int main(){
//Question : - https://youtu.be/KuycgoPQ_yk?list=PL1tpeH7dkvcIuRWunQqieQx4pltcOwGE_
int noOfPerson,profit,percentage;
scanf("%d %d %d",&noOfPerson,&profit,&percentage);
int i=1;
while(i<noOfPerson)
{
    profit = (profit*percentage)/100;
    i++;
}
printf("The root Superviser will get %d rupees",profit);
return 0;}
