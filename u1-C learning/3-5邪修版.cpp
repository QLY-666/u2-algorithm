#include<stdio.h>
int judgeyear(int year) //闰年判别函数
{   int flag=0; //平年返回0
    if ((year%4==0 && year%100!=0) || year%400==0)
           flag=1; //闰年返回1
    return flag;
}
int main()
{   int year,month,month1,day;
    int dayNumber=0;
    scanf("%d-%d-%d",&year,&month,&day);
    month1=month-1;
 switch (month1)
{ case 12:dayNumber +=30;
case 11:dayNumber +=31;
case 10:dayNumber +=30;
case 9 :dayNumber +=31;
case 8 :dayNumber +=31;
case 7 :dayNumber +=30;
case 6 :dayNumber +=31;
case 5 :dayNumber +=30;
case 4 :dayNumber +=31;
case 3 :dayNumber +=30;//3月的情况,请填写多行代码
case 2 :if(judgeyear(year))//2月的情况,请填写一行代码
        { dayNumber +=29;	
		} else {
		  dayNumber +=28;
		};
case 1 :dayNumber +=31;//1月的情况,请填写多行代码
        printf("%d",dayNumber+=day);
		break;      
default:printf("Input error!");
    }
}
