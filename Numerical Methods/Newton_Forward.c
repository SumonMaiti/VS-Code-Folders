#include<stdio.h>
int main(int argc, char const *argv[])
{
    float a[10][10],x,u;
    int i,n,j;
    printf("Enter the no. of values  : ");
    scanf("%d",&n);
    printf("Enter the values of x.........\n");
    for ( i = 0; i < n; i++)
    {
        scanf("%f",&a[i][0]);
    }
    printf("Enter the values of y.........\n");
    for ( i = 0; i < n; i++)
    {
        scanf("%f",&a[i][1]);
    }
    printf("The difference table is ........\n");
    for ( int j = 2; j <=n; j++)  //calculating forward difference teble
    {
        for (int  i = 0; i <= n-j; i++)
        {
            a[i][j]= a[i+1][j-1] - a[i][j-1]; 
        }
        
    }
    for (  i = 0; i < n; i++) // print the forward difference table
    {
        for (int  j = 0; j <=n-i; j++)// no of coloumn is decreasing that's why n-i
        {
            printf("%.2f  ",a[i][j]);
        }
        printf("\n");
        
    }
    
    printf("Enter the interpolating value  : ");
    scanf("%f",&x);
    float h= a[1][0]-a[0][0];
    u= (x-a[0][0])/h;
    int fact=1;
    float u1=u;
    float y=a[0][1];
    for (int  i = 2; i <= n; i++)
    {
        y=y+((u1*a[0][i])/fact);
        fact=fact*i;
        u1=u1*(u-(i-1));
    }
    printf("\nThe interpolating value of %f is %f",x,y);

    return 0;
}
