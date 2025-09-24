#include<stdio.h>
#include<math.h>
int main(){
	float x0,xn,y[10],res[10][10],X,s,u,h,p=1.0;
	int i,j,n;
	printf("Enter total no of value: ");
	scanf("%d",&n);
	printf("\nEnter the value of x0: ");
	scanf("%f",&x0);
	printf("\nEnter the value of xn: ");
	scanf("%f",&xn);
	printf("\nEnter the arguments: ");
	for(i=0;i<n;i++){
		scanf("%f",&y[i]);
	}
	printf("\nEnter your interpolating point: ");
	scanf("%f",&X);
	h=(xn-x0)/n;
	u=(X-x0)/h;
	s=y[0];
	for(i=0;i<n;i++){
		res[i][0]=y[i];
	}
	for(i=1;i<n;i++){
		for(j=0;j<n-i;j++){
			res[i][j]=res[j+1][i-1]-res[j][i-1];
		}
	}
	printf("Your forward table: \n");
	for(i=0;i<n;i++){
		printf("\n");
		for(j=0;j<n;j++){
			printf("%f",res[i][j]);
		}
		printf("\n");
	}
	for(i=1;i<n;i++){
		s=y[0];
		p=p*(u-i+1)/i;
		s=s+p*res[i][0];
	}
	printf("Value at X=%f is sum=%f",X,s);
	return 0;
}