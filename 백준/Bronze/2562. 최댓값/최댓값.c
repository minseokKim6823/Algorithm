#include<stdio.h>

int main(void)
{
	int a[9];
	int i, num = 0, gab = 0,t=0,max =0;
	
	for (i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		max = a[0];
	}
	for(i=1;i<9;i++){
		if (max < a[i]) {
			max = a[i];
			t = i;
		}	
	}
	printf("%d\n",max);
	printf("%d",t+1);
	return 0;
}