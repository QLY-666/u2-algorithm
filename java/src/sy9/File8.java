package sy9;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class File8 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        TreeMap<Integer, String> map = new TreeMap<>((a, b) -> b - a);
        System.out.print("请输入学生人数：");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("姓名 成绩：");
            String name = sc.next();
            int score = sc.nextInt();
            map.put(score, name);
        }
        BufferedWriter bw = new BufferedWriter(
                new FileWriter("score.txt"));
        for (Map.Entry<Integer, String> e : map.entrySet()) {
            bw.write(e.getValue() + " " + e.getKey());
            bw.newLine();
        }
        bw.close();
        System.out.println("写入完成");
    }
}
