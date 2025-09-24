#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(int argc, char const *argv[])
{
    char str[20];
    int count[26]={0},index;
    printf("Enter the string : ");
    gets(str);
    printf("%s\n",str);
    for (int i = 0; str[i]!= '\0'; i++)
    {
        if (isalpha(str[i]))
        {
            index=(int)(str[i])-97;
            count[index]=count[index]+1;

        }
        
    }
    for (int i = 0; i < 26; i++)
    {
        if (count[i]!=0)
        {
            printf("%c = %d\n",i+97,count[i]);
        }
        
    }
    return 0;
}
