#include <stdio.h>
#include<stdlib.h>
int main()
{
char ch;
int total=0,number=0,word=0,other=0,space=0; 
while((ch=getchar())!='\n')
{
 total++;
 if (ch>='0'&&ch<='9')
 number++;
 if ((ch>= 'A' &&ch <= 'Z') || (ch>= 'a' &&ch<= 'z'))
 word++;
 if(ch=' ')
 space++;
 else 
 other++;
}
 printf("total=%d\n",total);
 printf("number=%d\n",number);
 printf("word=%d\n",word);
 printf("other=%d\n",other);
 printf("space=%d\n",space);

 return 0;
}
