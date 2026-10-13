package sy2;

public class Accident {
    public static void main(String[] args) {
        for (int a = 1; a <= 9; a++) {
            for (int b = 0; b <= 9; b++) {
                int carNumber = a * 1000 + a * 100 + b * 10 + b;
                int root = (int) Math.sqrt(carNumber);
                if (root * root == carNumber) {
                    System.out.println("肇事者的车牌号码是：" + carNumber);
                }
            }
        }
    }
}