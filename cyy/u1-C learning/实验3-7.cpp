#include<stdio.h>
int judgeyear(int year)
{   return((year%4==0 && year%100 !=0) || year%400==0);}
int main()
{   int year,month,day;
    int flag=0; //先假定日期非法
    scanf("%d-%d-%d",&year,&month,&day);
    //判断输入的合法性（月-日的适配性）
    if(day>=1&&day<=31&&(month==1||month==3||month==5||month==7||month==8||month==10||month==12))//大月的月份
           flag=1;
    else if(day>=1&&day<=30&&(month==4||month==6||month==9||month==11))
//小月的日的范围
           flag=1;
    else if(day>=1&&day<=28+judgeyear(year)&&month==2) //二月的情况，
//注意judgeyear函数的返回值，闰年返回1，闰年二月的天数也多1，使用加法运算
           flag=1;
    if(flag) printf("yes");
    else  printf("no");
return 0;
}
