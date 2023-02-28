#include<stdio.h>

int main(void)
{
    int N,cnt,gab=0;
    scanf("%d",&N);
    N>=1&&N<=9;
    for(cnt=1;cnt<=9;cnt++){
        gab=N*cnt;
        printf("%d * %d = %d\n",N,cnt,gab);
    }
    
        return 0;
}