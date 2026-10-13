#include<stdio.h>
int main()
{  int a,b;
   printf("a=");
   scanf("%d",&a);
   printf("b=");
   scanf("%d",&b);
   if((a>3)&&(b>2))
   {  printf("yes");
   } else 
   { if (a>3) {
     if (b==2) {
	 printf("we can know b=2");
	 } else {
	 printf("b is too small");
	 } 
	 } else { 
	 printf("a is not in place");
	 }
   
   }
   







//if else
//   {printf("yes");
//   } else 
//   { printf("no");
//   }



//else if
//   {printf("too far");
//   
//   } else if((a=3)&&(b=2))
//   {printf("yes");
//   } else 
//   { printf("too near");
//   }









  return 0;
}





// if((a>3)&&(b>2))
//   {  printf("yes");
//   } else 
//   { if((a>3)&&(b=2))
//     {printf("b=2");
//	 } else if((a>3)&&(b<2))
//	 { printf("b too small");
//	 } else {
//	   printf("a don't in this place");
//	 }
//       







