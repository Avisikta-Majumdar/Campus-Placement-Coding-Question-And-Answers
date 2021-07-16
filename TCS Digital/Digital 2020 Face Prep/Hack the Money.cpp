#include <iostream>
using namespace std;
bool Hack(int target , int current){
if(current==target){return true;}
else if(current>target){return false;}
else{
if(Hack(target,10*current)){return true;}
if(Hack(target,20*current)){return true;}
}
  return false;

}
int main() 
{
   int test;
  cin>>test;
  while(test--){
    int target;
    cin>>target;
  if(Hack(target,1)){
   cout<<"Yes\n";}
  else{
  cout<<"No\n";  }
  }
    return 0;
}