#include<stdio.h>
int main(int argc, char const *argv[])
{
    int a[10],i,n;
    printf("Enter the max value : ");
    scanf("%d",&n);
    printf("Enter the elements one by one.......\n");
    for (int  i = 0; i < n; i++)
    {
        scanf("%d",&a[i]);
    }
    int pos;
    printf("Enter the position: ");
    scanf("%d",&pos);
    int data;
    printf("Enter the data; ");
    scanf("%d",&data);
    for (int i = n-1; i>=pos ; i--)
    {
        a[i+1]=a[i];
    }
    a[pos-1]=data;

    
    return 0;
}
