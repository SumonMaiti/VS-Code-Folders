#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(int argc, char const *argv[])
{
    char data[50];
    int alpha_flag=1,digi_flag=1,flag_01=1;

    printf("\nEnter the data stream :");
    scanf("%s",data);
    int len=strlen(data);
    for (int i = 0; i < len; i++)
    {
        if (!isalpha(data[i]))
        {
            alpha_flag=0;
            
        }
        if (!(data[i]>='2' && data[i]<='9'))
        {
            digi_flag=0;
            
        }
        if (data[i]!='1'&&data[i]!='0')
        {
            flag_01=0;
        } 
        

    }
    if (alpha_flag==1)
    {
        printf("\nThe string only contain alphabet");
    }
    if (digi_flag==1)
    {
        printf("\nThe string only contain digits");
    }
    if (flag_01==1)
    {
        printf("\nThe string only contain 0 and 1");
    }
    if (alpha_flag==0 && digi_flag==0 && flag_01==0)
    {
        printf("\nThe string doesn't contain only alphabet or digit or 0&1");
    }
    
    
}