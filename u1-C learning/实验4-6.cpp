#include <stdio.h>
#include <math.h>

int main() {
  int n,sum=1;
  scanf("%d",&n);
  for(int i=1;i<n;i++) {
  sum=(sum+1)*2; 
  }
  printf("Titals=%d",sum);
	return 0;
}
