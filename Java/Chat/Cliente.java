import java.io.*;
import java.net.*;

public class Cliente {
  public static void main(String[] args) {
    try {
      Socket socket = new Socket("192.168.1.95", 12345); // Usando o endereço IP local para se conectar ao servidor na
      // mesma máquina

      // Fluxo de entrada para o servidor
      BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

      // Fluxo de saída do cliente
      PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

      BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

      String serverMessage, clientMessage;

      while (true) {
        System.out.print("Cliente: ");
        clientMessage = consoleInput.readLine();
        out.println(clientMessage);

        serverMessage = in.readLine();
        System.out.println("Servidor: " + serverMessage);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
