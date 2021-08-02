#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str;
    getline(cin,str);
    int NoOfVowels=0;
    for(int i=0;str[i];++i){
        if((str[i]=='a')||(str[i]=='e')||(str[i]=='i')||(str[i]=='o')||(str[i]=='u')||(str[i]=='A')||(str[i]=='E')||(str[i]=='I')||(str[i]=='O')||(str[i]=='U'))
        NoOfVowels++;
    }
    cout<<NoOfVowels;
    return 0;
}


/*MINDTREE CODING QUESTION 
Question:- https://youtu.be/_pSx8ndzCjg
*/