#include<stdio.h>
#include<math.h>
int main()
{   double x0,y0,A,B,C;
    scanf("%lf%lf",&x0,&y0);//输入点P的坐标
    scanf("%lf%lf%lf",&A,&B,&C);//输入直线L的A、B和C
    printf("%f\n",fabs(A*x0 + B*y0 + C) / sqrt(A*A + B*B));//输出距离
    return 0;
}
