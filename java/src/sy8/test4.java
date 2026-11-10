package sy8;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class test4 extends JFrame {
    JComboBox<String> proBox, cityBox;
    JRadioButton r1, r2;
    JCheckBox c1, c2, c3, c4, c5, c6;
    JButton btn;
    JTextArea area;

    // 省市数据（3个省，每省2个城市）
    String[][] cities = {{"广州", "深圳"}, {"武汉", "宜昌"}, {"成都", "绵阳"}};
    String[] provinces = {"广东", "湖北", "四川"};

    public test4() {
        // 1. 菜单栏
        JMenuBar mb = new JMenuBar();
        for (String m : new String[]{"File", "Edit", "Window", "Help"}) {
            JMenu menu = new JMenu(m);
            for (int i = 1; i <= 2; i++) {
                JMenuItem item = new JMenuItem(m + " " + i);
                item.addActionListener(e -> System.out.println("点击了: " + item.getText()));
                menu.add(item);
            }
            mb.add(menu);
        }
        setJMenuBar(mb);

        // 2. 主体面板
        JPanel p = new JPanel(new GridLayout(4, 2));

        // 城市联动
        proBox = new JComboBox<>(provinces);
        cityBox = new JComboBox<>(cities[0]);
        proBox.addActionListener(e -> { // 联动事件
            cityBox.removeAllItems();
            for (String c : cities[proBox.getSelectedIndex()]) cityBox.addItem(c);
        });
        p.add(new JLabel("城市"));
        JPanel cityP = new JPanel(); cityP.add(proBox); cityP.add(cityBox); p.add(cityP);

        // 性别单选
        r1 = new JRadioButton("男"); r2 = new JRadioButton("女");
        ButtonGroup bg = new ButtonGroup(); bg.add(r1); bg.add(r2);
        p.add(new JLabel("性别"));
        JPanel genderP = new JPanel(); genderP.add(r1); genderP.add(r2); p.add(genderP);

        // 爱好多选
        c1 = new JCheckBox("读书"); c2 = new JCheckBox("游泳");
        c3 = new JCheckBox("跑步"); c4 = new JCheckBox("旅行"); c5 = new JCheckBox("球类");
        p.add(new JLabel("爱好"));
        JPanel hP = new JPanel();
        for (JCheckBox c : new JCheckBox[]{c1, c2, c3, c4, c5}) hP.add(c);
        p.add(hP);

        // 协议与按钮
        c6 = new JCheckBox("同意协议");
        btn = new JButton("下一步"); btn.setEnabled(false);
        c6.addActionListener(e -> btn.setEnabled(c6.isSelected())); // 协议控制按钮
        p.add(new JLabel("请勾选"));
        JPanel bP = new JPanel(); bP.add(c6); bP.add(btn); p.add(bP);

        // 按钮事件：未勾选弹窗，勾选后输出结果
        btn.addActionListener(e -> {
            if (!c6.isSelected()) {
                JOptionPane.showMessageDialog(this, "请先勾选同意协议！");
                return;
            }
            String res = "城市：" + proBox.getSelectedItem() + " " + cityBox.getSelectedItem() + "\n"
                    + "性别：" + (r1.isSelected() ? "男" : "女") + "\n爱好：";
            if(c1.isSelected()) res += "读书 "; if(c2.isSelected()) res += "游泳 ";
            if(c3.isSelected()) res += "跑步 "; if(c4.isSelected()) res += "旅行 ";
            if(c5.isSelected()) res += "球类 ";
            area.setText(res);
        });

        // 3. 结果输出区
        area = new JTextArea(6, 40); area.setEditable(false);
        add(p, BorderLayout.CENTER);
        add(new JScrollPane(area), BorderLayout.SOUTH);

        setSize(550, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }

    public static void main(String[] args) {
        new test4().setVisible(true);
    }
}