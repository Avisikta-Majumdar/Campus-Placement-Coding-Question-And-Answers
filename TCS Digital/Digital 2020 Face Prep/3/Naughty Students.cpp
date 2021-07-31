
#include<iostream>
#include<map>
#include<iterator>
using namespace std;

int main()
{
    int n;
    cin>>n;
    map<string , int> student;
    string name;
    while(n--){
        cin>>name;
        student[name]++;
    }
    map<string , int> ::iterator iter;
    for(iter=student.begin(); iter!=student.end();++iter)
    {
        cout<<iter->first<<" "<<(*iter).second<<endl;
    }

    return 0;
}
