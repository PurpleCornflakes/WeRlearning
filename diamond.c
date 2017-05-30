#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[])
{
	int n = atoi(argv[1]);
	if(n%2 == 0) n += 1;
	int i, k, n_space, n_star;
	for(i=0; i<n; i++){
		n_space = abs((n-1)/2-i);
		n_star = 2*((n-1)/2-n_space)+1;
		for(k = 0; k < n_space ; k++) printf(" ");
		for(k = 0; k < n_star; k++) printf("*");
		printf("\n");	
	}

}
