import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.stream.IntStream;

//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//String[] input = br.readLine().split(" ");

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int N = Integer.parseInt(input);
        int[] priceList = new int[N];
        for (int n=0; n < N; n++) {
            int price = Integer.parseInt(br.readLine());
            priceList[n] = price;
        }


        priceList = Arrays.stream(priceList)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();

        int count = N / 3;
        int total = Arrays.stream(priceList).sum();
        int sum = 0;
        for (int j=2; j<N; j+=3) {
            sum += priceList[j];
        }
        System.out.println(total-sum);
    }
}