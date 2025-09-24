#include<stdio.h>

int parity_generator(int *arr,int n,char parity_type)
{
    int count=0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i]==1)
        {
            count++;
        }
        
    }
    
    switch (parity_type)
    {
        case 'o':
            if (count%2==0)
            {
                arr[n]=1;
            }
            else
                arr[n]=0;
            
            break;
        case 'e':
            if (count%2==0)
            {
                arr[n]=0;
            }
            else
                arr[n]=1;
            
            break;
    }
    return count;
}
int main()
{
    int bit[20],i,n;
    char choose_parity;
    printf("Enter the type of the parity(o for odd and e for even) : ");
    scanf("%c",&choose_parity);
    printf("Enter total no. of bits : ");
    scanf("%d",&n);
    printf("\nEnter the bit .....\n ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&bit[i]);
    }   
    printf("Your data bit is...........\n ");
    for (int i = 0; i < n; i++)
    {
        printf("%d",bit[i]);
    }   
    int count=parity_generator(bit,n,choose_parity);
    printf("\nTotal no. of 1 is %d\n",count);
    printf("After adding parity bit the data bit is...........\n");
    for (int i = 0; i <= n; i++)
    {
        printf("%d",bit[i]);
    }   
    return 0;
}
