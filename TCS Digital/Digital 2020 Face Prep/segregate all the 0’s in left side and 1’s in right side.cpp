#include <iostream>
using namespace std;

int main() 
{
   int n,start=0;
  cin>>n;
  int array[n];
  int end=n-1;
  for(int i=0;i<n;++i){
  int value;
    cin>>value;
    if(value==0){
    array[start++]=0;
    }
    else if(value==1){
    array[end--]=1;
    }
  }
  for(int i=0;i<n;++i)
    cout<<array[i]<<"";
    return 0;
}