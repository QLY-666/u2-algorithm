#include "stdio.h"
struct complex complexproduct(struct complex s1,struct complex s2);
struct complex
{ double sb;
double xb;
};
int main()
{ struct complex c1,c2,c3;
scanf("%lf,%lf",&c1.sb,&c1.xb);
scanf("%lf,%lf",&c2.sb,&c2.xb);
c3=complexproduct(c1,c2);
printf("%g,%g\n",c3.sb,c3.xb);
return 0;
}
struct complex complexproduct(struct complex s1,struct complex s2)
{
 struct complex s3;
 s3.sb=s1.sb*s2.sb-s1.xb*s2.xb;
 s3.xb=s1.sb*s2.xb+s2.sb*s1.xb;
 return s3;             
}
