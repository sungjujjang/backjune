# include <stdio.h>

int main() {
	int n;
	unsigned a = 0x80000000;
	scanf("%d", &n);
	if (n == 0) {
		printf("1");
		return 0;
	}
	int cnt=0, isl=0;
	for (int i = 0; i < 32; i++) {
        if ((a & n) == a) {
        	isl = 1;
        }
        if (isl == 1) {
        	cnt++;
		}
        a >>= 1;
    }
    printf("%d", cnt);
}