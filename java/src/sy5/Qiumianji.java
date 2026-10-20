package sy5;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Rectangle {
    double width, height;

    Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    double getArea() {
        return width * height;
    }

    double getPerimeter() {
        return 2 * (width + height);
    }
}

class Square extends Rectangle {
    Square(double side) {
        super(side, side);
    }

    @Override
    double getArea() {
        return width * width;
    }

    @Override
    double getPerimeter() {
        return 4 * width;
    }
}

public class Qiumianji {
    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String[] args) {
        Rectangle[] arr = {
                new Rectangle(3, 4),
                new Rectangle(5, 2),
                new Square(3),
                new Square(2.5)
        };

        System.out.println("第1个面积：" + arr[0].getArea());
        System.out.println("第2个面积：" + arr[1].getArea());
        System.out.println("第3个面积：" + arr[2].getArea());
        System.out.println("第4个面积：" + arr[3].getArea());
        }
    }
