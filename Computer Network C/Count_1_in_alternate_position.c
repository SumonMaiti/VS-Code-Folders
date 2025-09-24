#include<stdio.h>
#include<string.h>
int main(int argc, char const *argv[])
{
    char data[50];
    int count1=0,count2=0,count3=0;

    printf("\nEnter the data stream :");
    scanf("%s",data);
    printf("\nThe length of the data stream is : %d\n",strlen(data));
    for (int i = 0; i < strlen(data); i+=2)
    {
        if(data[i]=='1')
        count1++;
    }
    printf("\nA. 1 in every  alternate position is : %d",count1);

    for (int i = 1,j=2; i < strlen(data)||j < strlen(data); i+=4,j+=4)
    {
        if(data[i]=='1')
            count2++;
        if(data[j]=='1')
            count2++;
    }
    printf("\nB. 1 in every two alternate position is : %d",count2);

    
    for (int i = 3,j=4,k=5,l=6; i<strlen(data)||j<strlen(data)||k<strlen(data)||l<strlen(data);i+=8,j+=8,k+=8,l+=8)
    {
        if(data[i]=='1')
            count3++;
        if(data[j]=='1')
            count3++;
        if(data[k]=='1')
            count3++;
        if(data[l]=='1')
            count3++;
    }
    printf("\nC. 1 in every four alternate position is : %d",count3);
    return 0;
}
