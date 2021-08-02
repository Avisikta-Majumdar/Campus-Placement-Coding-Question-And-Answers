#include<iostream>
using namespace std;
int main()
{
    printf("Hello World\n");
    string name[3]={"dfghj","rtyui"};
    //cout<<name[0];
    //cout<<"\n"<<name[1][0];
    name[2] = name[0]+name[1];
    cout<<name[2];
    return 0;
}
