#include <assert.h>
#include <stdio.h>
#include "../../solutions/c/practice1.c"

int main(void) {
    assert(totalNQueens(1) == 1);
    assert(totalNQueens(4) == 2);
    assert(totalNQueens(5) == 10);
    printf("practice1 N-Queens II: all cases passed\n");
    return 0;
}

