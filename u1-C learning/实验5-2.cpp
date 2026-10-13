#include <stdio.h>
#include <math.h>
int IsPrime(int x) {
  if(x==1) return 0;
  for(int i=2;i<=x-1;i++) {
  if(x%i==0) {
  return 0;
  } 
  }
  return 1;
}
int main() {
    int a,n,b,c;
	scanf("%d,%d",&a,&n);
	b=a; 
	for(int i=1;i<=n;) {
	if(IsPrime(b)) {
	c=b+2;
	if(IsPrime(c)) {
	printf("%d:%d\n",b,c); 
	i++;
	}
	}	
	b++;
	} 	
    return 0;
}
