#include <stdio.h>
int main()
{ int n,i,j,count=0;
  scanf("%d",&n);
  for(i=1;i<=n;i++)
  {for(j=0;j<=n-1;j++)
   { count++;}   
   }
  printf("%d\n",count); 
  return 0;
}
