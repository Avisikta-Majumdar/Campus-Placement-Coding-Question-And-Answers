#include <iostream>
#include <string>

using namespace std;
int main()
{
   int number;
 cin>>number;
 int array[26]={0};
 string Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 array[0]=1;
 int count=2;
 for(int i=1;i<26;++i)
 {
     array[i] = count*array[i-1] + array[i-1];
     count++;
 }


 string s="";
 int start=0;
 while(number>0){
     start=0;
  //   cout<<"Inside while loop first \n";
    while(number>=array[start]){
        //cout<<"Inside 2nd while loop\n"<<number<<"  "<<array[start]<<endl;
        //cout<<array[start]<<"  ";
        start++;
    } 
    start--;
    number-=array[start];
    s.push_back(Letters[start]);
  //  cout<<"After pussing "<<Letters[start]<<" now number = "<<number<<endl;
 }

 for(int i=s.length();i>=0;--i){
     cout<<s[i];
 }

    return 0;
}
