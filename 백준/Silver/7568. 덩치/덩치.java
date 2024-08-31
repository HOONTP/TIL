import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<Integer>> infoList = getArrayLists();
        int N = infoList.size();
        int[] result = new int[N];
        for ( int i = 0; i < N; i++ ) {
            int count = 1;
            int a = infoList.get(i).get(0);
            int b = infoList.get(i).get(1);
            for (int j = 0; j < N; j++) {
                int A = infoList.get(j).get(0);
                int B = infoList.get(j).get(1);
                if (a < A && b < B) {
                    count += 1;
                }
            }
            result[i] = count;
        }
        String answer = Arrays.stream(result).mapToObj(String::valueOf).collect(Collectors.joining(" "));
        System.out.println(answer);

        }

    private static ArrayList<ArrayList<Integer>> getArrayLists() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int T = Integer.parseInt(input[0]);

        ArrayList<ArrayList<Integer>> infoList = new ArrayList<>();
        for (int i = 0; i < T; i++) {
            String[] person = br.readLine().split(" ");
            ArrayList<Integer> info = new ArrayList<>();
            info.add(Integer.parseInt(person[0]));
            info.add(Integer.parseInt(person[1]));
            infoList.add(info);
        }
        return infoList;
    }

}