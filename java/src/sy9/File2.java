package sy9;

import java.io.File;
import java.io.IOException;

//注：这里的file和name是自己命名的，写成File f 也没问题

public class File2 {
    public static void main(String[] args) throws IOException {
        File d1 = new File("E:/");

        String[] txtnames = d1.list();
        if (txtnames != null) {
            for(String name :txtnames) {
                if(name.endsWith(".txt")) {
                    System.out.println("用list()找到.txt后缀的文件： "+name);
                }
            }
        }

        File[] files = d1.listFiles();
        if (files != null) {
            for (File file : files) {
                if(file.isFile() && file.getName().endsWith(".txt")) {
                    System.out.println("用listFiles()找到.txt后缀的文件： "+file.getName());
                }
            }
        }
    }
}

