#include <stdio.h>
int main() {
    double x, y; 
    scanf("%lf", &x);
    if (x < 1) {
        y = x;
    } else if (x < 10) {
        y = x - 1;
    } else {
        y = 3 * x - 11;
    }
    printf("y=%.2f\n", y);
    return 0;
}
