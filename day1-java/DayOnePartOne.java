import java.util.Scanner;
import java.util.Stack;

public class DayOnePartOne {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> elfs = new Stack<>();

        elfs.push(0);

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            try {
                Integer fromLine = Integer.parseInt(line);
                Integer current = elfs.pop();
                elfs.push(current + fromLine);
            } catch (NumberFormatException exception) {
                elfs.push(0);
            }
        }

        scanner.close();

        Integer most = -1;

        while (!elfs.isEmpty()) {
            most = Math.max(most, elfs.pop());
        }

        System.out.println(most);
    }
}
