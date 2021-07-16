#include <iostream>
using namespace std;
int prime(int a){
  int i;
for( i=2;i<a;++i){
if(a%i==0)
  return 0;
}
  if(i==a)return 1;
}
int Value(int n){int i;
for(i=0;i<=10000;++i){
if(prime(n-i)){
cout<<(n-i)<<endl;
  return 0;
}
  else if(prime(n+i)){
  cout<<(n+i)<<endl;
    return 0;
  }
  else continue;
}
}
int main() 
{
   int size;
  cin>>size;
  while(size--){
  int value;
    cin>>value;
    Value(value);
  }
    return 0;
}