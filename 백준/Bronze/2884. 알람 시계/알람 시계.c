#include<stdio.h>

int main(void)
{
    int H,M;
    scanf("%d",&H);
    scanf("%d",&M);
   
    if(H==0&&M<45){
        H=23;
        M=60+(M-45);
        printf("%d %d",H,M);
    }
    else if(M<45){
         H -=1;
         M=60+(M-45);
         printf("%d %d",H,M);
    }
    else{
        M-=45;
        printf("%d %d",H,M);
    }
    return 0;
}
       
    