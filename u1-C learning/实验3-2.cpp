#include <stdio.h>
#include <math.h>
int main()
{  double x1,y1,x2,y2,x3,y3;
   scanf("%lf,%lf",&x1,&y1);
   scanf("%lf,%lf",&x2,&y2);
   scanf("%lf,%lf",&x3,&y3);
   double a,b,c,p,area;
   a = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
   b = sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
   c = sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
   p = (a+b+c)/2;
   area=sqrt(p*(p-a)*(p-b)*(p-c));
   if(area==0) {
   printf("Impossible");
   } else {
   printf("primeter=%.2f,area=%.2f",a+b+c,area);
   }
   return 0;
}
