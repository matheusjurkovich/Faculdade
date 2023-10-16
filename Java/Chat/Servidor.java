import java.io.*;
import java.net.*;

public class Servidor {
  public static void main(String[] args) {
    try {
      ServerSocket serverSocket = new ServerSocket(12345); // Porta para o servidor
      System.out.println("Servidor aguardando conexões...");

      Socket clientSocket = serverSocket.accept(); // Aguardando a conexão do cliente

      System.out.println("Cliente conectado.");

      // Fluxo de entrada do cliente
      BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

      // Fluxo de saída para o cliente
      PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

      BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

      String clientMessage, serverMessage;

      while (true) {
        clientMessage = in.readLine();
        if (clientMessage == null) {
          System.out.println("Cliente desconectado.");
          break;
        }
        System.out.println("Cliente: " + clientMessage);

        System.out.print("Servidor: ");
        serverMessage = consoleInput.readLine();
        out.println(serverMessage);
      }

      in.close();
      out.close();
      clientSocket.close();
      serverSocket.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
