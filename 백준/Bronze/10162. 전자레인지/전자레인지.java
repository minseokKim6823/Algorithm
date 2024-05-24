import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        int T= sc.nextInt();

        int a =0;
        int b =0;
        int c =0;

        int[] arr= {300,60,10};

        a=T/arr[0];
        T=T%arr[0];
        b=T/arr[1];
        T=T%arr[1];
        c=T/arr[2];
        T=T%arr[2];

        if(T!=0){
            System.out.println(-1);
        }
        else{
            System.out.printf("%s %s %s", a, b, c);
        }
    }
}
