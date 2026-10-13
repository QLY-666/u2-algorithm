#include<stdio.h>
int judgeyear(int year)
{return((year%4==0 && year%100!=0) || year%400==0);}
int main()
{   int year,month,day;
    int dayNumber=365;
    scanf("%d-%d-%d",&year,&month,&day);
     if(judgeyear(year))
        { dayNumber=366;} 
    switch(month)
{ case 1:dayNumber -=31;
case 2:if(judgeyear(year))
        { dayNumber -=29;	
		} else {
		  dayNumber -=28;
		}; 
case 3:dayNumber -=31;
case 4 :dayNumber -=30;
case 5 :dayNumber -=31;
case 6 :dayNumber -=30;
case 7 :dayNumber -=31;
case 8 :dayNumber -=31;
case 9 :dayNumber -=30;
case 10:dayNumber -=31;
case 11:dayNumber -=30;
case 12:dayNumber -=31;
printf("%d",dayNumber+day);
break;
default:printf("Input error!");
    }
}
