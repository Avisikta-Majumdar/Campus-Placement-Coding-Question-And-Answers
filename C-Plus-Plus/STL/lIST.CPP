#include<iostream>
#include<list>
#include<iterator>
using namespace std;
int main()
{
    list<int> lst;
    lst.push_front(5);
    lst.push_back(1);
    lst.push_front(15);
    lst.push_back(11);
    lst.push_front(45);
    lst.push_back(11);
    
    //Using iterator
    cout<<"Let's print values by using iterator:- \n";
    list<int>::iterator i;
    for(i=lst.begin();i!=lst.end();++i){
        cout<<(*i)<<" ";
    }
    cout<<endl;
    
    //sorting the list
    cout<<"Let's sort values:- \n";
    lst.sort();
    for(int i:lst){
        cout<<i<<" ";
    }
    cout<<endl;
    
    //using unique function to remove duplicate
    cout<<"Let's remove duplicate values:- \n";
    lst.unique();
    for(int i:lst){
        cout<<i<<" ";
    }
    
    return 1;
}

/*
OUTPUT
Let's print values by using iterator:- 
45 15 5 1 11 11 
Let's sort values:- 
1 5 11 11 15 45 
Let's remove duplicate values:- 
1 5 11 15 45 

*/
