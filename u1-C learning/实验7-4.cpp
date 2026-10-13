#include <stdio.h>
#include <math.h>
int IsPrimer(int num)
{    int i,flag=num>1?1:0;
     for(i=2;i<=sqrt(num)&&flag;i++)
          if(num%i==0)
               flag=0;
     return flag;
}
int main()
{   int a[100],n,i,j,temp;
    scanf("%d",&n);
    for(i=0;i<n;i++)
         scanf("%d",&a[i]);
    i=0,j=n-1;
    while(i<j)
	{
        while (IsPrimer(a[i])==0)
            i++;
        while (IsPrimer(a[j])==1)
            j--;
        if (i < j){
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
	}
    for(i=0;i<n;i++)
         printf("%5d",a[i]);
    return 0;
}
