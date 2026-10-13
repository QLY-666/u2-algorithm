package sy3;

import java.util.Scanner;

class ChangFangXing {
    double length;
    double width;

    public double ZhouChang() {
        return 2 * (length + width);
    }
    public double MianJi() {
        return length * width;
    }
}

public class ChangFangXingTest {
    public static void main (String[] args) {
        ChangFangXing c = new ChangFangXing();
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入长方形的长：");
        c.length = sc.nextInt();
        System.out.println("请输入长方形的宽：");
        c.width = sc.nextInt();
        System.out.println("该长方形的周长："+ c.ZhouChang());
        System.out.println("该长方形的面积："+ c.MianJi());
    }
}