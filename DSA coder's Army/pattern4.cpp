#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
   
    for (int  row = 1; row <= 5; row++)
    {
        for (int i = 1; i <=5-row; i++)    // print the first spaces
        {
            cout<<"  ";
        }
        for (int j = 1; j <= row; j++)  // print star left of the refrence
        {
            
            cout<<"*"<<" ";
            
        }
        for (int k = 1; k <row; k++)  // print star to the right of the reference
        {
           cout<<"*"<<" ";
        }
        
        
        cout<<endl;
        
    }
    /*
        * 
      * * *
    * * * * *
  * * * * * * * 
* * * * * * * * *
    */
    
    return 0;
}
