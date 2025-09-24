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
    
    l: printf("Enter the interpolating value  : ");
    scanf("%f",&x);
    float h= a[1][0]-a[0][0];
    u= (x-a[n-1][0])/h;
    int fact=1;
    float u1=u;
    float y=a[n-1][1];
    j=2;
    for (int  i = n-2; i >= 0; i--)
    {
        y=y+((u1*a[i][j])/fact);
        fact=fact*j;
        u1=u1*(u+(j-1));
        j++;
    }
    int q;
    printf("\nThe interpolating value of %f is %f",x,y);
    printf("repeat? 0 to exit 1 to again reapeat  :");
    scanf("%d",&q);
    if(q==0)
        return 0;
    else
        goto l ; 
    return 0;
}
