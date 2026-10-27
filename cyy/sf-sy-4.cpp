#include <stdio.h>
#include <limits.h>
#define N 5

int m[N+1][N+1];
int s[N+1][N+1];

int RecurMatrixChain(int P[],int i,int j) 
{
 if (i==j) 
 {
  m[i][j]=0;
  s[i][j]=i;
  return 0;
 }
m[i][j]=INT_MAX;
s[i][j]=i;

for (int k = i; k < j; k++) 
{
 int q=RecurMatrixChain(P,i,k)+RecurMatrixChain(P,k +1,j)+ P[i-1]*P[k]*P[j];
 if (q<m[i][j]) 
 {
  m[i][j]=q;
  s[i][j]=k;
 }
}
 return m[i][j];
}

void printOptimal(int i,int j) 
{
 if (i==j) 
 {
  printf("A%d",i);
 } 
 else 
 {
  printf("(");
  printOptimal(i, s[i][j]);
  printOptimal(s[i][j] + 1, j);
  printf(")");
 }
}

int main() {
    int P[]={30,35,15,5,10,20};
    int n=N;
    RecurMatrixChain(P,1,n);
    printf("最小乘法次数=%d\n",m[1][n]);
    printf("最后一次运算位置s[1][%d] = %d\n",n,s[1][n]);
    printf("\n");
    return 0;
}