#include "stdio.h"
double power(double x,int n)
{
if (n==0)
return 1.0;
return power(x,n-1);
}
int main()
{ double x,a;
int n;
scanf("%lf,%d",&x,&n);
a=power(x,n);
printf("%g",a);
return 0;
}
