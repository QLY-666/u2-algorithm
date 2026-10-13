#include <stdio.h>

// 1. 定义静态顺序表核心结构（仅保留必要字段）
#define MAX 5  // 顺序表最大容量（极简设为5）
typedef struct {
    int data[MAX];  // 存储数据的数组
    int size;       // 当前元素个数（核心标识）
} SeqList;

// 2. 初始化顺序表（核心：把元素个数置0）
void InitSeqList(SeqList *list) {
    list->size = 0;
}

// 3. 向顺序表尾部添加元素（极简版，仅基础功能）
void AddElem(SeqList *list, int num) {
    // 简单检查：没满就添加
    if (list->size < MAX) {
        list->data[list->size] = num;  // 新元素放到size位置
        list->size++;                  // 元素个数+1
    }
}

// 主函数（测试：创建+初始化+添加+打印）
int main() {
    SeqList list;          // 创建顺序表变量（核心：创建）
    InitSeqList(&list);    // 初始化
    
    // 添加几个元素
    AddElem(&list, 10);
    AddElem(&list, 20);
    AddElem(&list, 30);
    
    // 打印顺序表（极简打印，直接写在主函数里，不单独写函数）
    printf("顺序表元素：");
    for (int i = 0; i < list.size; i++) {
        printf("%d ", list.data[i]);
    }
    
    return 0;
}