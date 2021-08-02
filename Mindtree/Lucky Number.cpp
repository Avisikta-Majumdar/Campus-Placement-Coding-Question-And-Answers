#include<iostream>
using namespace std;

int main()
{
    int no;
    cin>>no;
    int array[10];
    int i=0;
    while(no>0){
        int rem = no%10;
        array[i++] = rem;
        no/=10;
    }
    int mid=i/2;
    //cout<<mid;
    int sumFirst=0,sumSecond=0;
    for(int j=0;j<mid;++j)
    sumFirst+=array[j];
    for(int j=mid;j<i;++j)
    sumSecond+=array[j];
    
    //cout<<"sumSecond  :- "<<sumSecond<<"\tsumFirst:- "<<sumFirst;
    if(sumFirst==sumSecond)
    cout<<"Lucky Number";
    else
    cout<<"Not Lucky Number";
    return 0;
}
/*
MINDTREE CODING QUESTION 2021
Question:-https://youtu.be/1telg5tkiP0

*/