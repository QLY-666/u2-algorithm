#include<stdio.h>
#include<stdlib.h>

int main()
{
 int n,b;
 printf("输入物品种数 n 和背包限制 b:");
 scanf("%d %d",&n,&b);
 
 int* w=(int*)malloc((n+1) * sizeof(int));
 int* v=(int*)malloc((n+1) * sizeof(int));	
 printf("输入物品价值v和物品重量w（每行输入：v w）:\n");
 for(int i=1;i<=n;i++)
 {
  scanf("%d %d",&v[i],&w[i]);	
 }
 int *dp =(int*)calloc(b+1,sizeof(int));
 int *choice =(int*)calloc(b+1,sizeof(int));
 
 for(int i=1;i<=n;i++)
 {
  for(int j=w[i];j<=b;j++)
  {
   if(dp[j-w[i]]+v[i] > dp[j])
   {
    dp[j] = dp[j-w[i]]+v[i];
	choice[j]=i; 
   }	
  }	
 }
 
 int *cnt=(int*)calloc(n+1,sizeof(int));
 int j=b;
 while(j>0 && choice[j]!=0)
 {
  int id=choice[j];
  cnt[id]++;
  j-=w[id];
 }
 
 printf("物品编号 数量 价值\n");
 for(int i=1;i<=n;i++)
 	if(cnt[i]>0)
   		printf("%d %d %d\n",i,cnt[i],cnt[i]*v[i]);
  
 printf("最大价值：%d\n",dp[b]);  
 	
 free(w);
 free(v);
 free(dp);
 free(choice);
 free(cnt);
 return 0;
}