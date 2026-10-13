#include <stdio.h>
int even(int n)
{ if(n%2==0) 
  {
  return 0;
  } else {
  return 1;
  }
} 
int main()
{ int a,b,i;
  scanf("%d %d",&a,&b);
  int sum=0;
  for(i=a;i<=b;i++) 
  {if (even(i))
   sum=i+sum;
  }
  printf("%d\n",sum);
  return 0;
}

