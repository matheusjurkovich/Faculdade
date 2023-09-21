import javax.swing.JFrame;
import java.awt.*;

// Classe abstrata Win, que estende a classe JFrame
public abstract class Win extends JFrame {
  // Construtor com parâmetros para configurar a janela
  public Win(String title, int x, int y, int width, int height, int closing) {
    // Chama o método setupFrame para configurar os atributos da janela
    setupFrame(title, x, y, width, height, closing);

    // Chama o método setupComponents, que deve ser implementado pelas subclasses
    setupComponents();

    // Torna a janela visível
    setVisible(true);
  }

  // Construtor alternativo para criar uma janela sem definir a posição (x, y)
  public Win(String title, int width, int height, int closing) {
    this(title, -1, -1, width, height, closing);
  }

  // Método privado para configurar os atributos da janela
  private void setupFrame(String title, int x, int y, int width, int height, int closing) {
    // Define o título da janela
    setTitle(title);

    // Define o comportamento de fechamento da janela
    setDefaultCloseOperation(closing);

    // Define o tamanho da janela
    setSize(width, height);

    // Define a posição da janela com base nos parâmetros (x, y) ou de forma
    // automática
    if (x == -1 && y == -1) {
      setLocationByPlatform(true);
    } else {
      setLocation(x, y);
    }
  }

  // Método para centralizar a janela na tela
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

  // Método abstrato que deve ser implementado pelas subclasses para configurar os
  // componentes da janela
  protected abstract void setupComponents();
}
