package sy9;

import java.io.*;

public class File7 {
    public static void main(String[] args) throws IOException {
        copyDir(new File("D:\\MultiFile"),
                new File("E:\\MultiFileCopy"));
        System.out.println("复制完成");
    }

    public static void copyDir(File src, File dst) throws IOException {
        if (!dst.exists()) {
            dst.mkdirs();
        }
        File[] files = src.listFiles();
        if (files == null) return;
        for (File f : files) {
            File target = new File(dst, f.getName());
            if (f.isDirectory()) {
                copyDir(f, target);
            } else {
                copyFile(f, target);
            }
        }
    }

    public static void copyFile(File src, File dst) throws IOException {
        BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(src));
        BufferedOutputStream bos = new BufferedOutputStream(
                new FileOutputStream(dst));
        byte[] buf = new byte[1024];
        int len;
        while ((len = bis.read(buf)) != -1) {
            bos.write(buf, 0, len);
        }
        bos.close();
        bis.close();
    }
}
