package sy9;

import java.io.*;

public class File6 {
    public static void main(String[] args) throws IOException {
        File src = new File("d:\\bbb.mp4");
        File dst = new File("copy.mp4");
        long t1 = System.currentTimeMillis();
        copy1(src, dst);
        long t2 = System.currentTimeMillis();
        System.out.println("方式一耗时：" + (t2 - t1) + "ms");

        t1 = System.currentTimeMillis();
        copy2(src, new File("copy2.mp4"));
        t2 = System.currentTimeMillis();
        System.out.println("方式二耗时：" + (t2 - t1) + "ms");

        t1 = System.currentTimeMillis();
        copy3(src, new File("copy3.mp4"));
        t2 = System.currentTimeMillis();
        System.out.println("方式三耗时：" + (t2 - t1) + "ms");

        t1 = System.currentTimeMillis();
        copy4(src, new File("copy4.mp4"));
        t2 = System.currentTimeMillis();
        System.out.println("方式四耗时：" + (t2 - t1) + "ms");
        // 依次测试 copy2 / copy3 / copy4，记录四种方式的耗时
    }

    public static void copy1(File src, File dst) throws IOException {
        FileInputStream fis = new FileInputStream(src);
        FileOutputStream fos = new FileOutputStream(dst);
        int b;
        while ((b = fis.read()) != -1) {     // 一次读一个字节
            fos.write(b);
        }
        fos.close();
        fis.close();
    }

    public static void copy2(File src, File dst) throws IOException {
        FileInputStream fis = new FileInputStream(src);
        FileOutputStream fos = new FileOutputStream(dst);

        byte[] buf = new byte[1024];
        int len;

        while ((len = fis.read(buf)) != -1) {
            fos.write(buf, 0, len);
        }

        fos.close();
        fis.close();
    }

    public static void copy3(File src, File dst) throws IOException {
        BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(src));
        BufferedOutputStream bos = new BufferedOutputStream(
                new FileOutputStream(dst));

        int b;

        while ((b = bis.read()) != -1) {
            bos.write(b);
        }

        bos.close();
        bis.close();
    }

    public static void copy4(File src, File dst) throws IOException {
        BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(src));
        BufferedOutputStream bos = new BufferedOutputStream(
                new FileOutputStream(dst));
        byte[] buf = new byte[1024];
        int len;
        while ((len = bis.read(buf)) != -1) {  // 一次读一个数组
            bos.write(buf, 0, len);
        }
        bos.close();
        bis.close();
    }
}
