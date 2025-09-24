#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
   
    
     for (int  row1 = 1; row1 <= 4; row1++)
    {
        for (int i = 1; i <=row1; i++)    // print the first stars
        {
            cout<<"* ";
        }
        for (int j = 1; j <= (4-row1)*2; j++)  // print the middle spaces
        {
            cout<<"  ";
        }
        for (int k = 1; k <=row1; k++)  // print star to the right of the reference
        {
           cout<<"* ";
        }
        cout<<endl;
/*
        *             * 
        * *         * *
        * * *     * * *
        * * * * * * * *
*/
    }
    for (int  row2 = 3; row2 >= 1; row2--)
    {
        for (int i = row2; i >=1; i--)    // print the first stars
        {
            cout<<"* ";
        }
        for (int j = 1; j <= (4-row2)*2; j++)  // print the middle spaces
        {
            cout<<"  ";
        }
        for (int k = row2; k >=1; k--)  // print star to the right of the reference
        {
           cout<<"* ";
        }
        cout<<endl;
/*
        * * *     * * *
        * *         * *
        *             *
*/
    }

    return 0;
}
    /*
*             * 
* *         * *
* * *     * * *
* * * * * * * *  <-  dividing point there two for loops are required
* * *     * * *
* *         * *
*             *
    */
    
