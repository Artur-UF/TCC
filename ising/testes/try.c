#include <sys/resource.h>
#include <stdio.h>
#include <stdlib.h>


int main (int argc, char **argv)
{
    const rlim_t kStackSize = 16L * 1024L * 1024L;   // min stack size = 64 Mb
    struct rlimit rl;
    int result;

    printf("Antes\n");
    system("ulimit -s");

    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
            }
            printf("Depois\n");
        }
    }


    system("ulimit -s");
    return 0;
}
