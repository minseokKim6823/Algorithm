#include<stdio.h>

int main(void)
{
    int jumsu;
    scanf("%d",&jumsu);
    if(90<=jumsu&&jumsu<=100)
        printf("A");
    else if(80<=jumsu&&jumsu<=89)
        printf("B");
    else if(70<=jumsu&&jumsu<=79)
        printf("C");
    else if(60<=jumsu&&jumsu<=69)
        printf("D");
    else
        printf("F");
    
    return 0;
}