#include <cassert>
#include <vector>

#define main solution_main
#include "../../solutions/cpp/practice1.cpp"
#undef main

int main() {
    assert((twoSum({2, 7, 11, 15}, 9) == std::vector<int>{0, 1}));
    assert((twoSum({3, 2, 4}, 6) == std::vector<int>{1, 2}));
    assert((twoSum({3, 3}, 6) == std::vector<int>{0, 1}));
    assert((twoSum({1, 2, 3}, 10).empty()));
    return 0;
}

