#include <stdio.h>

int main() {
    int n, dasom, bribe = 0;
    int votes[50] = {0};

    scanf("%d", &n);
    scanf("%d", &dasom);

    for (int i = 1; i < n; i++) {
        scanf("%d", &votes[i]);
    }

    while (1) {
        int max_idx = 1;
        for (int i = 1; i < n; i++) {
            if (votes[i] > votes[max_idx]) {
                max_idx = i;
            }
        }
        if (votes[max_idx] < dasom) {
            break;
        }
        votes[max_idx]--;
        dasom++;
        bribe++;
    }

    printf("%d\n", bribe);
    return 0;
}