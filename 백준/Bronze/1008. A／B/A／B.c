#include<stdio.h>

int main(void) {

    int A, B;
    scanf("%d %d", &A, &B);
    if (0 < A, B < 10)
      printf("%.10lf",(double)A/B);

    return 0;
}