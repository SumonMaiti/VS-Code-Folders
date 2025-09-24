#include<stdio.h>
int main(int argc, char const *argv[])
{
    int n;
    printf("Enter the number : ");
    scanf("%d",&n);
    while (n%2==0)
    {
        n/=2;
    }
    if (n==1)
    {
        printf("The number is power of 2");

    }
    else
    {
        printf("The number is not power of 2");
    }
    
    return 0;
}
