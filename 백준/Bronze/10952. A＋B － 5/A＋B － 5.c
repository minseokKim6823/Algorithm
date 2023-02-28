#include<stdio.h>

int main(void)
{
    int A, B, C = 0;
    do{
    scanf("%d %d",&A,&B);
        if(0<A&&B<10){ 
            C=A+B;
        printf("%d\n",C);          
        }
        else
            break;
   
    }while(1);
    
    return 0;
}