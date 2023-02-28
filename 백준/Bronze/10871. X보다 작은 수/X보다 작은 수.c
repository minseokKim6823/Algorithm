#include<stdio.h>

int main(void)
{
	int X, N, cnt;

	scanf("%d %d", &N, &X);

	for (cnt = 1; cnt <= N; cnt++) {
		int a;
		scanf("%d", &a);
		if (a < X)
			printf("%d ", a);
	}
	return 0;
}