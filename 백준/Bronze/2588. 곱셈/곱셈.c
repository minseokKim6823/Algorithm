#include<stdio.h>

int main(void) {
    int a, b, c, d, e, f;
    scanf("%d %d", &a, &b);
    printf("%d\n", a * (b % 10));
    printf("%d\n", a * ((b / 10) % 10));
    printf("%d\n", a * (b / 100));

    f = a * (b % 10);
    e = a * ((b / 10) % 10) * 10;
    d = a * (b / 100) * 100;
    printf("%d\n", d + e + f);

    return 0;
}
