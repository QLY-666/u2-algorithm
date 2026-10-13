#include<stdio.h>
int Isleap(int year);
int IsDate(int year,int month,int day);
int Yeardays(int year);


int Isleap(int year)
{return((year%4==0 && year%100!=0) || year%400==0);}

int IsDate(int year,int month,int day) {
 if(Isleap(year)) {
 if(day>=1&&day<=31&&(month==1||month==3||month==5||month==7||month==8||month==10||month==12))
           return 1;
    else if(day>=1&&day<=30&&(month==4||month==6||month==9||month==11))
           return 1;
    else if(day>=1&&day<=28+judgeyear(year)&&month==2) 
           return 1;
    else return 0;
} else return 0;
}


int Yeardays(int year) {
  if
}
