package sy7;
import java.util.Scanner;

//1.string类的方法系统自带，不用import
//2.trim()：去首尾空格
//3。nextLine():接收一行，还有nextInt这些

public class test1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String targetpassword = "1234";
        for(int i = 3;i>=0;i--) {
            System.out.print("请输入密码：");
            String password = sc.nextLine();
            password = password.trim();
            if(password.equals(targetpassword)) {
                System.out.println("密码正确！");
                return;
            } else {
                System.out.println("密码错误，还有"+ i + "次机会");
            }

        }
        System.out.println("密码错误，退出游戏");
        sc.close();
    }
}