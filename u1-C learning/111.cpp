#include"stdio.h"
int main()
{ int sc[30]={0},s,i,j,n;
scanf("%d",&n);
for(i=0;i<n;i++)//输入n位选手的成绩
{ scanf("%d",&s);
if(s>=70&&s<100) //若成绩在约定的区间内
sc[s-70]++; //记录成绩得分的人数
}
 for(i=30;i>=0;i--)
{
for(j=0;j<sc[i];j++)
{
printf("%3d",i+70); 
}
}
return 0;
}
