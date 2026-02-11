import java.util.LinkedList;

public class Playlist {
    public static void main(String[] args) {
        LinkedList<String> playlist = new LinkedList<>();

        playlist.add("Null and Void");
        playlist.addFirst("Pointer Parade");
        playlist.addLast("The Tail End");

        playlist.removeFirst();
        playlist.add(1, "Forever Node");

        for (String song : playlist) {
            System.out.println(song);
        }
    }
}
