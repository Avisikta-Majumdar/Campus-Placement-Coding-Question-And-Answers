//Robot move  
#include<iostream>
using namespace std;
int total_moves(int curr_row, int curr_col , int row, int col)
{
    if (curr_col==col && curr_row==row)
    return 1;
    if(curr_row>row || curr_col>col)
    return 0;
    
    return total_moves(curr_row+1,curr_col ,row, col)+total_moves(curr_row,curr_col+1 ,row,col);
    //     Moving 1 step toward downward                Moving 1 step towards right side
}
int main(){
    int row,col;
    cin>>row>>col;
    cout<<total_moves(0,0,row-1 , col-1);
    return 0;
}