#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main (int argc, char **argv){

    FILE *readfile;
    char command[50], buffer[BUFSIZ + 1] = {0};
    int chars_read;
    int ok = 0, seed = 1702939903;
    do{ 
        sprintf(command, "find samples_L_%d/ -name *%d.dat", 200, seed);
        readfile = popen(command, "r");
        chars_read = fread(buffer, sizeof(char), BUFSIZ, readfile);
        if(chars_read > 0){
            seed += 2;
        }else{
            ok = 1;
        }
        memset(buffer, 0, (BUFSIZ +1)*sizeof(char));
        memset(command, 0, 50*sizeof(char));
        pclose(readfile);
    }while(ok == 0);
  

    printf("seed : %d\n", seed); 
    return 0;
}
