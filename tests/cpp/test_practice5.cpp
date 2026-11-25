#include <cassert>
#include <climits>
#include <vector>

#define main solution_main
#include "../../solutions/cpp/practice5.cpp"
#undef main

int main() {
    std::vector<int> a = {100, 4, 200, 1, 3, 2};
    assert(longestConsecutive(a) == 4);

    std::vector<int> b = {};
    assert(longestConsecutive(b) == 0);

    std::vector<int> c = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
    assert(longestConsecutive(c) == 9);
    return 0;
}

