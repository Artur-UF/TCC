#include "lib.h"


int main(){

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for(int i = 0; i < 10; ++i){
        printf("Dentro do %d\n", i);
        for(int j = 0; j < 10; ++j){
            if(i == j){
                printf("%d\n", arr[i]);
                break;
            }
        }
        printf("saindo do %d\n", i);
    }

    return 0;
}



