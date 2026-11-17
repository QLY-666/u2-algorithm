package sy9;

import java.io.File;

public class File3 {
    public static void main(String[] args) {
        path(new File("C:\\JavaFile"));
    }

    public static void path(File dir) {
        if (dir == null || !dir.isDirectory()) {
            return;
        }

        File[] files = dir.listFiles();
        if (files == null) {
            return;
        }
        for (File file : files) {
            if (file.isDirectory()) {
                path(file);
            } else if (file.getName().endsWith(".java")) {
                System.out.println(file.getAbsolutePath());
            }
        }
    }
}
