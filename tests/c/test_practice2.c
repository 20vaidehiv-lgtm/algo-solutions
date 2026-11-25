#include <assert.h>
#include <stdio.h>
#include "../../solutions/c/practice2.c"

int main(void) {
    int a1[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    assert(maxSubArray(a1, 9) == 6);

    int a2[] = {1};
    assert(maxSubArray(a2, 1) == 1);

    int a3[] = {5, 4, -1, 7, 8};
    assert(maxSubArray(a3, 5) == 23);

    printf("practice2 Maximum Subarray: all cases passed\n");
    return 0;
}

