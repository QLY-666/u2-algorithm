#include <stdio.h>
int main()
{  char str[1000];
   scanf("%[^\n]", str);
   for(int i=0;str[i]!='\0';i++)
   {
    char ch = str[i];
	if(ch>='a'&&ch<='z')
	{
	str[i]=219-ch;
	}
    if(ch>='A'&&ch<='Z')
	{
	str[i]=155-ch;
	}
    if(ch>='0'&&ch<='9')
	{
	str[i]=105-ch;
	}
   }
   printf("%s\n",str);












   return 0;
}
