#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int i,j;
    for (int  i = 5; i >= 1; i--)// row 
    {
        for (int j = 1; j <=i; j++)    // coloumn
        {
            cout<<j<<" ";
        }
        cout<<endl;
        
    }
    /*
    1 2 3 4 5 
    1 2 3 4
    1 2 3
    1 2
    1
    */
    
    return 0;
}
