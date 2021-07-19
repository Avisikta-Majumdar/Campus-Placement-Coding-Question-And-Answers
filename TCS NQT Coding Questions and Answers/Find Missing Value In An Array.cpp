#include <iostream>

using namespace std;
int main()
{
    int temp,N,i=0;
    cin>>N;
    int array[N];
    while(i<N){
        cin>>array[i++];
    }
    for(int j=1;j<=N;++j){
        temp=0;
        for(int ij=0;ij<N;++ij)
        {
            if(array[ij]==j)
            {
                temp=1;
                break;
            }
        }
        if(temp==0){
            cout<<j;
            break;
        }
    }

    return 0;
}
