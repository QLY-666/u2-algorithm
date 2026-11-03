package sy7;
import java.util.Scanner;
import java.util.StringTokenizer;

//`StringTokenizer` 在 `java.util` 包，
//作用：把一个长字符串，按照指定分隔符切成一小段一小段（分词）**，是 Java 早期用来分割字符串的工具类。
//特点：多个连续分隔符会被当成**一个**，不会分出空串；
//和 `String.split()` 不一样，split 是正则，StringTokenizer**不支持正则**，只认普通字符。

//scanner方式（1.3.4.5.6.7为重点）
//1. `new Scanner(bill)`：Scanner 本来读控制台，这里传入字符串，用来扫描这个字符串
//2. `.useDelimiter("[：，元]")`：设置分隔规则，`[]`是正则，表示里面任意一个字符作为分隔符
//3. `sc.hasNext()`：判断**下一个有没有一段字符串**
//4. `sc.next()`：读取下一段字符串，指针后移
//5. `sc.hasNextDouble()`：判断下一段能不能转成 double 小数
//6. `sc.nextDouble()`：直接读取下一段，自动转成 double（不用自己 parseDouble）
//7. `sc.close()`：关闭扫描器，释放资源，好习惯

public class test5 {
    public static void main(String[] args) {
        String bill = "市话费：28.89元，长途话费：128.87元，短信费：10.5元";

        System.out.println("StringTokenizer方式:");

        //1. `StringTokenizer st = new StringTokenizer(原字符串, 分隔符);`
        //创建分词器，指定用哪些符号切分
        StringTokenizer st = new StringTokenizer(bill, "：，元");
        double sum1 = 0;

        //2. `st.hasMoreTokens()`
        //判断：**还有没有下一段可以取**，返回 true/false，一般放 while 循环条件
        while (st.hasMoreTokens()) {

        //3. `st.nextToken()`
        //取出**下一段字符串**，取完自动跳到下一个
            String name = st.nextToken();
            String valStr = st.nextToken();
            double val = Double.parseDouble(valStr);
            System.out.println(name + " = " + val);
            sum1 += val;
        }
        System.out.println("总话费：" + sum1);

        System.out.println("");

        System.out.println("Scanner方式:");
        Scanner sc = new Scanner(bill).useDelimiter("[：，元]");
        double sum2 = 0;
        while (sc.hasNext()) {
            String name = sc.next();
            if (sc.hasNextDouble()) {
                double val = sc.nextDouble();
                System.out.println(name + " = " + val);
                sum2 += val;
            }
        }
        System.out.println("总话费：" + sum2);
        sc.close();
    }
}
