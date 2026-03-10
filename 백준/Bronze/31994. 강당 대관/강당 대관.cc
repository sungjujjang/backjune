#include <stdio.h>

int main() {
	char semina[7][100];
	int people[7], i;
	
	for (i=0; i<=6; i++) {
		scanf("%s %d", semina[i], &people[i]);
	}
	int temp = 0;
	for (i=1; i<=6; i++) {
		if (people[temp] < people[i]) {
			temp = i;
		}
	}
	
	printf("%s", semina[temp]);
}