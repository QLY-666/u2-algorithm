package sy7;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

//## 1. 常用获取对象
//LocalDate now = LocalDate.now(); // 获取系统当前日期
//LocalDate date = LocalDate.of(1945,9,3); // 指定年月日

//## 2. 获取年月日、星期
//- `getYear()` 年
//- `getMonthValue()` 月份（数字 1~12）
//- `getDayOfMonth()` 日
//- `getDayOfWeek()` 星期（返回 DayOfWeek 枚举）

//## 3. 日期运算（返回新 LocalDate，原对象不变）
//- `plusDays(n)` 加 n 天
//- `minusDays(n)` 减 n 天
//- `plusMonths()` / `minusMonths()` 加减月

//## 4. 计算两个日期相隔天数（import java.time.temporal.ChronoUnit;）
//ChronoUnit.DAYS.between(日期1,日期2);
//返回 long，得到相差天数（可能负数，取绝对值用 Math.abs）

//## 5. 和旧 Date 转换（你之前题目用到）

/// / LocalDate → Date
//Date d = Date.from(localDate.atStartOfDay(ZoneId.systemDefault()).toInstant());
//作用：拿去给 `String.format("%tY年%tm月%td日",d,d,d)` 格式化

//## 6. 判断方法
//- `isBefore()` 是否在另一个日期之前
//- `isAfter()` 是否在另一个日期之后
//- `isEqual()` 日期相等
//## ✅ 对比区分（考点）
//- LocalDate：**只有年月日**
//- LocalTime：只有时分秒
//- LocalDateTime：年月日 + 时分秒

public class test4 {

    public static void main(String[] args) {
                LocalDate now = LocalDate.now();
                System.out.println("当前日期：" + now);
                System.out.println("当前星期：" + now.getDayOfWeek());

                LocalDate d1 = LocalDate.of(1945, 9, 3);
                LocalDate d2 = LocalDate.of(1931, 9, 18);
                long days = ChronoUnit.DAYS.between(d2, d1);
                System.out.println("相隔天数：" + days);

                String format = String.format("%tY年%tm月%td日", now, now, now);
                System.out.println("格式化日期：" + format);
            }
    }