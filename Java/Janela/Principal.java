import javax.swing.*;

// Classe Principal que estende a classe abstrata Win
public class Principal extends Win {
  // Construtor da classe Principal
  public Principal(int x, int y) {
    // Chama o construtor da superclasse Win para configurar a janela
    super("Principal", x, y, 300, 200, JFrame.EXIT_ON_CLOSE);
  }

  // Método override para configurar os componentes da janela
  @Override
  protected void setupComponents() {
    // Define o layout da janela como null (layout personalizado)
    setLayout(null);

    // Cria um rótulo (label) com o texto "Clique no botão para abrir o cadastro"
    JLabel label = new JLabel("Clique no botão para abrir o cadastro");

    // Cria um botão com o texto "Cadastrar"
    JButton button = new JButton("Cadastrar");

    // Define a posição e o tamanho do rótulo e do botão
    label.setLocation(10, 10);
    label.setSize(label.getPreferredSize());

    button.setLocation(10, 40);
    button.setSize(button.getPreferredSize());

    // Adiciona o rótulo e o botão à janela
    add(label);
    add(button);

    // Adiciona um ouvinte de ação ao botão
    button.addActionListener(e -> {
      // Quando o botão é clicado, cria uma instância da classe Pessoa
      Pessoa pessoa = new Pessoa(100, 100);

      // Torna a janela Pessoa visível
      pessoa.setVisible(true);

      // Centraliza a janela Pessoa na tela
      pessoa.goToCenter();
    });
  }
}
