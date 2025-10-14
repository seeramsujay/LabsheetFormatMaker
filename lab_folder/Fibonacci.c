#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Fibonacci of %d is %d\n", num, fibonacci(num));
    return 0;
}