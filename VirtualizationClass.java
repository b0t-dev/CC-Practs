// Pract 2 part 1
// Pract 2 part 1
public class VirtualizationClass {
    public static void main(String[] args) {

        long maxMemory = Runtime.getRuntime().maxMemory();

        System.out.println("JVM Name: " + System.getProperty("java.vm.name"));
        System.out.println("OS Name: " + System.getProperty("os.name"));

        // Conversions
        System.out.println("Max JVM Memory in Bytes: " + maxMemory);
        System.out.println("Max JVM Memory in KB: " + (maxMemory / 1024));
        System.out.println("Max JVM Memory in MB: " + (maxMemory / (1024 * 1024)));
        System.out.println("Max JVM Memory in GB: " + (maxMemory / (1024 * 1024 * 1024)));

        try {
            int[] arr = new int[500_0000];
            System.out.println("Memory allocated successfully!");
        } catch (OutOfMemoryError e) {
            System.out.println("OutOfMemoryError occurred!");
        }
    }
}


// Pract 2 part 2
import java.util.Scanner;

public class pract2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Runtime runtime = Runtime.getRuntime();
        System.out.print("Enter a string: ");
        String input = sc.nextLine();
        // JVM memory details before allocation
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        long usedMemory = totalMemory - freeMemory;
        System.out.println("\n===== JVM MEMORY BEFORE PROCESSING =====");
        System.out.println("Max JVM memory : " + Runtime.getRuntime().maxMemory() / (1024 * 1024) + " MB");
        System.out.println("Total JVM Memory : " + totalMemory / (1024 * 1024) + " MB");
        System.out.println("Used JVM Memory  : " + usedMemory / (1024 * 1024) + " MB");
        System.out.println("----------------------------------------");
        char[] chars = input.toCharArray();
        try {
            // Traverse string in reverse
            for (int i = chars.length - 1; i >= 0; i--) {
                // Memory allocation per character
                byte[] memoryBlock = new byte[1024 * 1024]; // 1 MB allocation
                memoryBlock[0] = (byte) chars[i];
                // JVM memory after allocation
                long usedNow = runtime.totalMemory() - runtime.freeMemory();
                System.out.println("Character: " + chars[i] + " | Used JVM Memory: " + (usedNow / (1024 * 1024)) + " MB"
                );
            }
        } catch (OutOfMemoryError e) {
            System.out.println("OutOfMemoryError occurred!");
        }
        sc.close();
    }
}






