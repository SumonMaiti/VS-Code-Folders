#include<stdio.h>
#include<math.h>
#define epsilon 0.0001
float f(float x){
    return (x*x*x-2*x-5);
}
float findx(float x1,float x2){
    return ((x1*f(x2)-x2*f(x1))/(f(x2)-f(x1)));
}

int main(int argc, char const *argv[])

{
    float x1,x2,x;
    int n,i;
    l  : printf("Enter the value of x1 : ");
    scanf("%f",&x1);
    printf("Enter the value of x2 : ");
    scanf("%f",&x2);
    printf("Enter maximum number of iteration : ");
    scanf("%d",&n);
    if(f(x1)*f(x2)>0){
        printf("points are invalid! please enter the points again...\n ");
        goto l;
    }
    else
        printf("Your points are x1= %f & x2= %f \n",x1,x2);
    
    x=findx(x1,x2);
    for(i=1;i<=n;i++)   
    {
        if (f(x)*f(x1)<0)
        {
            x2=x;
        }
        else
            x1=x;
        printf("Iteration = %d root = %f\n",i,x);
        float x3=findx(x1,x2);
        if (fabs(x3-x)<=epsilon)
        {
            printf("The root = %f",x);
            return 0;
        }
        x=x3;
        
    }
    printf("\nAfter %d iteration root = %f",i-1,x);
    
    return 0;
}
