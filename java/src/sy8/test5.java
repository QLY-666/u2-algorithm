package sy8;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;

public class test5 extends JFrame {
    JTextField userField = new JTextField(15);
    JPasswordField passField = new JPasswordField(15);
    JTextArea area = new JTextArea(8, 30);

    public test5() {
        setTitle("登录与文本组件演示");
        setSize(420, 380);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new FlowLayout()); // 使用简单的流式布局

        add(new JLabel("用户名:"));
        add(userField);

        add(new JLabel("密 码:"));
        add(passField);

        JButton btnLogin = new JButton("登录");
        JButton btnCancel = new JButton("取消");
        JButton btnFile = new JButton("选择文件");
        JButton btnColor = new JButton("选择颜色");

        JPanel btnPanel = new JPanel();
        btnPanel.add(btnLogin);
        btnPanel.add(btnCancel);
        btnPanel.add(btnFile);
        btnPanel.add(btnColor);
        add(btnPanel);

        area.setEditable(false);
        area.setText("提示信息:\n");
        // 将 JTextArea 放入 JScrollPane 中
        JScrollPane scroll = new JScrollPane(area);
        add(scroll);

        btnLogin.addActionListener(e -> {
            String user = userField.getText();
            String pass = new String(passField.getPassword());

            if ("admin".equals(user) && "123456".equals(pass)) {
                int res = JOptionPane.showConfirmDialog(this, "登录成功，欢迎回来！\n是否继续？", "成功", JOptionPane.YES_NO_OPTION);
                area.append("> 登录成功，欢迎回来！(确认结果: " + (res == JOptionPane.YES_OPTION ? "是" : "否") + ")\n");
            } else {
                JOptionPane.showMessageDialog(this, "登录失败，用户名或密码错误！", "错误", JOptionPane.ERROR_MESSAGE);
                area.append("> 登录失败，用户名或密码错误\n");
            }
        });

        btnCancel.addActionListener(e -> {
            userField.setText("");
            passField.setText("");
            area.append("> 已清空输入框\n");
        });

        btnFile.addActionListener(e -> {
            JFileChooser chooser = new JFileChooser();
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
                File file = chooser.getSelectedFile();
                area.append("> 选择文件 - 路径: " + file.getAbsolutePath() + "\n");
                area.append("> 选择文件 - 名称: " + file.getName() + "\n");
            }
        });

        btnColor.addActionListener(e -> {
            Color c = JColorChooser.showDialog(this, "选择前景色", Color.BLACK);
            if (c != null) {
                area.setForeground(c); // 改变文本框前景色
                area.append("> 已修改文本框前景色\n");
            }
        });
    }

    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {}

        new test5().setVisible(true);
    }
}