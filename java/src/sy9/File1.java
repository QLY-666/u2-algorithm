package sy9;

import java.io.File;
import java.io.IOException;

//多级目录可用\\或/

public class File1 {
    public static void main(String[] args) throws IOException {
        File f1 = new File("f1.txt");
        System.out.println("文件1：createNewFile()返回值 "+f1.createNewFile());

        File d1 = new File("C:/test");
        System.out.println("目录：mkdir()返回值 "+d1.mkdir());

        File d2 = new File("C:/test/a/b");
        System.out.println("创建多级目录：mkdirs() " + d2.mkdirs());

        File f2 = new File("f2.txt");
        System.out.println("重命名：renameTo()返回值 " + f1.renameTo(f2));
        System.out.println("删除：delete()返回值 " + f2.delete());
    }
}

