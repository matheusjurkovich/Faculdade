import javax.swing.JFrame;
import java.awt.*;

public abstract class Win extends JFrame {
  public Win(String title, int x, int y, int width, int height, int closing) {
    setupFrame(title, x, y, width, height, closing);
    setupComponents();
    setVisible(true);
  }

  public Win(String title, int width, int height, int closing) {
    this(title, -1, -1, width, height, closing);
  }

  private void setupFrame(String title, int x, int y, int width, int height, int closing) {
    setTitle(title);
    setDefaultCloseOperation(closing);
    setSize(width, height);
    if (x == -1 && y == -1) {
      setLocationByPlatform(true);
    } else {
      setLocation(x, y);
    }
  }

  public void goToCenter() {
    Toolkit tk = Toolkit.getDefaultToolkit();
    int screenWidth = tk.getScreenSize().width;
    int screenHeight = tk.getScreenSize().height;
    int winWidth = getSize().width;
    int winHeight = getSize().height;
    int x = screenWidth / 2 - winWidth / 2;
    int y = screenHeight / 2 - winHeight / 2;
    setLocation(x, y);
  }

  protected abstract void setupComponents();
}