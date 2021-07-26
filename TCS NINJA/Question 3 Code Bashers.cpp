#include<iostream>

using namespace std;
int main()
{
    int n,a=0,b=1,s;
    cin>>n;
    if(n>5 &&n<=20){cout<<a<<" "<<b<<" ";
    for(int i=2;i<n;++i)
   {
       s=a+b;
       a=b;
       b=s;
       cout<<s<<" ";
   }    
    }
    else{
         cout<<"INVALID INPUT";
        }

    return 0;
}
/* Question :- https://youtu.be/3b4IhjpanDM  */