#include <stdio.h>

int main() {
    int n;
    int sum_n = 0;

    scanf("%d", &n);

    for(int i = 0; i <= n; i++) {
        sum_n += i;
    }

    printf("%d\n", sum_n);

    return 0;
}