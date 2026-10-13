#include <stdio.h>
typedef struct {
int id;
int score;
char name[10];
}stu;

int main() {
  int n;  
  scanf("%d",&n);
 stu a[n];
int max=0;
int min=0;


 for(int i=0;i<=n-1;i++)
{
 scanf("%d %d",&a[i].id,&a[i].score);
 gets(a[i].name);
}
int len=sizeof(a)/sizeof(a[0]);

for (int i = 1; i <len; i++) 
{     
if (a[i].score> a[max].score) 
max= i; 
if (a[i].score< a[min].score) 
min= i;
}
printf("max:%d %d %s\n",a[max].score,a[max].id,a[max].name);
printf("min:%d %d %s\n",a[min].score,a[min].id,a[min].name);

	return 0;
}
//#include <stdio.h>
//#define N 100
//
//typedef struct {
//    int id;
//    int score;
//    char name[10];
//}stu;
//
//int main() {
//    stu a[N];
//    int max=0;
//    int min=0;
//    
//    // 1. 修复for循环分隔符：逗号→分号
//    for(int i=0; i<=N-1; i++)
//    {
//        // 2. 输入id/score后，先清空缓冲区（避免name读入空行）
//        scanf("%d %d", &a[i].id, &a[i].score);
//        // 替换废弃的gets，用scanf("%9s")限制name长度（防溢出），且兼容你的输入逻辑
//        scanf("%9s", a[i].name); // %9s：最多读9个字符，适配name[10]的长度
//    }
//    
//    // 保留你原本的len计算（虽冗余，但按你的写法）
//    int len=sizeof(a)/sizeof(a[0]);
//
//    // 找最高分/最低分（逻辑不变）
//    for (int i = 1; i < len; i++) 
//    {     
//        if (a[i].score > a[max].score) 
//            max= i; 
//        if (a[i].score < a[min].score) 
//            min= i;
//    }
//    
//    // 3. 修复printf格式：%s对应name，补充参数，匹配格式符
//    printf("max:%s %d\n", a[max].name, a[max].score);
//    printf("min:%s %d\n", a[min].name, a[min].score);
//
//    return 0;
//}
