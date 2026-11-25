#include <cassert>

#define main solution_main
#include "../../solutions/cpp/practice2.cpp"
#undef main

int main() {
    assert(isPalindrome("A man, a plan, a canal: Panama") == true);
    assert(isPalindrome("race a car") == false);
    assert(isPalindrome(" ") == true);
    assert(isPalindrome("0P") == false);
    return 0;
}

