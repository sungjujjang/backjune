#include <stdio.h>

int n, s, cnt, i;
int a[20];

void bubun(int idx, int sum) {
    if (idx == n) {
        if (sum == s) cnt++;
        return;
    }

    bubun(idx + 1, sum + a[idx]);
    bubun(idx + 1, sum);
}

int main() {
    scanf("%d %d", &n, &s);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
	bubun(0, 0);
	if (s == 0) {
		cnt--;
	}
	printf("%d", cnt);
    return 0;
}