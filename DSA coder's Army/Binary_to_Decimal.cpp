#include<iostream>
#include<math.h>
using namespace std;
int main(int argc, char const *argv[])
{
    int binary,decimal=0,power=0;
    cout<<"Enter the binary number : ";
    cin>>binary;
    while (binary!=0)
    {
        int rem=binary%10;
        if (rem!=0 && rem!=1)
        {
            cout<<"the number is not a binary number"<<endl;
            return 0;
        }
        
        decimal+=rem*(pow(2,power));
        power++;
        binary=binary/10;
    }
    cout<<"The decimal value = "<<decimal;

    return 0;
}
