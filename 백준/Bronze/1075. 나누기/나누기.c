#include <stdio.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int n, f, temp, i;
	scanf("%d", &n);
	scanf("%d", &f);
	temp = n % 100;
	n = n - temp;
	for (i = 0; i <= 99; i++) {
		if (n % f == 0) {
			break;
		}
		n++;
	}
	printf("%02d", n%100);
	return 0;
}