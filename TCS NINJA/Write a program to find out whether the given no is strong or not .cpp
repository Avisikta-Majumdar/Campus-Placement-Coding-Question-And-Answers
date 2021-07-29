
#include<iostream>
using namespace std;
int fact(int n);
int main()
{
    int number,store ;
    cin>>number;
    store = number;
    int total=0;
    while(store>0){
        int rem = store%10;
        total+= fact(rem);
        store/=10;
    }
    
    if(number==total){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }
    return 0;
}
int fact(int n){
    if (n==1|| n==0){
    return 1;}
    else{
        return n*fact(n-1);
    }
}
/*Question :- https://youtu.be/qYJYDyCZXCY */