#include "stdio.h"
#include "string.h"
int findsubstring(char *s,char *sub)
{
  int len1=strlen(s),len2=strlen(sub);
  int flag;
    for(int i=0;i<=len1-len2;i++)
  {
    flag=1;
    for(int j=0;j<len2;j++)
   {
    if(s[i+j]!=sub[j])
    {
	 flag=0;       
	 break;
    }
  if(flag==1)
    {
	return i;
   }  
  }      
return -1;
}
}
int main()
{ char line[80],substr[10];
int index;
gets(line);
gets(substr);
index=findsubstring(line,substr);
if(index>=0)
printf("yes\n",index);
else
printf("no\n");
return 0;
}
