#include <stdio.h>
#include<string.h>
#include<stdlib.h>
typedef struct TreeNode{
    int data;
    struct TreeNode*lchild;
    struct TreeNode*rchild;
}Node,*Tree;

void CreateTree(Tree* T)
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
 CreateTree(&((*T)->lchild));
 CreateTree(&((*T)->rchild));
}

int Countleaf(Tree T)
{
 if(T==NULL)
 {
  return 0;  
 }
 if(T->lchild==NULL&&T->rchild==NULL)
 return 1;
 return Countleaf(T->lchild)+Countleaf(T->rchild);
}

int main()
{
 Tree T=NULL;
 printf("请输入前序序列(0表示空节点)\n");
 CreateTree(&T);
 int num=Countleaf(T);
 printf("叶子数为%d\n",num);
 return 0;   
}
