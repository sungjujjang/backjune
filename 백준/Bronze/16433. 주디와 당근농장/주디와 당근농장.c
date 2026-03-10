#include <stdio.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int n, c, r, i, j, front;
	scanf("%d %d %d", &n, &r, &c);
	front = (r+c) % 2;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			if ((i+j) % 2 == front) {
				printf("v");
			} else {
				printf(".");
			}
		}
		printf("\n");
	}
}