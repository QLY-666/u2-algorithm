#include <stdio.h>
//int n=2; 
//int main() {
//  int n=1;
//    printf("n=%d",n);
//    return 0;
//}
//输出n=1 

//int n=2; 
//int main() {
//    printf("n=%d",n);
//    return 0;
//}
//输出n=2 

//int main() {
//    int n=2;
//	{ int n=1;
//	}
//	printf("n=%d",n);
//    return 0;
//}
//输出n=2 



//
//int main() {
//    int n=2;
//	{ int n=1;
//	printf("n=%d",n);
//	}
//	printf("n=%d",n);
//    return 0;
//}
//输出n=1,n=2 
void test_function() {
    int a= 1;  // 生命周期开始：函数调用时创建
    printf("a=%d\n", a++);

} // 生命周期结束：函数返回时销毁

int main() {
    test_function();  // 输出：local_var = 10
    test_function();  // 输出：local_var = 10（重新创建，不是11！）
    return 0;
}
