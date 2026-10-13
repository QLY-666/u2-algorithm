#include <stdio.h>
#include <math.h>
int main() {
    double x,sum=1.0,term=1.0,n=1.0;
    scanf("%lf",&x);
    while(fabs(term)>1e-5 ) {
	term=term*x/n;
	sum=sum+term;
	n++;
	}
	printf("%.4f",sum);

   return 0;
}
