import java.util.Random;

public class APS_BuscaBinaria {
    public static void main(String[] args) {
        int[] sizes = {1000, 10000, 100000, 1000000, 10000000  };
        int[] ranges = {1000, 10000, 100000, 1000000, 10000000  };
        
        for (int i = 0; i < sizes.length; i++) {
            int size = sizes[i];
            int range = ranges[i];
            
            int[] numbers = generateRandomNumbers(size, range);
            
            long startTime = System.currentTimeMillis();
            RedBlackTree tree = createRedBlackTree(numbers);
            long endTime = System.currentTimeMillis();
            
            long creationTime = endTime - startTime;
            
            int randomValue = getRandomNumber(range);
            
            startTime = System.currentTimeMillis();
            boolean found = tree.search(randomValue);
            endTime = System.currentTimeMillis();
            
            long searchTime = endTime - startTime;
            
            System.out.println("Tamanho: " + size);
            System.out.println("Range: 1 - " + range);
            System.out.println("Numero aleatorio: " + randomValue);
            System.out.println("Tempo de busca: " + searchTime + " ms");
            System.out.println("Tempo de criação: " + creationTime + " ms");
            System.out.println("Numero foi encontrado?: " + found);
            System.out.println("------------------------------------");
        }
    }
    
    private static int[] generateRandomNumbers(int size, int range) {
        int[] numbers = new int[size];
        Random random = new Random();
        
        for (int i = 0; i < size; i++) {
            numbers[i] = random.nextInt(range) + 1;
        }
        
        return numbers;
    }
    
    private static int getRandomNumber(int range) {
        Random random = new Random();
        return random.nextInt(range) + 1;
    }
    
    private static RedBlackTree createRedBlackTree(int[] numbers) {
        RedBlackTree tree = new RedBlackTree();
        
        for (int number : numbers) {
            tree.insert(number);
        }
        
        return tree;
    }
}

class RedBlackTree {
    private Node root;
    
    private static final boolean RED = true;
    private static final boolean BLACK = false;
    
    private class Node {
        int key;
        Node left, right;
        boolean color;
        
        Node(int key) {
            this.key = key;
            this.color = RED;
        }
    }
    
    public boolean search(int key) {
        return search(root, key);
    }
    
    private boolean search(Node node, int key) {
        if (node == null) {
            return false;
        }
        
        if (key < node.key) {
            return search(node.left, key);
        } else if (key > node.key) {
            return search(node.right, key);
        } else {
            return true;
        }
    }
    
    public void insert(int key) {
        root = insert(root, key);
        root.color = BLACK;
    }
    
    private Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }
        
        if (key < node.key) {
            node.left = insert(node.left, key);
        } else if (key > node.key) {
            node.right = insert(node.right, key);
        }
        
        if (isRed(node.right) && !isRed(node.left)) {
            node = rotateLeft(node);
        }
        
        if (isRed(node.left) && isRed(node.left.left)) {
            node = rotateRight(node);
        }
        
        if (isRed(node.left) && isRed(node.right)) {
            flipColors(node);
        }
        
        return node;
    }
    
    private boolean isRed(Node node) {
        if (node == null) {
            return false;
        }
        
        return node.color == RED;
    }
    
    private Node rotateLeft(Node node) {
        Node temp = node.right;
        node.right = temp.left;
        temp.left = node;
        temp.color = node.color;
        node.color = RED;
        return temp;
    }
    
    private Node rotateRight(Node node) {
        Node temp = node.left;
        node.left = temp.right;
        temp.right = node;
        temp.color = node.color;
        node.color = RED;
        return temp;
    }
    
    private void flipColors(Node node) {
        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }
}
