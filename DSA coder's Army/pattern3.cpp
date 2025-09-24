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
            
            cout<<j<<" ";
            
        }
        for (int k = row-1; k >=1; k--)  // print star to the right of the reference
        {
           cout<<k<<" ";
        }
        
        
        cout<<endl;
        
    }
    /*
        1 
      1 2 1
    1 2 3 2 1 
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
    */
    
    return 0;
}
