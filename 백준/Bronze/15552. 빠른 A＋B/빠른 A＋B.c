#include<stdio.h>

int main(void)
{
    int A,cnt,B,T;
    scanf("%d",&T);
    T<= 100000;
    for (cnt = 1; cnt <= T; cnt++) {
        scanf("%d %d", &A, &B);
        1 <= A && A <= 1000;
        1 <= B && B <= 1000;
        printf("%d\n", A + B);
    }
    return 0;
}