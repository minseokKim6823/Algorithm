#include<stdio.h>

int main(void)
{
int T,cnt,A,B,C=0;
    scanf("%d",&T);
    for(cnt=1;cnt<=T;cnt++){
        scanf("%d %d",&A,&B);
        C=A+B;
        printf("Case #%d: %d + %d = %d\n",cnt,A,B,C);
    }
    return 0;
}