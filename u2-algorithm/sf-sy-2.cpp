#include "stdio.h"
#include <stdlib.h>
#include <time.h>

//题目要求：建立测试函数，参数iA表示主动测试芯片,iB表示被测芯片.返回值为被测芯片的测试值值为1时表示好芯片,为0时表示坏芯片.
int X_test(int iA, int iB) 
{
 	if (iA == 1) 
  	return iB;  
 	return rand() % 2; 
}

int main() 
{
	//题目要求：应用随机数来表示不确定的值1、0并在主函数中加上随机数种子语句srand(time(NULL));
    srand(time(NULL)); 
    
	int n;
    printf("请输入芯片总数 n (好芯片至少比坏芯片多1片): ");
    scanf("%d", &n);
    if (n <= 0) 
	{
     printf("输入无效！\n");
     return 0;
    }
    
    //分配数组 
    int *ABc = (int *)malloc(n * sizeof(int));
    
    //实现好芯片比坏芯片至少多1片 
    int iA = n / 2 + 1; 
    for (int i = 0; i < n; i++) 
	{
     if (i < iA) 
	 {
      ABc[i] = 1; 
     } 
	 else 
	 {
      ABc[i] = 0; 
     }
    }

    //随机打乱芯片顺序
    for (int i = 0; i < n; i++) {
        int j = rand() % n;
        int temp = ABc[i];
        ABc[i] = ABc[j];
        ABc[j] = temp;
    }
	
	//输出打乱的芯片序列 
    printf("生成的芯片序列(1好0坏): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", ABc[i]);
    }
    printf("\n");
    
    //分治算法 
    while (n > 1) 
	{
     int new_n = 0; 
     for (int i = 0; i + 1 < n; i += 2) 
	 {
      if (X_test(ABc[i], ABc[i+1]) == 1 && X_test(ABc[i+1], ABc[i]) == 1) 
	  {
       ABc[new_n++] = ABc[i]; 
      }
     }
     if (n % 2 == 1) 
	 {
      ABc[new_n++] = ABc[n - 1];
 	 }
     n = new_n; 
    }
    printf("最终剩下的一片芯片的好坏是(1好0坏): %d\n", ABc[0]);
    free(ABc);
    return 0;
}