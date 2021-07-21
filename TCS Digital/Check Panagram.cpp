#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{   
    string s;
    cin>>s;
    int array[128]={0};
    for(int i=0;i<s.length();++i){
        if(s[i]>='A' && s[i]<='Z')
        {
            s[i]+=32;
        }
        array[s[i]]+=1;
    }
    
    for(int i=97;i<123;++i){
        if(!array[i]){
            cout<<"Not panagram";
            return 0;
        }
    }
    cout<<"Panagram";
    return 0;
}

/*
Logic

1.Take string as input from user
2.make an array of size 26
3.for loop which will iterate thourgh the string 
4. inside if check if the char is in caps convert it into lower and then convert it into lower case
5.add array[s[i]] value by 123

6. make an another for loop from 97 to 122('a' = 97 & 'z'=122)
7.if (!array[i]) true means array[i] is 0 which means from a to z 1 or more than 1 char is missing then print Not Panagram and return 0
8. if for loop completed then print Panagram
