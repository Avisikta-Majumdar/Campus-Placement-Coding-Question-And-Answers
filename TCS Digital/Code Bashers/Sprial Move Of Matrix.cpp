#include<iostream>
using namespace std;
/*QUESTION:- https://youtu.be/rBka1G7t_GI*/
int main()
{

    int row,col;
    cin>>row>>col;
    int array[row][col];
    for(int i=0;i<row;++i){
        for(int j=0;j<col;++j)
        {
            cout<<"Enter value for array of row "<<i<<" and col "<<j<<": ";
            cin>>array[i][j];
        }
    }
    int start_row=0,start_col=0, end_row = row-1, end_col= col-1;
    int i=0;
    while(i<row*col)
    {int j;
        for(j=start_col;j<=end_col;++j)
        {
            cout<<array[start_row][j]<<" ";
            ++i;
        }
        //All the values of start_row has printed that's why we are making start_row+=1
        start_row++;
        for(j=start_row;j<=end_row;++j){
            cout<<array[j][end_col]<<" ";
            ++i;
        }
        //All the values of end_col now printed that's why we are making end_col-=1
        end_col--;
        for(j=end_col;j>=start_col;--j){
            cout<<array[end_row][j]<<" ";
            i++;
        }
        //All the values of end_row has printed now that's why we are making end_row-=1
        end_row--;
        for(j=end_row;j>=start_row;--j){
            cout<<array[j][start_col]<<" ";
            ++i;
        }
        //All the values of start_col has printed now so we are making start_col+=1
        start_col++;
    }
    return 0;
}
