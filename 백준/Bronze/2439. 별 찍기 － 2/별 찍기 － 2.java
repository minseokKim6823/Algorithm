import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        for(int i= input; i>0; i--){
            for(int j = 0; j <i-1; j++) {
                System.out.print(" ");
            }
            for(int k=0; k<input-i+1; k++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
