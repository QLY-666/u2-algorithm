#include <stdio.h>
#define MAX 5
typedef struct {
    int data[MAX];
    int lengh;
} SeqList;

void InitSeqList(SeqList *list) {
    list->lengh = 0;
}
void add(SeqList *list, int num) {
    if (list->lengh < MAX) {
        list->data[list->lengh] = num; 
        list->lengh++;                
}
}
int Locatedata(SeqList *list, int element) {
    if (list->lengh == 0) {
        return -1;
    }
    for (int i = 0; i < list->lengh; i++) {
        if (list->data[i] == element) {  
            return i;             
        }
    }
    return -1;
}
