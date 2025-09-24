#include<iostream>
#include<math.h>
using namespace std;
int main(int argc, char const *argv[])
{
    int data,temp,rem,sum=0,dig=0;
    cout<<"Enter the number : ";
    cin>>data;
    temp=data;
    while (temp!=0)
    {
        
        dig++;
        temp=temp/10;
        
    }cout<<"dig= "<<dig<<endl;
    temp=data;
    while (temp!=0)
    {
        rem=temp%10;
       // cout<<"rem= "<<rem<<endl;
        sum+=pow(rem,dig);
        cout<<"sum = "<<sum<<endl;
        temp=temp/10;
    }
    cout<<"sum= "<<sum<<endl;
    if (sum==data)
    {
        cout<<"The number is an armstrong number"; 
    }
    else
    {
        cout<<"Not a armstrong number";
    }
 
    return 0;
}
