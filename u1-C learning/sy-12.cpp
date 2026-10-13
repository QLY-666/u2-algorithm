#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct node
{
 char data[100];
 struct node*left,*right;
}node;

node* createnode(char *name)
{
 node* newnode=(node*)malloc(sizeof(node));
 strcpy(newnode->data,name);
 newnode->left=NULL;
 newnode->right=NULL;
 return newnode;
}

node* insert(node* root,char* name)
{
 if(root==NULL)
 return createnode(name);
 if(strcmp(name,root->data)<0)
 root->left=insert(root->left,name);
 if(strcmp(name,root->data)>0)
 root->right=insert(root->right,name);
 return root;
}

int Search(node* root,char* name)
{
 if(root==NULL)
 {
  return 0; 
 }
 int target=strcmp(name,root->data);
 if(target==0)
 return 1;
 if(target<0)
 return Search(root->left,name);
 return Search(root->right,name);
}

void inorder(node* root)
{
 if(root==NULL)
 return;
 inorder(root->left);
 printf("%s ",root->data);
 inorder(root->right);
}

void printTree(node* root, int space)
{
 if (root == NULL)
 return;
 int indent = 5;
 space=indent+space;
 printTree(root->right,space);
 printf("\n");
 for(int i=indent;i<space;i++)
 printf(" ");
 printf("%s\n",root->data);
 printTree(root->left,space);
}

int main()
{
 node* root=NULL;
 char* herb[]={"地龙","佛手","紫石英","沙苑子","佩兰","白蓬草","星宿草","玉竹","瓦松","葱白","骨碎补","胡黄连"};
 int n=12;
 for(int i=0;i<12;i++)
 {
  root=insert(root,herb[i]);
 }
 printf("二叉排序树的中序序列：\n");
 inorder(root); 
 printf("\n");
 printf("输入要查找的中药：");
 char name[50];
 scanf("%s",&name);
 int target=Search(root,name);
 if(target==1)
 printf("查找成功，%s存在\n",&name);
 else
 printf("查找失败，%s不存在\n",&name);
 printf("二叉排序树的结构:\n");
 printTree(root,0); 
 return 0;
}

