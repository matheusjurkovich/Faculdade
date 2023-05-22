import java.util.Random;

public class APS_BuscaSequencial {

    public static void main(String[] args) {
        int tamanhoVetor = 100000000; // Define o tamanho do vetor
        int[] vetor = criarVetor(tamanhoVetor);
        int numBusca = gerarNumeroAleatorio();
        
        long tempoCriacao = System.currentTimeMillis();
        boolean encontrado = buscarNumero(numBusca, vetor);
        tempoCriacao = System.currentTimeMillis() - tempoCriacao;

        System.out.println("Tempo de criação do vetor: " + tempoCriacao + " ms");
        if (encontrado) {
            System.out.println("O número " + numBusca + " foi encontrado!");
        } else {
            System.out.println("O número " + numBusca + " não foi encontrado!");
        }
    }

    private static int[] criarVetor(int tamanho) {
        Random gerador = new Random();
        int[] vetor = new int[tamanho];
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = gerador.nextInt(tamanho) + 1;
        }
        return vetor;
    }

    private static int gerarNumeroAleatorio() {
        Random gerador = new Random();
        return gerador.nextInt(1000) + 1;
    }

    private static boolean buscarNumero(int numBusca, int[] vetor) {
        long inicioBusca = System.currentTimeMillis();
        for (int i = 0; i < vetor.length; i++) {
            if (vetor[i] == numBusca) {
                System.out.println("Tempo de busca: " + (System.currentTimeMillis() - inicioBusca) + " ms");
                return true;
            }
        }
        System.out.println("Tempo de busca: " + (System.currentTimeMillis() - inicioBusca) + " ms");
        return false;
    }
}
