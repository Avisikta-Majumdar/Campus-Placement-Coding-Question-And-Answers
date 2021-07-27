#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    string time;
    cin>>time;
    int hour,minute,required_minute=0;
    hour = (time[0]-48)*10 + (time[1]-48);
    minute = (time[3]-48)*10 + (time[4]-48);
    while((hour%10 !=minute/10)||(hour/10 != minute%10)){
        minute++;
        required_minute++;
        if(minute==60){
            minute=0; 
            hour+=1;
        }
        else if(hour==24){
            hour=0 ;
        }
    } 
    
    cout<<required_minute;
    return 0;
}