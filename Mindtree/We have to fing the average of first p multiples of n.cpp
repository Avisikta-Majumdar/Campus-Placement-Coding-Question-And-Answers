#include<iostream>
#include<string>
using namespace std;
int main()
{
    int n,p,sum=0,avg=0;
    cin>>n>>p;
    for(int i=1;i<=p;++i)
    {
        sum += (n*i);
    }
    avg = (sum/p);
    cout<<avg;
    return 1;
}
/*MINDTREE CODING QUESTION 
Question:- https://youtu.be/_pSx8ndzCjg
*/