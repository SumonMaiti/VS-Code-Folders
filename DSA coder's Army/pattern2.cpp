#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
   
    for (int  row = 1; row <= 5; row++)
    {
        char ch='A';
        for (int i = 1; i <=5-row; i++)    
        {
            cout<<"  ";
        }
        for (int j = 1; j <= row; j++)
        {
            
            cout<<ch<<" ";
            ch=ch+1;
        }
        
        cout<<endl;
        
    }
    /*
        A 
      A B
    A B C
  A B C D 
A B C D E
    */
    
    return 0;
}
