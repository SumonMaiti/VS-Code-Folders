#include <stdio.h>
#include <string.h>
void main()
{
    char data[50],data1[20]={'\0'};
    int dl,sl,i,j,c=0,d=1,e=0,segment[20];
    printf("\nInput:");
    scanf("%s",data);
    dl=strlen(data);
    printf("\nSegment length: ");
    scanf("%d",&sl);
    printf("\nString length: %d\n",dl);
    if(dl%sl)
    {
        i=sl-(dl%sl);
        for(j=0;j<i;j++){
            data1[j]='0';
           // printf("inside for lop");
        }
        strcat(data1,data);
        //printf("after concatenation");
        strcpy(data,data1);
        dl=dl+i;
        printf("After zero padding the string is : %s\n",data);
    }
    
    for (int i = 0; i < dl/sl; i++)
    {
        
        c=i*sl;
        printf("\nSegment %d = ",i+1);
        while (c<(i+1)*sl)
        {
            printf("%c",data[c]);
            
            c++;
        }
        c=i*sl;
        int count=0;
        while (c<(i+1)*sl)
        {
            if (data[c]=='1')
            {
                count++;
            }
            c++;
        }
        //printf("\nFrequency of segment %d = %d",i+1,count);
        segment[i]=count;
    }
    for (int i = 0; i < dl/sl; i++)
    {
        printf("\nFrequency of segment %d = %d",i+1,segment[i]);
    }
    
} 