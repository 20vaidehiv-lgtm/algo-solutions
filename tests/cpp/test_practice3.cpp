#include <cassert>
#include <vector>

#define main solution_main
#include "../../solutions/cpp/practice3.cpp"
#undef main

int main() {
    std::vector<int> a = {0, 1, 0, 3, 12};
    moveZeroes(a);
    assert((a == std::vector<int>{1, 3, 12, 0, 0}));

    std::vector<int> b = {0};
    moveZeroes(b);
    assert((b == std::vector<int>{0}));

    std::vector<int> c = {};
    moveZeroes(c);
    assert(c.empty());
    return 0;
}

