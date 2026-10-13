package sy2;

import java.util.Scanner;

public class FindMaxIndex
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("请输入3个整数：");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int max = a;
        if(b > max) max = b;
        if(c > max) max = c;
        System.out.print("最大值是"+max);
        sc.close();
    }
}