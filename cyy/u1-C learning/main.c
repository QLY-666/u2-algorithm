#include <stdio.h>
int main()
{ int n;
  scanf("%d",&n);
  if(n>1&&n<=100)
  {
   int str[n];  
   for(int i=0;i<n;i++)
   {
    scanf("%d",&str[i]);
   }
    int x;
	scanf("%d",&x);
    int maxIndex=-1;
	for(int i=0;i<n;i++)
    {
	 if(str[i]==x)
	 {
	  maxIndex=i;
	 }
	}
  printf("%d",maxIndex);
  }
  return 0;
}
