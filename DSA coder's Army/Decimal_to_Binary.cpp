#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int n,i,a[10],index=0;
    cout<<"Enter the decimal data  : ";
    cin>>n;
    while (n!=0)
    {
        int rem=n%2;
        a[index]=rem;
        index++;
        n=n/2;
    }
    cout<<"The binary conversion is : ";
    for (int  i = index-1; i >=0; i--)
    {
        cout<<a[i];
    }
    
    
    return 0;
}
  
