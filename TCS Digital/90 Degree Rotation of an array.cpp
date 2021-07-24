
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int array[n][n];
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j)
        {
            cin>>array[j][i];
        }
    }
    int arr[n][n];
    for(int i=0;i<n;++i){
        int k=0;
        for(int j=n-1;j>=0;--j)
        {
            arr[i][k++] = array[i][j];
        }cout<<"\n";
    }
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j)
        {
            cout <<arr[i][j]<<" ";
        }cout<<"\n";
    }
}
/*Logic:-
1.Taking input as transpose matrix
2.Making a new matrix as arr
3.Reversing the array each row and putting values to new array arr
*/