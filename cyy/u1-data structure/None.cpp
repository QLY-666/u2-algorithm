
 #include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int data;         
    struct Node *next;
} LNode, *LinkList;
LinkList CreateList_Head(LinkList L, int arr[], int n) {
    L = (LinkList)malloc(sizeof(LNode));
    L->next = NULL;
  
    for (int i = 0; i < n; i++) {
        LNode *new_node = (LNode *)malloc(sizeof(LNode));
        new_node->data = arr[i];
        new_node->next = L->next;
        L->next = new_node;
    }
    return L;
}

LinkList CreateList_Tail(LinkList L, int arr[], int n) {
    L = (LinkList)malloc(sizeof(LNode));
    L->next = NULL;
    LNode *tail = L; 

    for (int i = 0; i < n; i++) {
        LNode *new_node = (LNode *)malloc(sizeof(LNode));
        new_node->data = arr[i];
        new_node->next = NULL; 
        tail->next = new_node;
        tail = new_node;
    }
    return L;
}

void PrintList(LinkList L) {
    if (L->next == NULL) { 
        printf("链表为空！\n");
        return;
    }
    LNode *p = L->next; 
    printf("链表元素：");
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

int main() {
    int test_arr[] = {1, 2, 3, 4, 5}; 
    int n = sizeof(test_arr) / sizeof(test_arr[0]); 
    LinkList L_head, L_tail; 
    
    L_head = CreateList_Head(L_head, test_arr, n);
    PrintList(L_head);
    
    L_tail = CreateList_Tail(L_tail, test_arr, n);
    PrintList(L_tail);
    
    return 0;
}