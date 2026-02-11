import java.util.ArrayList;

public class DynamicArrayEnd {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);

        for (Integer num : numbers) {
            System.out.println(num);
        }
    }
}
