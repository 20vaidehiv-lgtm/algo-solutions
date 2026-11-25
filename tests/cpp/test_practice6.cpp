// Note: solutions/cpp/practice6.cpp is currently marked IN PROGRESS.
#include <cassert>

#define main solution_main
#include "../../solutions/cpp/practice6.cpp"
#undef main

int main() {
    assert(search({4, 5, 6, 7, 0, 1, 2}, 0) == 4);
    assert(search({4, 5, 6, 7, 0, 1, 2}, 3) == -1);
    assert(search({1}, 0) == -1);
    assert(search({3, 1}, 1) == 1);
    return 0;
}

