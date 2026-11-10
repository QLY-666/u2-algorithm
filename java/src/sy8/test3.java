package sy8;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class test3 {
    private static int click = 0, dblClick = 0;
    private static ArrayList<Point> squares = new ArrayList<>();

    public static void main(String[] args) {
        JFrame f = new JFrame("鼠标事件案例");
        f.setSize(500, 400);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLayout(new BorderLayout());

        JButton btn = new JButton("鼠标移到我上面");
        btn.setBackground(Color.LIGHT_GRAY);
        btn.addMouseListener(new MouseAdapter() {
            public void mouseEntered(MouseEvent e) { btn.setBackground(Color.GREEN); }
            public void mouseExited(MouseEvent e) { btn.setBackground(Color.LIGHT_GRAY); }
        });

        JLabel info = new JLabel("坐标：(0,0)  单击：0  双击：0");
        JPanel panel = new JPanel() {
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.BLUE);
                for (Point p : squares) g.fillRect(p.x - 5, p.y - 5, 10, 10);
            }
        };
        panel.setBackground(Color.WHITE);

        panel.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseMoved(MouseEvent e) {
                info.setText("坐标：(" + e.getX() + "," + e.getY() + ")  单击：" + click + "  双击：" + dblClick);
            }
            public void mouseDragged(MouseEvent e) {
                squares.add(e.getPoint());
                panel.repaint();
            }
        });

        panel.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 1) click++;
                if (e.getClickCount() == 2) dblClick++;
                info.setText("坐标：(" + e.getX() + "," + e.getY() + ")  单击：" + click + "  双击：" + dblClick);
            }
        });

        f.add(btn, BorderLayout.NORTH);
        f.add(info, BorderLayout.SOUTH);
        f.add(panel, BorderLayout.CENTER);
        f.setVisible(true);
    }
}