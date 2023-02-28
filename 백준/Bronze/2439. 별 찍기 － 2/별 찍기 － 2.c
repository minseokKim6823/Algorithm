#include<stdio.h>

int main(void)
{
    int cnt, N, A,B;
    scanf("%d", &N);
    for (cnt = 1; cnt <= N; cnt++){

        for (A = N - cnt; A>=1; A--) {
            printf(" ");
        }
        for (B = 1; cnt >= B; B++)
            printf("*");
        printf("\n");      
    }
    return 0;
}