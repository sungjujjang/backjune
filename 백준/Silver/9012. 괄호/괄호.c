#include <stdio.h>
#include <string.h>

#define MAX 100

int main() {
	int t, len;
	scanf("%d", &t);
	for (int i=0; i<t; i++) {
		char temp[50];
		int stack[50];
		int top = 0, su = 1;
		
		scanf("%s", temp);
		len = strlen(temp);
		
		for (int j=0; j<len; j++) {
			if (temp[j] == '(') {
				stack[top++] = 0;
			} else if (temp[j] == ')') {
				if (top <= 0) {
					su = 0;
					break;
				}
				top--;
			}
		}
		if (top > 0) {
			su = 0;
		}
		if (su == 0) {
			printf("NO\n");
		} else {
			printf("YES\n");
		}
	}
}