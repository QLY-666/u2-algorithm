#include<stdio.h>
int main()
{   int score;
    printf("请输入分数：");
    scanf("%d",&score);
    switch(score)
	{
//单个字符要加'',记得空格与冒号	
	case 9:
		printf(" 优秀\n");
		
	 
	case 8:
		printf(" 良好\n");
	
		
	case 7:
		printf(" 一般\n");
		break;	
//不加 default则填一个范围外的数无结果 
//	default:
//	printf("NO CHOOSE");
	
	}
	
	return 0;
}




