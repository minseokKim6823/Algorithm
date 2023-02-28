#include<stdio.h>

int main(void)
{
	int A, B, C=0,D=0;

	scanf("%d", &A);
	C = A;
	do {
			B = C / 10 + C % 10;
			C = (C % 10) * 10 + (B % 10);
			D++;
	} while (A != C);
	printf("%d", D);
return 0;
}