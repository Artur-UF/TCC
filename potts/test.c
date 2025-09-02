#include"lib.h"


int main(){
    int seed = time(NULL);
    srand(seed);

    for(int i = 0; i < 10; i++){
        printf("%d\n", (int)uniform(0., 3.));
    }
    return 0;
}


