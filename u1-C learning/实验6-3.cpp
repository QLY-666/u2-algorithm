#include <stdio.h>
int main()
{ int i=0;
  char ch[1000]; 
  scanf("%999[^\n]", ch);
  while (ch[i]!='\0') 
  { 
   ch[i]=ch[i]^15;
  i++;
  }
  printf("%s",ch);
 return 0;
}

