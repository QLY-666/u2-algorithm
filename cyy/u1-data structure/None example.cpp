#include <stdio.h>
#include <stdlib.h>

// ====================== 1. 链表节点类型定义（数据结构标准定义） ======================
// 定义单链表节点结构体
typedef struct LNode {
    int data;               // 数据域：存储节点数据
    struct LNode *next;     // 指针域：指向后继节点
} LNode, *LinkList;         // LNode：节点类型；LinkList：节点指针类型（链表头指针）

// ====================== 2. 链表创建函数 ======================
/**
 * 头插法创建带头结点单链表
 * @param L：链表头指针（输出型参数）
 * @param arr：待插入的数组
 * @param n：数组长度
 */
void CreateList_Head(LinkList *L, int arr[], int n) {
    // 1. 初始化头结点（空链表）
    *L = (LinkList)malloc(sizeof(LNode));  // 分配头结点空间
    (*L)->next = NULL;                     // 头结点后继置空
    
    // 2. 头插法核心：逐个插入数组元素
    for (int i = 0; i < n; i++) {  
        // ① 创建新节点
        LNode *p = (LNode *)malloc(sizeof(LNode));
        p->data = arr[i];  // 赋值
        
        // ② 头插：新节点后继指向头结点的后继
        p->next = (*L)->next;
        // ③ 头结点后继指向新节点
        (*L)->next = p;
    }
}

/**
 * 尾插法创建带头结点单链表
 * @param L：链表头指针（输出型参数）
 * @param arr：待插入的数组
 * @param n：数组长度
 */
void CreateList_Tail(LinkList *L, int arr[], int n) {
    // 1. 初始化头结点
    *L = (LinkList)malloc(sizeof(LNode));
    (*L)->next = NULL;
    LNode *r = *L;  // 尾指针r，始终指向链表尾部
    
    // 2. 尾插法核心：逐个插入数组元素
    for (int i = 0; i < n; i++) {
        // ① 创建新节点
        LNode *p = (LNode *)malloc(sizeof(LNode));
        p->data = arr[i];
        p->next = NULL;  // 尾节点后继置空
        
        // ② 尾插：尾部节点后继指向新节点
        r->next = p;
        // ③ 尾指针后移到新节点
        r = p;
    }
}

// ====================== 3. 辅助函数 ======================
/**
 * 遍历输出链表元素
 * @param L：链表头指针
 */
void TraverseList(LinkList L) {
    LNode *p = L->next;  // 跳过头结点，指向第一个数据节点
    if (p == NULL) {
        printf("链表为空！\n");
        return;
    }
    printf("链表元素：");
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

/**
 * 销毁链表（释放所有节点内存）
 * @param L：链表头指针
 */
void DestroyList(LinkList *L) {
    LNode *p = *L, *q;
    while (p != NULL) {
        q = p->next;
        free(p);
        p = q;
    }
    *L = NULL;  // 头指针置空，避免野指针
}

// ====================== 4. 测试主函数 ======================
int main() {
    LinkList L1, L2;  // 定义两个链表头指针
    int data[] = {1, 2, 3, 4, 5};  // 测试数据
    int len = sizeof(data) / sizeof(data[0]);  // 数据长度
    
    // 头插法创建链表并输出
    printf("【头插法创建链表】\n");
    CreateList_Head(&L1, data, len);
    TraverseList(L1);
    
    // 尾插法创建链表并输出
    printf("\n【尾插法创建链表】\n");
    CreateList_Tail(&L2, data, len);
    TraverseList(L2);
    
    // 销毁链表（规范操作，避免内存泄漏）
    DestroyList(&L1);
    DestroyList(&L2);
    
    return 0;
}