#include<stdio.h>
int main()
{
    float x[20],y[20],xv;
    int n,i,j;
    printf("Enter the no. of terms : ");
    scanf("%d",&n);
    printf("Enter the values of x : ");
    for(int i=0;i<n;i++)
        scanf("%f",&x[i]);
    printf("Enter the values of y : ");
    for(int i=0;i<n;i++)
        scanf("%f",&y[i]);
    printf("Enter the interpolation value  : ");
    scanf("%f",&xv);
    printf("Your values are.............\n");
    for(i=0;i<n;i++)
        printf("%f   ",x[i]);
    printf("\n");
    for(i=0;i<n;i++)
        printf("%f   ",y[i]);    
    float sum=0;
    for(i=0;i<n;i++){// this for loop for 4 no. of terms.
        float mul=1.0;// every time for one group multiplication factor will be 1.
        for(j=0;j<n;j++){
            if(i!=j)
                mul=mul*((xv-x[j])/(x[i]-x[j]));// standard formula
        }
       // mul=mul*y[i];
        sum+=(mul*y[i]);//multiplying with y term and adding with previous sum
    }    
    printf("interpolation value= %f",sum);
    return 0;
}
