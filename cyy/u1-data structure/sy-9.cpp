#include<stdio.h>
#include<stdlib.h> 
#define MaxVertices 20
#define MaxWeight 10000
typedef struct
{
 int List[MaxVertices];
 int size;
}SequenceList;

void ListIntiate(SequenceList* L)
{
 L->size=0;
}

int ListLength(SequenceList L)
{
 return L.size;
}

int ListInsert(SequenceList* L,int pos,int x)
{
 if(L->size>=MaxVertices)
 {
  printf("已满，无法插入！");
  return 0;
 }
 else if(pos<0||pos>L->size)
 {
  printf("pos不合法，无法插入！");
  return 0;
 }
 else
 {
  for(int i=L->size;i>pos;i--) 
  L->List[i]=L->List[i-1];
  L->List[pos]=x;
  L->size++;
  return 1;
 } 
}

int ListDelete(SequenceList* L,int pos,int* x)
{
 int j;
 if(L->size<=0)
 {
  printf("已空，无法删除！");
  return 0;
 }
 else if(pos<0||pos>L->size-1)
 {
  printf("pos不合法，无法插入！");
  return 0;
 } 
 else
 {
  *x=L->List[pos];
  for(j=pos+1;j<=L->size-1;j++)
  {
   L->List[j-1]=L->List[j];
  }
 L->size--;
 return 1;
 } 
}


typedef struct
{
 SequenceList Vertices;
 int edge[MaxVertices][MaxVertices];
 int numofEdges;
}MatrixGragh;

void Intiate(MatrixGragh* G,int n)
{
 int i,j;
 for(i=0;i<n;i++)
 {
  for(j=0;j<n;j++)
  {
   if(i==j)
   G->edge[i][j]=0;
   else
   G->edge[i][j]=MaxWeight;
  }
 }
 G->numofEdges=0;
 ListIntiate(&G->Vertices);
}

void InsertVertex(MatrixGragh* G,int x)
{
 ListInsert(&G->Vertices,G->Vertices.size,x);
}


void InsertEdge(MatrixGragh* G,int v1,int v2,int weight)
{
 if(v1<0||v1>=G->Vertices.size||v2<0||v2>=G->Vertices.size) 
 {
  printf("v1 or v2 越界！");
  exit(1); 
 }
 G->edge[v1][v2]=weight;
 G->numofEdges++;
}

void DeleteEdge(MatrixGragh* G,int v1,int v2)
{
 if(v1<0||v1>=G->Vertices.size||v2<0||v2>=G->Vertices.size) 
 {
  printf("v1 or v2 越界！");
  exit(1); 
 }
 G->edge[v1][v2]=MaxWeight;
 G->numofEdges--;
}

void DeleteVertex(MatrixGragh* G,int v)
{
 int n=ListLength(G->Vertices),i,j;
 int x;
 for(i=0;i<n;i++)
 {
  for(j=0;j<n;j++)
  {
   if((i==v||j==v)&&G->edge[i][j]>0&&G->edge[i][j]<MaxWeight)
   G->numofEdges--;
  }
 }
 for(i=v;i<n;i++)
 {
  for(j=0;j<n;j++)
  {
   G->edge[i][j]=G->edge[i+1][j];
  }
 }
for(i=0;i<n;i++)
 {
  for(j=v;j<n;j++)
  {
   G->edge[i][j]=G->edge[i][j+1];
  }
 }
 ListDelete(&G->Vertices,v,&x);
}

void CreateGraph(MatrixGragh *G)
{
    int n,e;
    int vertex,v1,v2,w;
    printf("请输入顶点数和边数（空格分隔）：");
    scanf("%d%d",&n,&e);
    Intiate(G,n);
    printf("请输入%d个顶点的值（空格分隔）：",n);
    for(int i=0;i<n;i++)
    {
     scanf("%d",&vertex);
     InsertVertex(G,vertex);
    }
    printf("请输入%d条带权有向边（格式：起点 终点 权值，每行一条）：\n",e);
    for(int i=0;i<e;i++)
    {
     scanf("%d%d%d",&v1,&v2,&w);
     InsertEdge(G,v1,v2,w);
    }
}

void PrintMatrix(MatrixGragh *G)
{
 int n = G->Vertices.size;
 int a=10000;
 printf("当前带权有向图邻接矩阵：\n");
 for(int i=0;i<n;i++)
 {
  for(int j=0;j<n;j++)
  {
   if(G->edge[i][j] == MaxWeight)
   
   printf("%5d ",a);
   else
   printf("%5d ",G->edge[i][j]);
  }
  printf("\n");
 }
 printf("-------------------------\n");
}

int main()
{
    MatrixGragh G;
    CreateGraph(&G);
    PrintMatrix(&G);
    DeleteEdge(&G,0,1);
    printf("删除边 0→1 后：\n");
    PrintMatrix(&G);
    DeleteVertex(&G,1);
    printf("删除下标1的顶点后：\n");
    PrintMatrix(&G);
    return 0;
}

