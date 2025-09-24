#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
   
    
     for (int  row1 = 1; row1 <= 4; row1++)
    {
        for (int  j = 1; j <= 4-row1; j++)
        {
            cout<<" ";
        }
        
        for (int i = 1; i <=row1; i++)    // print the first stars
        {
            cout<<"* ";
        }
        
       
        cout<<endl;
/*
   * 
  * *
 * * *
* * * *
*/
    }
    for (int  row2 = 4; row2 >= 1; row2--)
    {
        for (int  j = 1; j <= 4-row2; j++)
        {
            cout<<" ";
        }
        for (int i = row2; i >=1; i--)    // print the first stars
        {
            cout<<"* ";
        }
        
        cout<<endl;
/*
* * * *
 * * *
  * *
   * 
*/
    }

    return 0;
}
    /*
   * 
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   * 
    */
    
