#include <stdio.h>

int main() {
	int n, num=0, a,b,c, cc=0;
	
	scanf("%d", &n);
	num = n;
	while (1) {
		a = num/10;
		b = num%10;
		c= (a+b)%10;
		num = (b*10) + c;
		
		cc += 1;
		if (num == n) {
			break;
		}
	}
	printf("%d", cc);
}