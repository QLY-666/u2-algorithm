#include "stdio.h"
struct Time
{ int hour;
int minute;
int second;
};
int main()
{ int n;
struct Time t1;
int a,b;
scanf("%d:%d:%d",&t1.hour,&t1.minute,&t1.second);
scanf("%d",&n);

 t1.second=n+t1.second;
 a=t1.second/60;
 t1.second%=60;
 
 t1.minute+=a;
 b=t1.minute/60;
 t1.minute%60;
 
 t1.hour+=b;
 t1.hour%=24;
 
 printf("%d:%d:%d",t1.hour,t1.minute,t1.second);







return 0;
}
