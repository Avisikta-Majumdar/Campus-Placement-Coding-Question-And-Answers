#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
   int testcase;
   //cout<<"No of Testcase ";
   cin>>testcase;
   while(testcase--){
     int size;
    // cout<<"Size of the array ";
     cin>>size;
     int array[size];
     for(int i=0;i<size;i++){
       // cout<<"Insert "<<i+1<<"th element :- ";
        cin>>array[i];
     }
      int start = 0 ,end=size-1 , count=0;
      while(start<end){
      if(array[start]==array[end]){
      		start++;
			end--;
      }
      else if(array[start]>array[end]){
      array[end-1]+= array[end];
        end--;
        count++;
      }
      else if(array[start]<array[end]){
      array[start+1] += array[start];
      start++;
      count++;
      }

      }
      cout<<"\n"<<count<<endl;
   }
    return 0;
}
/* Question :- Face Prep Stage 2 question 7*/
