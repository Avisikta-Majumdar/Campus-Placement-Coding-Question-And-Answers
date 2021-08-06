#include<iostream>
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
int main(){
    string names[30]={"Ajay","Bijay","Sanjay","Majay"};
    cout<<names[0][0];
    names[4] =names[2].substr(3,5) ;// substring : - jay 
    cout<<"\n"<<names[4];
}

/*OUTPUT 
jay
*/