#include"stdio.h"
#define N 10
struct Date
{ int year;
int month;
int day;
};
struct Mate
{ char name[10];
//此处填写一行语句
char tel[12];
};
struct Mate p[N];
int Datecomp(struct Date d1,struct Date d2); //d1年龄比d2大返回1，相等返回0，小则返回-1
int main()
{ int i,j,k,n;
struct Mate m;
scanf("%d",&n);
for(i=0;i<n;i++) //输入n个联系人的信息
{ scanf("%s",p[i].name);
scanf("%d-%d-%d",&p[i].birthday.year,&p[i].birthday.month,&p[i].birthday.day);
scanf("%s",p[i].tel);
}
for(i=0;i<n-1;i++) //选择排序算法按年龄降序排列
{ k=i;
for(j=i+1;j<n;j++)
//此处填入一行语句
k=j;
if(k!=i)
{ m=p[i];
p[i]=p[k];
p[k]=m;
}
}
for(i=0;i<n;i++)
printf("%s,%d-%d-%d,%s\n",p[i].name,p[i].birthday.year,p[i].birthday.month,p[i].birthday.day,p[i].tel);
return 0;
}

int Datecomp(struct Date d1,struct Date d2)
{ int result;
//此处填入多行语句
return result;
}
