package sy7;
import java.time.LocalDateTime;
import java.util.Random;
import java.util.Scanner;

//正则表达式（简称：正则，regex）
//一句话：正则是一套专门用来描述字符串规则的模板，用来判断一段文字符不符合你规定的格式
//Java 里用字符串.matches(正则)` 来判断是否匹配，返回 true/false。
//通用符号
//符号	含义
//[abc]	匹配 a 或者 b 或者 c 其中一个字符
//[0-9]	匹配一个数字，等价于\\d
//[a-z]	小写字母
//+	前面内容 ≥1 次
//{m,n}	前面内容，最少 m 次，最多 n 次
//^ 在 [] 内	取反，[^a] = 不是 a
//\\d	一个数字（Java 必须双斜杠）


public class test6 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        int code = random.nextInt(100) + 1;
        String username, pwd, email, phone;
        int inputCode;

        // 1. 用户名正则：`[a-zA-Z]+`
        //规则：**全部只能是大写、小写字母，不能为空**
        //- `[a-zA-Z]`：代表任意一个英文字母（a~z 或者 A~Z）
        //- `+`：前面这个内容 **出现 1 次或者多次**
        //✅ 合法：`Tom`、`LiSi`
        //❌ 不合法：`Tom123`、`123abc`、`张三`

        while (true) {
            System.out.print("请输入用户名(只能是字母)：");
            username = sc.next();
            if (username.matches("[a-zA-Z]+")) {
                break;
            }
            System.out.println("用户名不合法！只能输入字母，请重新输入。");
        }

        //##  密码正则：`[^a-zA-Z][a-zA-Z0-9]{5,21}`
        //规则：一共 6~22 位，只能字母数字，**第一位不能是字母**
        //- `[^a-zA-Z]`：`^` 在中括号里面代表**取反** → 不是字母（可以是数字）
        //- `[a-zA-Z0-9]`：任意字母或者数字
        //- `{5,21}`：前面的字母数字，出现 **5 到 21 次**
        //👉 第一位 (1 位) + 后面 (5~21 位) = 总长度 6~22
        //✅ 合法：`123abc`、`9a1b2c3`
        //❌ 不合法：`abc123`（字母开头）、`12ab`（太短，只有 4 位）
        //> ⚠️ 注意：`[]里面的^` 和正则最开头的`^`不是一个意思！
        //> - `[ ^ ]` 里面：代表**非、不是**
        //> - 写在正则最开头 `^xxx`：代表字符串开头

        while (true) {
            System.out.print("请输入密码(6-22位，字母数字，不能字母开头)：");
            pwd = sc.next();
            if (pwd.matches("[^a-zA-Z][a-zA-Z0-9]{5,21}")) {
                break;
            }
            System.out.println("密码不合法！6-22位、字母数字、不能字母开头，重输。");
        }

        //## 3. 邮箱正则：`^[a-zA-Z0-9_]+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+$`
        //规则：简单邮箱格式，必须有 `@`，@后面要有域名，比如 `.com`
        //- `^`：字符串开始
        //- `[a-zA-Z0-9_]+`：用户名部分，字母数字下划线
        //- `@`：必须有 @符号
        //- `[a-zA-Z0-9]+`：@后面主体，比如 qq、163
        //- `(\\.[a-zA-Z0-9]+)+`：`.com` / `.cn` 这种后缀，至少出现一次
        //- `$`：字符串结束
        //✅ 合法：`zs@qq.com`
        //❌ 不合法：`zsqq.com`（没有 @）、`zs@qq`（没有后缀）

        while (true) {
            System.out.print("请输入邮箱：");
            email = sc.next();
            if (email.matches("^[a-zA-Z0-9_]+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+$")) {
                break;
            }
            System.out.println("邮箱格式错误，请重新输入！");
        }

        //## 4. 手机号正则：`1[3-9]\\d{9}`
        //
        //规则：11 位手机号，1 开头，第二位 3~9，后面 9 个数字
        //
        //- `1`：第一位固定是 1
        //- `[3-9]`：第二位是 3、4、5…9 中的一个
        //- `\\d`：代表任意一个数字（0-9），Java 里要写两个反斜杠
        //- `{9}`：数字连续出现 9 次
        //✅ 合法：`13912345678`
        //❌ 不合法：`12912345678`（第二位是 2）、`139123456`（不够 11 位）

        while (true) {
            System.out.print("请输入手机号：");
            phone = sc.next();
            if (phone.matches("1[3-9]\\d{9}")) {
                break;
            }
            System.out.println("手机号格式错误，请重新输入！");
        }

        while (true) {
            System.out.println("本次验证码：" + code);
            System.out.print("请输入验证码：");
            inputCode = sc.nextInt();
            if (inputCode == code) {
                break;
            }
            System.out.println("验证码错误！重新输入");
        }

        LocalDateTime now = LocalDateTime.now();
        String timeStr = String.format("%tY年%tm月%td日 %tH时%tM分", now, now, now, now, now);
        System.out.println("注册成功！");
        System.out.println("注册时间：" + timeStr);
        sc.close();
    }
}

