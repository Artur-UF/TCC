.RECIPEPREFIX = {

FLAGS = -lm -g -Wall -O3
OUTFILE = out

out: ising2D.o lib.o
{ gcc ising2D.o lib.o -o $(OUTFILE) $(FLAGS)

ising2D.o: ising2D.c
{ @gcc -c ising2D.c $(FLAGS)

lib.o: lib.c lib.h
{ @gcc -c lib.c $(FLAGS)

clean:
{ rm *.o $(OUTFILE)
