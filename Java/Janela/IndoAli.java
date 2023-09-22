import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.InputStream;
import javax.imageio.ImageIO;
import javax.swing.*;

public class IndoAli extends Win {

    public IndoAli(int x, int y) {
        // Chama o construtor da superclasse Win para configurar a janela
        super("Indo Ali", x, y, 1000, 700, JFrame.DISPOSE_ON_CLOSE);
    }

    @Override
    protected void setupComponents() {

        try {
            // Carrega a imagem
            InputStream inputStream = IndoAli.class.getResourceAsStream("/indo_ali.jpeg");
            BufferedImage bufferedImage = ImageIO.read(inputStream);
            Image image = bufferedImage.getScaledInstance(1000, 700, Image.SCALE_SMOOTH);

            // Cria um JLabel para exibir a imagem
            JLabel label = new JLabel(new ImageIcon(image));

            // Adiciona o JLabel ao JFrame
            add(label);

        } catch (IOException e) {
            // Registra a exceção ou trate-a de outra forma
            System.err.println("Erro ao carregar a imagem: " + e.getMessage());
        }
    }
}
