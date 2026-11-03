package sy7;
import java.util.Scanner;

//charAt(x):类似数组的用法

public class test2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("请输入字符串：");
        String zifuchuan = sc.nextLine().trim();
        boolean duicheng = true;
        for(int left = 0,right = zifuchuan.length() - 1;left < right;left++, right--) {
            if(zifuchuan.charAt(left) != zifuchuan.charAt(right)) {
                duicheng = false;
                break;
            }
        }
        if(duicheng) {
            System.out.println("字符串"+zifuchuan+"对称");
            return;
        }
        System.out.println("字符串"+zifuchuan+"不对称");
        sc.close();
    }
}