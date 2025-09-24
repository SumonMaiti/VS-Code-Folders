#include<stdio.h>
float f(float x){
    return x*x*x;
}
int main()
{
    float a,b,interval,h,n;
    printf("Enter the upper limit : ");
    scanf("%f",&b);
    printf("Enter the lower limit : ");
    scanf("%f",&a);
    printf("Enter the no. of  intervals : ");
    scanf("%f",&n);
    h=(b-a)/n;
    float sum;
    sum=f(a)+f(b);
    for(float i=a+h;i<b;i+=h)
        sum=sum+(2*f(i));
    printf("sum= %f  h=%f",sum,h);
    sum=(h*sum)/2;
    printf("\n The answer= %f",sum);
    return 0;
}
