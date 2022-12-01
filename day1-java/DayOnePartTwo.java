import java.util.Scanner;
import java.util.Stack;
import java.util.List;

public class DayOnePartTwo {
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

        Integer sum = 0;

        List<Integer> sorted = elfs.stream()
                .sorted()
                .toList();

        for (int i = sorted.size() - 1; i >= sorted.size() - 3; i--) {
            sum += sorted.get(i);
        }

        System.out.println(sum);
    }
}
