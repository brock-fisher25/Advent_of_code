import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;



public class Main {
    public static void main(String[] args) {
        String input_1 = read_text_file("day_1.txt");
        String input_7 = read_text_file("day_7.txt");
        Day_1.run(input_1);
        Day_7.run(input_7);
    }
    public static String read_text_file(String day_input) {
        String content = "";
        try {
            content = Files.readString(Paths.get("input_" + day_input));
        } catch (IOException e) {
            System.out.println("An error occurred reading the file.");
            e.printStackTrace();
        }
        return content;
    }
}
