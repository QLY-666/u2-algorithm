#include <stdio.h>
int main()
{ double n;
  scanf("%lf",&n);
  if(n<=100)
  {printf("%.2f",n*0.51); 
  } else {
   printf("%.2f",51+(n-100)*0.65);
  }
  return 0;
}


