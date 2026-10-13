#include <stdio.h>
int main() {
  int c,flag=1,b;
  scanf("%d",&c);
  for(int a=1;a<c&&flag;a++) {
  for(b=a;b<c&&flag;b++) {
  if(c*c==a*a+b*b) {
  printf("%d:yes",c);
  flag=0;
  }
  }
  }
  if(flag) {
  printf("%d:no",c);
  }
	return 0;
}
