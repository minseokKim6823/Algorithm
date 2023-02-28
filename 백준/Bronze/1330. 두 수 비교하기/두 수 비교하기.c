#include<stdio.h>

int main(void) {
    int A,B;
    scanf("%d %d",&A,&B);
    if(-10000<=A&&A<=10000&&-10000<=B&&B<=10000)
        if(A>B)
      printf(">");
    else if(A<B)
        printf("<");
    else
        printf("==");
    return 0;
     
}
