#include <stdio.h>
#include <string.h>
int main()
{
char a[10000];
int word=0,i=0;
gets(a); 
int n=strlen(a);
while(i<=n-1)
{
 if(a[i]!=' '&&(a[i+1]==' '||a[i+1]=='\0'))
 {
 word++;
 }
 i++;
}
 printf("word=%d\n",word);
 return 0;
}
