#include<stdio.h>

int main(void)
{ 
    int cnt,a,N;
    scanf("%d",&N);
    for(cnt=1;cnt<=N;cnt++){
        for(a=1;a<=cnt;a++)
            printf("*");
          printf("\n");
    }
  return 0;
}
