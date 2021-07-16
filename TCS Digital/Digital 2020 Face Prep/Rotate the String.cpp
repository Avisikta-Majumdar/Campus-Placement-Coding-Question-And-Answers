#include <iostream>
using namespace std;
int main() 
{
string a;
  cin>>a;
  int pos;
  cin>>pos;
  string direction;
  cin>>direction;
  if(direction=="L"){
  for(int i=0;i<a.length();++i){
    int val=(i+pos)%a.length();
    cout<<a[val];
  }return 0;
  }
  else{
  
  for(int i=0;i<a.length();++i){
    int val=(a.length()-pos+i)%a.length();
    cout<<a[val];
  }}

    return 0;
}