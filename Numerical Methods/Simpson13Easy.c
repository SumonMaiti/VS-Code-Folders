#include<stdio.h>
float f(float x){
    return 1/(1+(x*x));
}
int main()
{
    float a,b,h,n;
    printf("Enter the upper limit : ");
    scanf("%f",&b);
    printf("Enter the lower limit : ");
    scanf("%f",&a);
    printf("Enter the no. of  intervals : ");
    scanf("%f",&n);
    h=(b-a)/n;
    float sum;
    sum=f(a)+f(b);
    int count=1;
    for(float i=a+h;i<b;i+=h){
        if(count%2==0)
            sum=sum+(2*f(i));
        else
            sum=sum+(4*f(i));
        count++;
    }
    //printf("sum= %f  h=%f",sum,h);
    sum=(h*sum)/3;
    printf("\n The answer= %f",sum);
    return 0;
}
