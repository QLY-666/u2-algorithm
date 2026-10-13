#include <stdio.h>
int main()
{ 
  printf("%3d\n",1);
  printf("%4d\n",2);
  printf("%5d\n",3);
  printf("%6d\n",4);
  //
  //
  printf("%03d\n",1);
  printf("%04d\n",2);
  printf("%05d\n",3);
  printf("%06d\n",4);
  //  
  //
  printf("%-3d\n",1);//把数左对齐 
  printf("%-4d\n",11);
  printf("%-5d\n",111);
  printf("%-6d\n",1111);
  //
  //
  printf("%6.2f\n",1.2);
  printf("%6.2f\n",1.23);
  printf("%6.2f\n",1.234);
  printf("%6.2f\n",1.2345);
  
  
  return 0;
}

