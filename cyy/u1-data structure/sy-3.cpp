#include <stdio.h>
#define MAXSIZE 100

typedef struct {
    int data[MAXSIZE];
    int front;
    int rear;
    int count;
} SequenceQueue;

void QueueInitiate(SequenceQueue *Q) {
    Q->front = 0;
    Q->rear = 0;
    Q->count = 0;
}

int QueueNotempty(SequenceQueue *Q) {
    return Q->count > 0;
}

int QueueAppend(SequenceQueue *Q, int x) {
    if (Q->count == MAXSIZE)
        return 0;
    Q->data[Q->rear] = x;
    Q->rear = (Q->rear + 1) % MAXSIZE;
    Q->count++;
    return 1;
}

int QueueDelete(SequenceQueue *Q, int *x) {
    if (Q->count == 0)
        return 0;
    *x = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXSIZE;
    Q->count--;
    return 1;
}

int yanghuisanjiao(int n) {
    if(n <= 0)
        return 0;
    SequenceQueue s;
    QueueInitiate(&s);
    QueueAppend(&s, 1);
    for(int i = 1; i <= n; i++) {
        int last = 0, cur;
        for(int j = 0; j < i; j++) {
            QueueDelete(&s, &cur);
            printf("%d ", cur);
            if(j < i - 1)
                QueueAppend(&s, last + cur);
            last = cur;
        }
        QueueAppend(&s, 1);
        printf("\n");
    }
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    yanghuisanjiao(n);
    return 0;
}