import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // n(n+1)/2  => 2*X <= n(n+1) 인 부분 찾으면 해당 라인에 있다. (n-1)n 을 빼고 남은 값에다가 n-left+1 를 분모로 +1+left를 분자로
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int X = Integer.parseInt(input[0]);
        int N = binary(X);
//        System.out.println("N = " + N);
        int num = X - ((N * (N - 1)) / 2);

        int a = num;
        int b = 1 + N - num;
        String result;
        if ( N % 2 == 0 ) {
            result = a + "/" + b;
        } else {
            result = b + "/" + a;
        }
        System.out.println(result);
    }

    public static int binary(int X) {
        int start = 0;
        int end = 10000;
        int mid;
        int i = X * 2;
        while (start <= end) {
            mid = (start + end) / 2;
            if ( mid * (mid - 1) < i && (mid * (mid + 1)) >= i) {
                return mid;
            } else if (mid * (mid + 1) > i) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return end;
    }
}