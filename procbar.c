#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void ProcessBar(float proc, float base);

int main()
{
	for (int i = 0; i<=5; i++){
		ProcessBar(i*10., 50.);
		sleep(1);
	}

}



void ProcessBar(float proc, float base)
{
	int i=0, j=0;
	int percent = proc/base*100;
	printf("\r[");
	for (i=0; i<percent/2; i++ )
		printf("="); 
	for (j=i; j<50; j++ )
		printf(" ");
	printf("][%d%%]", percent);
	fflush(stdout);
	if(percent==100)printf("\n");
}