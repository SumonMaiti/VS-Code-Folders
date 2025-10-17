#include<stdio.h>
void main()
{
    int Basic,DA,HRA,Net,Tax,Gross;
    printf("Enter Basic Salary");
    scanf("%d",&Basic);
    printf("Enter your DA percentage");
    scanf("%d",&DA);
    Tax=200;
    DA=Basic*15/100;
    HRA=Basic*15/100;
    Net=Basic+DA+HRA;
    Gross=Net-Tax;
    printf("\nYour salary is\t\t %d\n",Basic);
    printf("Your DA is\t\t %d \n",DA);
    printf("Your DA is\t\t %d \n",HRA);
    printf("Your Net Salary is\t %d\n",Net);
    printf("Your Gross Salary is \t %d\n",Gross);
}