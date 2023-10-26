package linkedlist;

import java.util.Scanner;

abstract class BaseStack extends LinkedList<Integer> {
    int capacity;
    String MENU = """
            ** STACK MENU **
            1. PUSH
            2. POP
            3. PEEK
            4. DISPLAY
            Any other number to show menu.
            """;
    Scanner sc = new Scanner(System.in);

    BaseStack(int length) {
        capacity = length;
    }

    abstract void push(int data);

    abstract void pop();

    abstract void peek();

    abstract void displayStack();

    void menu() {
        System.out.println(MENU);
        int choice = 1;
        while (choice != 0) {
            switch (choice) {
                case 1 -> {
                    System.out.print("Enter the string: ");
                    int elem = sc.nextInt();
                    push(elem);
                }
                case 2 -> pop();
                case 3 -> peek();
                case 4 -> displayStack();
                default -> System.out.println(MENU);

            }
            System.out.print("\nEnter your choice: ");
            choice = sc.nextInt();
        }

    }
}