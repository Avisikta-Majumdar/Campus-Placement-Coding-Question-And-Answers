#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    int size,k;
    cin>>size>>k;
    int array[size];
    for(int i=0;i<size;++i)
    cin>>array[i];
    sort(array,array+size);
    for(int i=0;i<size;++i)
    cout<<array[i]<<"  ";
    cout<<"\n"<<array[size-k];
}

/*Cognizant Genc Next Coding Questions

Question :- https://youtu.be/Q1VsJfUn0jM
*/