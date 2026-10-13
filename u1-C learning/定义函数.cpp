#include<stdio.h>
 //函数声明加； 
 //函数中定义的变量在主函数中可以不出现 
 int x(int a);
 int x(int a)
{  int sum,i; 
   for(i=1;i<=a;i++)
   sum=sum+i;   
 //return返回的是将返回值返到调用函数处（主函数内调用的该函数），  
 //相当于将该函数的结果（sum）赋给变量，即 变量=f(x),此时调用数据才可进行函数运算   
   return sum;
}




int main()
{  int jieguo,n; 
   printf("请输入:");
   scanf("%d",&n);
//for里面加分号  
//调用数据不用加参数类型int之类   
   jieguo=x(n);
   printf("%d",jieguo);
  return 0;
}

