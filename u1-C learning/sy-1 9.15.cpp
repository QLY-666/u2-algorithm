#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

#define N 10000

long long count;

//插入排序  
void insert(int arr[])
{
 count=0;
 for(int i=1;i<N;i++)
 {
  int j=i-1;
  int key = arr[i];
  while(j>=0)
  {
   count++;
   if(key < arr[j])
   {
    arr[j+1]=arr[j];
    count++;
    j--;
   }
   else break;
  }
  arr[j+1]=key;
  count++;
 }
}

//冒泡排序 
void bubble(int arr[])
{
 count=0;
 for(int i=0;i<N-1;i++)
 {
  count++;
  for(int j=0;j<N-1-i;j++)
  {
   if(arr[j]>arr[j+1])
   {
    int t=arr[j+1];
    arr[j+1] = arr[j];
    arr[j]=t;
    count+=3;
   }
  }
 }
}

//选择排序
void select(int arr[])
{
 count=0;
 for(int i=0;i<N-1;i++)
 {
  int min=i;
  for(int j=i+1;j<N;j++)
  {
   count++;
   if(arr[j]<arr[min])
   {
    min=j;
   }
  }
  if(min!=i)
   {
    int t=arr[i];
	arr[i]=arr[min];
	arr[min]=t;
	count+=3;
   }
 }
} 

int main()
{
 srand(time(NULL));
 int arr[N];
 clock_t start,end;
 double spent;
 
 //1.插入排序
 for(int i=0;i<N;i++)
 arr[i]=rand()%N;
 start=clock();
 insert(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("1.插入排序\n");
 printf("一般情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 
 for(int i=0;i<N;i++)
 arr[i]=N-i;
 start=clock();
 insert(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("最坏情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 printf("\n");
 
//2.冒泡排序
 for(int i=0;i<N;i++)
 arr[i]=rand()%N;
 start=clock();
 bubble(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("2.冒泡排序\n");
 printf("一般情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 
 for(int i=0;i<N;i++)
 arr[i]=N-i;
 start=clock();
 bubble(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("最坏情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 printf("\n");
 
 //3.选择排序
 for(int i=0;i<N;i++)
 arr[i]=rand()%N;
 start=clock();
 select(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("3.选择排序\n");
 printf("一般情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 
 for(int i=0;i<N;i++)
 arr[i]=N-i;
 start=clock();
 select(arr);
 end=clock();
 spent=(double)(end-start)/CLOCKS_PER_SEC;
 printf("最坏情况  运行时间：%.4f秒  执行次数:%lld\n",spent,count);
 printf("\n");
 return 0;
}
