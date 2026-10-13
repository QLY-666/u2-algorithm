//神人代码从输入12开始就是 11月的天数，case=4就是三月的，所以case=3不用的，因为2月是我自己定义的 

#include<stdio.h>
int judgeyear(int year) //闰年判别函数
{   int flag=0; //平年返回0
    if ((year%4==0 && year%100!=0) || year%400==0)
           flag=1; //闰年返回1
    return flag;
}
int main()
{   int year,month,day;
    int dayNumber=0;
    scanf("%d-%d-%d",&year,&month,&day);
	switch (month)
{ case 12:dayNumber +=30;//11月的 
case 11:dayNumber +=31;
case 10:dayNumber +=30;
case 9 :dayNumber +=31;
case 8 :dayNumber +=31;
case 7 :dayNumber +=30;
case 6 :dayNumber +=31;
case 5 :dayNumber +=30;
case 4 :dayNumber +=31;
case 3 :;//3月的情况,请填写多行代码
case 2 :if(judgeyear(year))//2月的情况,请填写一行代码
        { dayNumber +=29;	
		} else {
		  dayNumber +=28;
		}; 
case 1 :dayNumber +=31;//1月的情况,请填写多行代码
        printf("%d",dayNumber+day);
		break;      
default:printf("Input error!");
    }
}
