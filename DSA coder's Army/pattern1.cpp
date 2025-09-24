#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int i,j;
    for (int  row = 1; row <= 5; row++)
    {
        for (int i = 1; i <=5-row; i++)    
        {
            cout<<"  ";
        }
        for (int i = 1; i <= row; i++)
        {
            cout<<"*"<<" ";
        }
        
        cout<<endl;
        
    }
    /*
        * 
      * *
    * * *
  * * * *
* * * * *
    */
    
    return 0;
}
