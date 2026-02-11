
public class StaticArrayEnd {
    public static void main(String[] args) {
        int[] original = {10, 20, 30};
        int size = 3;

        int newValue = 40;
        int[] newArray = new int[size + 1];

        for (int i = 0; i < size; i++) {
            newArray[i] = original[i];
        }

        newArray[size] = newValue;
        size++;

        for (int item : newArray) {
            System.out.println(item);
        }
    }
}
