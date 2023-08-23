import javax.swing.JFrame;

public class MeuJFrame {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Meu JFrame");
        frame.setSize(400, 200);
        frame.setVisible(true);
        frame.setLocation(600, 300);

        JFrame janelaPessoa = new JFrame("Cadastro de Pessoa");
        janelaPessoa.setSize(400, 400);
        janelaPessoa.setVisible(true);
        janelaPessoa.setLocation(400, 400);
    }
}
