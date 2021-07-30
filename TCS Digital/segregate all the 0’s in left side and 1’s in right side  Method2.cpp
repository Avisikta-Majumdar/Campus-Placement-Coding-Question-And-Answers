#include <iostream>
using namespace std;

int main() 
{
   int n,start=0;
  cin>>n;
  int array[n];

  for(int i=0;i<n;++i){
  
      cin>>array[i];
  }
  int left=0,right=n-1;
  while(1){
      if(left>=right){
          break;
      }
      if(array[left]==0)
      {
          left++;
      }
      else if (array[right]==1)
      {
          right--;
      }
      else{
          int temp;
          temp = array[left];
          array[left]=array[right];
          array[right]  = temp;
          right--;
          left++;
      }
      
  }
  for(int i=0;i<n;++i)
    cout<<array[i]<<"";
    return 0;
}