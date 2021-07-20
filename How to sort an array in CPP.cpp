#include<bits/stdc++.h>
using namespace std;
int main()
{
    int array[5]={10,2,5,3,6};
    int n = sizeof(array) / sizeof(array[0]);
    cout<<"Size of array :- "<<array+n<<endl;
    sort(array,array+n);
    for(int i=0;i<5;++i)
    cout<<array[i]<<" ";

    return 0;
}
