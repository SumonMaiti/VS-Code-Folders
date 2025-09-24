#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int i,j;
    for (int  i = 0; i <= 5; i++)
    {
        for (int j = 1; j <=i; j++)    
        {
            cout<<j<<" ";
        }
        cout<<endl;
        
    }
    /*
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 
    */
    
    return 0;
}
