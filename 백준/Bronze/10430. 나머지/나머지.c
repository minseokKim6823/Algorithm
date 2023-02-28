#include <stdio.h>

int main()
{
    int A,B,C;
    scanf("%d %d %d",&A,&B,&C);
    if (2<=A<=10000||2<=B<=10000||2<=C<=10000){
    printf("%d\n",(A+B)%C);
    printf("%d\n",((A%C)+(B%C))%C);
    printf("%d\n",(A*B)%C);
    printf("%d\n",((A%C)*(B%C))%C);
    }
   
    return 0;
}