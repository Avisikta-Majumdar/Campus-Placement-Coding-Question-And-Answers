#include<iostream>
using namespace std;

int main()
{
    int size;
    cin>>size;
    int array[size];
    for(int i=0;i<size;++i)
    cin>>array[i];
    
    int newArray[size];
    for(int i=0;i<size;++i){
        int mult=1;
        for(int j=0;j<size;++j){
            if(i!=j){
                mult*=array[j];
            }
        }newArray[i] = mult;
    }

    //Printing the Updated array
    for(int i=0;i<size;++i)
    cout<<newArray[i]<<" ";
    return 0;
}

/* Question :- https://youtu.be/4x9j3vMO3nk  */
