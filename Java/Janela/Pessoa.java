import javax.swing.*;

// Classe Pessoa que estende a classe abstrata Win
public class Pessoa extends Win {
  // Construtor da classe Pessoa
  public Pessoa(int x, int y) {
    // Chama o construtor da superclasse Win para configurar a janela
    super("Pessoa", x, y, 400, 400, JFrame.DISPOSE_ON_CLOSE);
  }

  // Método override para configurar os componentes da janela
  @Override
  protected void setupComponents() {
    // Define o layout da janela como null (layout personalizado)
    setLayout(null);

    // Cria diversos componentes de interface do usuário
    JTextField nome = new JTextField(30);
    JTextField cidade = new JTextField("São José do Rio Preto", 30);
    JPasswordField senha = new JPasswordField(30);
    JComboBox<String> ufs = new JComboBox<>(new String[] {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    });
    JCheckBox robot = new JCheckBox("Não sou um robô");
    JRadioButton masculino = new JRadioButton("Masculino", true);
    JRadioButton feminino = new JRadioButton("Feminino");
    ButtonGroup sexo = new ButtonGroup();
    sexo.add(masculino);
    sexo.add(feminino);
    JButton help = new JButton("Me ajude");

    // Define a posição e o tamanho dos componentes
    nome.setLocation(10, 10);
    nome.setSize(nome.getPreferredSize());
    cidade.setLocation(10, 40);
    cidade.setSize(cidade.getPreferredSize());
    senha.setLocation(10, 70);
    senha.setSize(senha.getPreferredSize());
    ufs.setLocation(10, 100);
    ufs.setSize(ufs.getPreferredSize());
    robot.setLocation(10, 130);
    robot.setSize(robot.getPreferredSize());
    masculino.setLocation(10, 160);
    masculino.setSize(masculino.getPreferredSize());
    feminino.setLocation(10, 190);
    feminino.setSize(feminino.getPreferredSize());
    help.setLocation(10, 220);
    help.setSize(help.getPreferredSize());

    // Adiciona os componentes à janela
    add(nome);
    add(cidade);
    add(senha);
    add(ufs);
    add(robot);
    add(masculino);
    add(feminino);
    add(help);

    // Adiciona um ouvinte de ação ao botão "Me ajude"
    help.addActionListener(e -> {
      JOptionPane.showMessageDialog(null, "uili", "uili", JOptionPane.INFORMATION_MESSAGE);
      JOptionPane.showMessageDialog(null, "uilov", "uilov", JOptionPane.INFORMATION_MESSAGE);
      JOptionPane.showMessageDialog(null, "uilai", "uilai", JOptionPane.INFORMATION_MESSAGE);
      IndoAli IndoAli = new IndoAli(100, 100);

      IndoAli.setVisible(true);

      IndoAli.goToCenter();
    });
  }
}
