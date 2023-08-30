import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JComboBox;
import javax.swing.JCheckBox;
import javax.swing.JRadioButton;
import javax.swing.ButtonGroup;
import javax.swing.JButton;

public class Principal extends Win {
  public Principal(int x, int y) {
    super("Principal", x, y, 400, 400, JFrame.EXIT_ON_CLOSE);
  }

  @Override
  protected void setupComponents() {
    setLayout(null);
    JTextField nome = new JTextField(30);
    JTextField cidade = new JTextField("São José do Rio Preto", 30);
    JPasswordField senha = new JPasswordField(30);
    JComboBox ufs = new JComboBox(new String[] { "SP", "RJ", "MG" });
    JCheckBox robot = new JCheckBox("Não sou um robô");
    JRadioButton masculino = new JRadioButton("Masculino", true);
    JRadioButton feminino = new JRadioButton("Feminino");
    ButtonGroup sexo = new ButtonGroup();
    sexo.add(masculino);
    sexo.add(feminino);
    JButton help = new JButton("Me ajude");

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

    add(nome);
    add(cidade);
    add(senha);
    add(ufs);
    add(robot);
    add(masculino);
    add(feminino);
    add(help);
  }
}