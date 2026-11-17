package sy9;

public class File4 {
    public static void main(String[] args) {
        int a = 10, b = 0;
        int[] arr = new int[3];
        String s = null;

        try {
            // System.out.println(a / b);
            // arr[5] = 100;
            // s.length();
        } catch (ArithmeticException e) {
            System.out.println("1. 抓到了：算术异常（除数为0）");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("2. 抓到了：数组越界异常");
        } catch (NullPointerException e) {
            System.out.println("3. 抓到了：空指针异常");
        } catch (RuntimeException e) { // 兜底
            System.out.println("4. 兜底：其他运行期异常");
        }

        System.out.println("程序正常");
    }
}