#include <stdio.h>
void f(int*a,int*b)
{
  int t=*a;
  *a=*b;
  *b=t;
}
int main() {
  int a=4,b=7;
  printf("a=%d a=%d\n",a,b);
  f(&a,&b);
  printf("a=%d a=%d\n",a,b);
  int c[3]={1,3,5};
   int*p=c; 
   printf("%d",(p+1));
 return 0;
}
