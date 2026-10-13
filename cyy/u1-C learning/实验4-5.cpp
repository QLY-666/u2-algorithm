#include "stdio.h"
int main()
{  double a=1.0,b=2.0,t,n,sum=2.0;
   scanf("%lf",&n); 
   for(int i=1;i<=n-1;i++) {
   t=b;
   b=a+b;
   a=t;
   sum+=b/a;
   }	
   printf("s=%.2f",sum);
   return 0;
}
