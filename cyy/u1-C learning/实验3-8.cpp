#include<stdio.h>
int judgeyear(int year)
{    return (year%4==0 &&year%100!=0 || year%400==0); }
 
int main()
{   int year,month,day;
    int flag=1; //先假定日期合法
    scanf("%d-%d-%d",&year,&month,&day);
    //判断输入的合法性
    if(day>31||day<1||month>12||month<0||year<0 )//日，月，年非法情况
           flag=0;
    else if(day==31&&(month==4||month==6||month==9||month==11)) //考虑“非大月”但又31日的非法情况
           flag=0;
    else if(month==2&&day>29||month==2&&(day==29&&(year%400!=0||(year%100==0&&year%4!=0))))//考虑2月的情况，注意judgeyear()函数的返回值为（闰年1，平年0），可用于计算day是否越界。
           flag=0;
    if(flag) printf("yes");
    else  printf("no");
return 0;
}

