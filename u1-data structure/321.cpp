#include<stdio.h>
#include<stdlib.h>

typedef struct TreeNode
{
 int data;
 TreeNode* lchild;
 TreeNode* rchild;
}*Tree,Node;


void CreateTree(Tree*T)
{
 int val;
 scanf("%d",&val);
 if(val==0)
 {
  *T=NULL;
  return;
 }
 *T=(Node*)malloc(sizeof(Node));
 (*T)->data=val;
 CreateTree(&(*T)->lchild);
 CreateTree(&(*T)->rchild);
}

int Countleaf(Tree T)
{
 if(T==NULL)
 return 0;
 if(T->lchild==NULL&&T->rchild==NULL)
 return 1;
 return Countleaf(T->lchild)+Countleaf(T->rchild);
}

void Printleaf(Tree T)
{
 if(T==NULL)
 return;
 if(T->lchild==NULL&&T->rchild==NULL)
 {
  printf("%d ",T->data);
  return;
 }
 Printleaf(T->lchild);
 Printleaf(T->rchild);
}

void preorder(Tree T)
{
 if(T==NULL)
 return;
 printf("%d ",T->data);
 preorder(T->lchild);
 preorder(T->rchild);
}

void inorder(Tree T)
{
 if(T==NULL)
 return;
 preorder(T->lchild);
 printf("%d ",T->data);
 preorder(T->rchild);
}

void postorder(Tree T)
{
 if(T==NULL)
 return;
 preorder(T->lchild);
 preorder(T->rchild);
 printf("%d ",T->data);
}

typedef struct QueueNode
{
 Tree data;
 struct QueueNode *next;
}QueueNode;

typedef struct
{
 QueueNode* front; 
 QueueNode* rear;
}Queue; 

void InitQueue(Queue* Q)
{
Q->rear=NULL;
Q->front=NULL;
}

int QueueNotEmpty(Queue Q)
{
 if(Q.front==NULL)
 return 0;
 return 1;
}

int QueueAppend(Queue* Q,Tree x)
{
 QueueNode *p=(QueueNode*)malloc(sizeof(QueueNode));
 if(p==NULL)
 return 0;
 p->data=x;
 p->next=NULL;
 if(Q->rear!=NULL)
 {
  Q->rear->next=p;
  Q->rear=p; 
 }
 if(Q->front==NULL)
 {
  Q->front=p;
  Q->rear=p;
 }
 return 1;
}

int QueueDelete(Queue* Q,Tree* x)
{
 QueueNode *p;
 if(Q->front==NULL)
 {
  return 0; 
 }
 else
 {
  *x=Q->front->data;
  p=Q->front;
  Q->front=Q->front->next;
  if(Q->front==NULL)
  Q->rear=NULL;
  free(p); 	
  return 1;
 }

}

void Level(Tree T)
{
 if(T==NULL)
 return;
 Queue q;
 InitQueue(&q);
 Tree p;
 QueueAppend(&q,T);
 while(QueueDelete(&q,&p))
 {
  printf("%d ",p->data);
  if(p->lchild)
  QueueAppend(&q,p->lchild);
  if(p->rchild)
  QueueAppend(&q,p->rchild);
 }
}

int main()
{
 Tree T;
 printf("按前序序列输入创建二叉树（A为1，以此类推，0为结束后续结点）：\n"); 
 CreateTree(&T);
 printf("树的前序序列：\n"); 
 preorder(T); 
 printf("\n");
 printf("树的中序序列：\n"); 
 inorder(T); 
 printf("\n");
 printf("树的后序序列：\n"); 
 postorder(T); 
 printf("\n");
 printf("树的叶子结点：\n"); 
 Printleaf(T); 
 printf("\n");
 printf("树的叶子个数：\n"); 
 printf("%d",Countleaf(T));
 printf("\n");
 printf("树的层序遍历：\n");
 Level(T); 
 return 0;
}