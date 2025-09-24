#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int i,j;
    for (int  i = 5; i >=1; i--)// row 
    {
        for (int j = 5; j >=i; j--)    // coloumn
        {
            cout<<j<<" ";
        }
        cout<<endl;
        
    }
    /*
    5 
    5 4 
    5 4 3 
    5 4 3 2 
    5 4 3 2 1 
    */
    
    return 0;
}
