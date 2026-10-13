package sy2;

import java.util.Scanner;

public class Temperature {
    public static void main(String[] args) {
        double[][] temperature = new double[4][3];
        Scanner sc = new Scanner(System.in);
        System.out.println("请依次输入 4 名患者每天 3 次的体温数据（共 12 个）：");
        for (int i=0;i<temperature.length; i++) {
            System.out.println("请输入第 " + (i + 1) + " 名患者的 3 次体温：");
            for (int j = 0; j < temperature[i].length; j++) {
                System.out.print("  第 " + (j + 1) + " 次测量：");
                temperature[i][j] = sc.nextDouble();
            }
        }
        System.out.println();
        System.out.println("患者\t第1次\t第2次\t第3次");
        for (int i = 0; i < temperature.length; i++) {
            System.out.print("患者" + (i + 1) + "\t");
            for (int j = 0; j < temperature[i].length; j++) {
                System.out.printf("%.1f\t", temperature[i][j]);
            }
            System.out.println();
        }

        sc.close();
    }
}