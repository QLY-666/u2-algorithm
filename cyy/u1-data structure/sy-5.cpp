#define MaxSize 100
#include <stdio.h>
#include<string.h>
#define Maxlength 100


typedef struct
{
    char str[MaxSize];
    int length;
} String;

int Insert(String *S, int pos, String T)
/*在串S的pos位置插入子串T*/
{
    int i;
    if(pos < 0)
    {
        printf("参数pos出错！");
        return 0;
    }
    else if(S->length + T.length > MaxSize)
    {
       printf("数组空间不足无法插入！");
        return 0;
    }
	else
    {
        for(i = S->length-1; i >= pos; i--)
            S->str[i+T.length] = S->str[i];     /*为插入做准备*/
        for(i = 0; i < T.length; i++)
            S->str[pos+i] = T.str[i];               /*插入*/
        S->length += T.length;                      /*产生新的元素个数*/
        return 1;
    }
}

int Delete(String *S, int pos, int len)
{
    int i;
    if(S->length <= 0)
    {
        printf("数组中未存放字符无元素可删! ");
        return 0;
    }
    else if(pos < 0 || len < 0 || pos+len > S->length)
   {
        printf("参数pos和len出错");
        return 0;
    }
    else
    {
        for(i = pos+len; i <= S->length-1; i++)
            S->str[i-len] = S->str[i];              /*依次前移*/
        S->length -= len;                       /*产生新的长度值*/
        return 1;
    }
}

int BFIndex(String *S, int start, String T)
{ 
 if(S->str[0]=='\0'||T.str[0]=='\0'||T.length>S->length||T.length==0)
 {
  printf("参数不合法！");
  return -1;
 }
 int i=start;
 int j=0;
 while(i<S->length&&j<T.length)
 {
  if(S->str[i]==T.str[j])
  {
   i++;
   j++;
  }
  else
  {
   i=i-j+1;
   j=0;
  }
 }
 if(j==T.length)
 return i-T.length;
 else
 return -1;
}

int Replace(String *s,int start,String t,String v)
{
 int pos=BFIndex(s,start,t);
 int lens=s->length,lent=t.length,lenv=v.length;
 if(pos>=0)
 {
  int newlength=s->length-t.length+v.length;
  if(newlength>MaxSize)
  {
   printf("长度超出范围！");
   return 0;
  }
  if(v.length<t.length) 
  {
   for(int i=pos+t.length;i<s->length;i++)
   {
    s->str[i-(lent-lenv)]=s->str[i];
   }
  }
  else if(v.length>t.length)   
  {
   for(int i=s->length-1;i>=pos+lent;i--)
   {
    s->str[i+(lenv-lent)]=s->str[i];
   }
  }
  for(int i=0;i<lenv;i++)
   s->str[pos+i]=v.str[i];
  s->length=newlength;
  return 1;
 }
return 0;
}

int main(void)
{
      String myString1,myString2,myString3;
       int i,start=0;
      printf("请输入主串");
       scanf("%s",myString1.str );
       printf("请输入子串 ");
       scanf("%s",myString2.str);
       printf("请输入要替换的串 ");
       scanf("%s",myString3.str);
       myString1.length=strlen(myString1.str);
       myString2.length=strlen(myString2.str);
       myString3.length=strlen(myString3.str);
       if(Replace(&myString1,start,myString2,myString3)==0)
              printf("不成功 ");
       else
              for(i=0;i<myString1.length ;i++)
              printf("%c",myString1.str[i]);
}