#include "stdio.h"
#include <stdlib.h>
#include <time.h>
#define RANDNUM 20000 //随机数的个数

void SelectSort(int a[],int n)
{
 int i,j,pos,t;
 for(i=0;i<n-1;i++)
 {
  pos=i;
  for(j=i+1;j<n;j++)
  {
   if(a[j]<a[pos])
   pos=j; 
  }
  if(pos!=i)
  {
   t=a[i];
   a[i]=a[pos];
   a[pos]=t;
  }
 }
}

void InsertSort(int a[],int n)
{
 int t,i,j;
 for(i=1;i<n;i++)
 {
  t=a[i];
  for(j=i-1;j>=0&&a[j]>t;j--)
  {
   a[j+1]=a[j];
  } 
  a[j+1]=t;
 }
}

void BubbleSort(int a[],int n)
{
 int i,j,t,tag=1;
 for(i=1;i<n&&tag==1;i++)
 {
  tag=0;
  for(j=0;j<n-i;j++)
  {
   if(a[j+1]<a[j])
   {
    t=a[j];
    a[j]=a[j+1];
    a[j+1]=t;
    tag=1;
   }
  }
 }
}

void Merge(int a[],int swap[],int k,int n)
{
 int i,j,l1,l2,u1,u2,m=0;
 l1=0,m=0;
 while(l1+k<=n-1)
 {
  l2=l1+k;
  u1=l2-1;
  u2=(l2+k-1<=n-1)? l2+k-1:n-1;
  for(i=l1,j=l2;i<=u1&&j<=u2;)
  {
   if(a[i]<=a[j])
   {
    swap[m]=a[i];
    i++;
   }
   else
   {
    swap[m]=a[j];
    j++;
   }
  m++;
  }
  while(i<=u1)
  {
   swap[m]=a[i];
   m++;
   i++;
  }
 
  while(j<=u2)
  {
   swap[m]=a[j];
   m++;
   j++;
  }
  l1=u2+1;
 }
 for(i=l1;i<n;i++,m++)
 swap[m]=a[i]; 
}

void MergeSort(int a[],int n)
{
 int i,k=1;
 int* swap;
 swap=(int*)malloc(sizeof(int)*n);
 while(k<n)
 {
  Merge(a,swap,k,n);
  for(i=0;i<n;i++)
  a[i]=swap[i];
  k=2*k;
 }
 free(swap);
}

void copyarray(int a[],int save[],int n)
{
 for(int i=0;i<n;i++)
 save[i]=a[i];
}

int main()
{
 int iRandNum[RANDNUM];//存放随机数
 clock_t first,second; //记录开始和结束时间（以毫秒为单位
 int i;
 for(i=0;i<RANDNUM;i++)
 {//产生2万个随机数
  iRandNum[i]=rand()%RANDNUM;
 }

 int work[RANDNUM];
 printf("初始序列的前20个数：\n");
 for(int i=0;i<20;i++)
 printf("%d ",iRandNum[i]);
 printf("\n");
 
 printf("选择排序：\n");
 copyarray(iRandNum,work,RANDNUM); 
 first=clock();
 SelectSort(work,RANDNUM);
 second=clock();
 printf("选择排序耗时：%f秒\n",(double)(second-first)/CLOCKS_PER_SEC); 
 
 printf("插入排序：\n");
 copyarray(iRandNum,work,RANDNUM); 
 first=clock();
 InsertSort(work,RANDNUM);
 second=clock();
 printf("插入排序耗时：%f秒\n",(double)(second-first)/CLOCKS_PER_SEC); 
 
 printf("冒泡排序排序：\n");
 copyarray(iRandNum,work,RANDNUM); 
 first=clock();
 BubbleSort(work,RANDNUM);
 second=clock();
 printf("冒泡排序耗时：%f秒\n",(double)(second-first)/CLOCKS_PER_SEC); 
 
 printf("二路归并排序：\n");
 copyarray(iRandNum,work,RANDNUM); 
 first=clock();
 MergeSort(work,RANDNUM);
 second=clock();
 printf("二路归并排序耗时：%f秒\n",(double)(second-first)/CLOCKS_PER_SEC); 
 //显示排序算法所用的时间
 return 0;
}