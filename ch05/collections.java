/* uses Timsort */

import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Zoe", "Alice", "Bob");

        Collections.sort(names);  // built-in sort

        System.out.println(names);
    }
}

