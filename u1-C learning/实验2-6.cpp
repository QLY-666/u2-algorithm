#include "stdio.h"
int main()
{ 
    int i,j,n;
    scanf("%d",&n);
    for(i=1;i<=n;i++)   // 循环n次，每次输出金字塔的一行
    { 
        for(j=0;j<n-i;j++)   // 修正循环条件：输出每行前段的空格
        {
            printf(" ");
        }
        for(j=0;j<2*i-1;j++)   // 【1】输出每行后段的星号
        {
            printf("*");
        }
        printf("\n");   // 输出换行
    }
    return 0;
}
