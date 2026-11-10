package sy8;
import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class test2{
    public static void main(String[] args) {
        JFrame f = new JFrame("QQ号录入");
        f.setSize(400, 250);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLayout(new FlowLayout());

        JLabel label = new JLabel("QQ号：");
        JTextField tf = new JTextField(20);
        JLabel tip = new JLabel("只能输入数字，最多 10 位；按回车提交");
        JButton btn = new JButton("提交");

        tf.addKeyListener(new KeyAdapter() {
            public void keyTyped(KeyEvent e) {
                char c = e.getKeyChar();
                if (!Character.isDigit(c) || tf.getText().length() >= 10) {
                    e.consume();
                }
            }
        });

        tf.addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    show(f, tf);
                }
            }
        });

        btn.addActionListener(e -> show(f, tf));

        f.add(label);
        f.add(tf);
        f.add(tip);
        f.add(btn);
        f.setVisible(true);
    }

    private static void show(JFrame f, JTextField tf) {
        JOptionPane.showMessageDialog(f, "录入的QQ号：" + tf.getText());
    }
}