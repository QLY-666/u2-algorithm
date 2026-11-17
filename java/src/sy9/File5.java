package sy9;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

//writer相当于类，write相当于方法
//new BufferedWriter(new FileWriter("D:\\test.txt")) ，为什么是new FileWriter而不是File
//BufferedWriter 的构造方法只接收“流”，不接收“文件地址”
//Java 的底层源码，BufferedWriter 的构造方法要求传入的必须是 Writer 类型的对象
//File 只是内存里的“路径对象”，没有“写”的能力
//当你 new File("D:\\test.txt") 时，它其实连文件都没碰，只是告诉系统“我要找这个路径”。
//而 new FileWriter("D:\\test.txt") 在实例化的那一刻，底层其实已经帮你把这个文件创建好（或者打开）了，
// 并且准备好了将字符转换成字节的编码能力。它才是真正具有 write() 功能的源头。

public class File5 {
    public static void main(String[] args) throws IOException {

        BufferedWriter bw = new BufferedWriter(new FileWriter("D:\\test1.txt"));

        for (int i = 1; i <= 5; i++) {
            for (int j = 0; j < i; j++) {
                bw.write("*");
            }
            bw.newLine();
        }
        bw.close();

        BufferedWriter bw2 = new BufferedWriter(new FileWriter("D:\\test2.txt", true));
        bw2.newLine();
        bw2.write("一闪一闪亮晶晶");
        bw2.close();
        System.out.println("写入完成");
    }
}
