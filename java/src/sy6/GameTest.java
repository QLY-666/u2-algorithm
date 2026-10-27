package sy6;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

//接口interface:相当于规范，类似多个抽象类，可以提供接口给不同子类来重写方法，注意用接口时子类用implements而不是extends
//关键规则：
//1.普通具体类可以实现接口，只要把接口里的抽象方法全部实现。
//2.如果类没有实现接口的全部抽象方法，那这个类必须声明为 abstract，否则编译报错。
//3.抽象类也可以实现接口，它可以只实现一部分方法，剩下的交给子类。
//4.接口不是类，接口本身不能 new，但可以被普通类、抽象类、枚举、记录类、匿名类等实现。

//例子：
//
//interface Greeting {
//    void hello();
//}
//1.普通类实现接口，不需要是抽象类：
//
//class GreetingImpl implements Greeting {
//    @Override
//    public void hello() {
//        System.out.println("Hello");
//    }
//}

//2.抽象类实现接口，可以不实现 hello()：
//
//abstract class BaseGreeting implements Greeting {
//    // 不实现 hello() 也可以，因为类是 abstract
//}
//因为是抽象类，所以接口的实现可以让子类去实现：
//
//class SubGreeting extends BaseGreeting {
//    @Override
//    public void hello() {
//        System.out.println("Hello");
//    }
//}

interface Skill {
    void skill();
}

abstract class Role implements Skill {
    protected int id;
    protected int hp;

    public Role(int id, int hp) {
        this.id = id;
        this.hp = hp;
    }

    public int getId() { return id; }
    public int getHp() { return hp; }
    public void setHp(int hp) { this.hp = hp; }

    public void move() {
        System.out.println("角色" + id + " 正在移动");
    }
}

class RoleA extends Role {
    public RoleA(int id, int hp) { super(id, hp); }

    @Override
    public void skill() {
        System.out.println("角色" + getId() + " 释放必杀技：降龙掌"
                + "(surDragonPalm)");
    }
}

class RoleB extends Role {
    public RoleB(int id, int hp) { super(id, hp); }

    @Override
    public void skill() {
        System.out.println("角色" + getId() + " 释放必杀技：六脉剑"
                + "(surDragonPalm)");
    }
}

class RoleC extends Role {
    public RoleC(int id, int hp) { super(id, hp); }

    @Override
    public void skill() {
        System.out.println("角色" + getId() + " 释放必杀技：一阳指"
                + "(oneSunFinger)");
    }
}

public class GameTest {
    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println("班级：计科252 学号：2500502222 姓名：李维熙");
        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String[] args) {
        Role[] roles = {
                new RoleA(1, 100),
                new RoleB(2, 90),
                new RoleC(3, 80)
        };
        for (Role r : roles) {
            System.out.println("ID=" + r.getId() + "，血量=" + r.getHp());
            r.move();
            r.skill();
            r.setHp(r.getHp() - 10);
            System.out.println("受伤后血量=" + r.getHp());
        }
    }
}
