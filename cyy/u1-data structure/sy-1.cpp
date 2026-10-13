#include<stdio.h>
#include<string.h>
#define MAX 100

typedef struct {
  int number;   
  char name[20];
  char ill[MAX];
}bingren;

typedef struct {
bingren data[MAX];
int length; 
}SequenceList;

void ListInitialize(SequenceList*L)
{
L->length=0;
}

int indexfind (SequenceList *L,int a)
{

 for(int i=0;i<L->length;i++)
 {
  if(L->data[i].number==a)
  {
   printf("该病人的序号为%d\n",i+1); 
   printf("该病人的姓名为%s\n",L->data[i].name);
   printf("该病人的病症为%s\n",L->data[i].ill);
   return i+1; 
  }
 }
 return -1; 
}

int ListFind(SequenceList L,char *x)
{
 for(int i=0;i<L.length;i++)
 {
  if(strcmp(L.data[i].name,x)==0)
  {
   return i+1;
  }

 }
 printf("没找到姓名为%s的病人！\n",x);
 return -1;
}

int main(){
SequenceList L;
ListInitialize(&L);
for(int i=0;i<2;i++)
{
printf("输入第%d个病人的病历号：",i+1);
scanf("%d",&L.data[i].number);
printf("输入第%d个病人的姓名：",i+1);
scanf("%s",L.data[i].name);
printf("输入第%d个病人的病症：",i+1);
scanf("%s",L.data[i].ill);
L.length++;
}

char targetname[20];
printf("输入要找的姓名：");
scanf("%s",targetname);
int index=ListFind(L,targetname);
if(index>0)
{
    printf("找到姓名为%s的病人，信息如下：\n",targetname);
    printf("病历号：%d\n",L.data[index-1].number); 
    printf("姓名：%s\n",L.data[index-1].name);
    printf("病症：%s\n",L.data[index-1].ill);
}

return 0; 
}