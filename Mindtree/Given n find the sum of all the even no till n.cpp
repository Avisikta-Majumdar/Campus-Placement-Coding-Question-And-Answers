#include<iostream>
#include<string>
using namespace std;
int main()
{
    int n,sum=0;
    cin>>n;
    for(int i=2;i<=n;i+=2)
    {
        sum+=i;
    }
    cout<<sum;
    return 0;
}
/*MINDTREE CODING QUESTION 
Question:- https://youtu.be/_pSx8ndzCjg
*/