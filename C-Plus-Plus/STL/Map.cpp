#include<iostream>
#include<map>
#include<iterator>
using namespace std;
int main()
{
    map<string , int> Std;
    Std["avisikta"]=19;
    Std["jayita"]=62000;
    //Using iterator
    cout<<"Let's print values by using iterator:- \n";
    map<string , int>::iterator i;
    for(i=Std.begin();i!=Std.end();++i){
        cout<<(*i).first<<" "<<i->second<<endl;
    }
    cout<<endl;
    

    return 1;
}

/*
Let's print values by using iterator:- 
avisikta 19
jayita 62000



*/