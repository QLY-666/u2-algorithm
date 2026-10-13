package sy3;

import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
    public static void main (String[] args) {
        Random rand = new Random();
        int r = rand.nextInt(100)+1;
        Scanner sc = new Scanner(System.in);
        int count = 1;
        while (true) {
            System.out.println("请输入第"+count+"次猜测：");
            int guess = sc.nextInt();
            if (guess>r) {
                System.out.println("猜大了");
                count++;
            } else if (guess<r) {
                System.out.println("猜小了");
                count++;
            } else {
                System.out.println("猜对了");
                break;
            }
        }
        sc.close();
    }
}
