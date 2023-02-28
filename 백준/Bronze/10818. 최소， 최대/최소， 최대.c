#include <stdio.h>

int main()
{
	int N = 0;
	int min = 1000000;
	int max = -1000000;

	scanf("%d", &N);
    
    int *arr = malloc(sizeof(int) * N);
    
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
        
		if (arr[i] < min) min = arr[i];
		if (arr[i] > max) max = arr[i];
	}
    
	printf("%d %d", min, max);

	return 0;
}
