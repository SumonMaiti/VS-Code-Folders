#include<stdio.h>
#include<string.h>
#include<ctype.h>
int parity_checker(char *str,char parity_type)
{
    int count=0,length=strlen(str);
    for (int i = 0; i < length; i++)
    {
        if (str[i]=='1')
        {
            count++;
        }
        
    }
    
    switch (parity_type)
    {
        case 'o':
            if (count%2)
            {
                return 1;
            }
            else
                return 0;
            
            break;
        case 'e':
            if (!(count%2))
            {
                return 1;
            }
            else
                return 0;
            
            break;
        default:
            printf("\nNot a correct choice");
    }
}
int main()
{
    int i,n;
    char choose_parity,bit[20];
    printf("Enter the type of the parity(o for odd and e for even) : ");
    scanf("%c",&choose_parity);

    printf("\nEnter the bit = ");
    scanf("%s",bit); 
    printf("Your data bit is = %s",bit);

    int temp=parity_checker(bit,choose_parity);
    
    if (temp)
    {
        printf("\nNo error in the received data\n");
    }
    else
        printf("\n!!Warning!! error in the received data\n");
    return 0;
}
