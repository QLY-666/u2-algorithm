#include <stdio.h>
#include <math.h>
int heshu(int x) {
  if(x==1) return 0;
  for(int i=2;i<=x-1;i++) {
  if(x%i==0) {
  return 1;
  } 
  }
  return 0;
}
int sushu(int x) {
  if(x==1) return 0;
  for(int i=2;i<=x-1;i++) {
  if(x%i==0) {
  return 0;
  } 
  }
  return 1;
}


int main() {
   int n,x=0,first=1;
   scanf("%d",&n);
   if(heshu(n)) {
   printf("%d=",n);
   for(int k=2;k<=n;) {
   while(n%k==0&&sushu(k)) {
   if(first==1) {
   printf("%d",k);
   first=0;
   n=n/k;
   } else {
   printf("*%d",k);
   n=n/k;
   }
   }
   k++;
   }
   } 
    return 0;
}
