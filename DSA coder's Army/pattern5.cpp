#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
   
    for (int  row = 5; row >= 1; row--)
    {   for (int  k = 5-row; k >= 1; k--)
        {
            cout<<"  ";
        }
        for (int i = row; i >=1; i--)    // print the first spaces
        {
            cout<<"* ";
        }
        
        
        for (int j = row-1; j >= 1; j--)  // print star left of the refrence
        {
            
            cout<<"* ";
            
        }
        cout<<endl;
        
    }
    /*
* * * * * * * * * 
  * * * * * * * 
    * * * * *
      * * * 
        *
    */
    
    return 0;
}
