#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100

typedef struct {
 int stack[MAX_SIZE];
 int top;
}SequenceStack;

void StackInitiate(SequenceStack*s)
{
 s->top=0;
}

int StackNotEmpty(SequenceStack *s)
{
 if(s->top==0)
 {
  return 0;
 }
 else return 1;
}

int StackPush(SequenceStack*s,int x)
{
 if(s->top>=MAX_SIZE)
 {
  printf("栈已满，无法插入！");
  return 0; 
 }
 else 
 {
  s->stack[s->top]=x;
  s->top++;
  return 1;
 }
}

int StackPop(SequenceStack*s,int* x)
{
 if(s->top==0)
 {
  printf("无元素可以出栈！");
  return 0; 
 }
 else 
 {
  s->top--;
  *x=s->stack[s->top];
  return 1;
 }
}

void conversion()
{
 int decimal,jinzhishu,N;
 SequenceStack myStack;
 StackInitiate(&myStack);
 printf("输入要转换的进制(2~16)：\n"); 
   scanf("%d",&N);
  printf("输入要转换的十进制数N：\n"); 
scanf("%d",&decimal);
 while(decimal>0)
 {
  StackPush(&myStack,decimal%N);
  decimal = decimal / N;
 }
 printf("对应%d进制数为：",N); 
 while(StackNotEmpty(&myStack))
 {
  StackPop(&myStack,&jinzhishu);
  if(jinzhishu<10)
  {
    printf("%d ",jinzhishu); 
  } else {
    printf("%c ",jinzhishu + 'A' - 10); 
  }
 }
printf("\n");
}

int kuohaocheck(char *expr)
{
 int lens=strlen(expr);
 char c;
 int topc;
 SequenceStack myStack;
 StackInitiate(&myStack);
 for(int i=0;i<lens;i++)
 {
  c=expr[i];
  if(c=='(' || c=='[')
  StackPush(&myStack,c);
  else if(c==')' || c==']')
  {
   if(StackNotEmpty(&myStack)==0)
   return 0;
   StackPop(&myStack,&topc);
   if((c==')'&&topc!='(')||(c==']'&&topc!='['))
   return 0;
  } 
 }
 return !StackNotEmpty(&myStack);
}

int main()
{
 conversion();
 printf("----------------------\n");

 char expr1[]="[(1+2)*3-1]+[((1+2]*3)-1]";
 char expr2[]="[(1+2)*3-1]+[(1+2)*3-1]";
 printf("当前测试表达式为[(1+2)*3-1]+[((1+2]*3)-1]\n");
 if(kuohaocheck(expr1))
 {
  printf("匹配成功！\n"); 
 } else {
   printf("匹配失败！\n");
 }
 printf("当前测试表达式为[(1+2)*3-1]+[(1+2)*3-1]\n");
 if(kuohaocheck(expr2))
 {
  printf("匹配成功！\n");
 } else {
   printf("匹配失败！\n");
 }



 return 0;
}