#include <cassert>

#define main solution_main
#include "../../solutions/cpp/practice9.cpp"
#undef main

int main() {
    assert(lengthOfLastWord("Hello World") == 5);
    assert(lengthOfLastWord("   fly me   to   the moon  ") == 4);
    assert(lengthOfLastWord("luffy is still joyboy") == 6);
    assert(lengthOfLastWord("a") == 1);
    return 0;
}

