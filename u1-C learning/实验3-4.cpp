#include <stdio.h>
int main()
{  int n;
   scanf("%d",&n);
   if(n%5==0&&n%7==0){
   printf("A");
   } 
   else if(n%5==0&&n%7!=0) {
   printf("B");
   }
   else if(n%5!=0&&n%7==0) {
   printf("C");
   }
   else {
   printf("D");
   }
  return 0;
}
