package sy8;
import javax.swing.*;
import java.awt.*;

public class test1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Swing窗口");
        frame.setSize(800, 600);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new FlowLayout());
        for (int i = 1; i <= 5; i++) {
            topPanel.add(new JButton("按钮 " + i));
        }

        JPanel centerPanel = new JPanel(new BorderLayout());
        centerPanel.add(new JButton("北 North"), BorderLayout.NORTH);
        centerPanel.add(new JButton("南 South"), BorderLayout.SOUTH);
        centerPanel.add(new JButton("西 West"), BorderLayout.WEST);
        centerPanel.add(new JButton("东 East"), BorderLayout.EAST);
        centerPanel.add(new JButton("中 Center"), BorderLayout.CENTER);

        JPanel bottomPanel = new JPanel(new GridLayout(2, 2));
        for (int i = 1; i <= 5; i++) {
            bottomPanel.add(new JButton("Grid " + i));
        }

        frame.add(topPanel, BorderLayout.NORTH);
        frame.add(centerPanel, BorderLayout.CENTER);
        frame.add(bottomPanel, BorderLayout.SOUTH);

        frame.setVisible(true);
    }
}