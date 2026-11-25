// Problem: Valid Palindrome
// Source: https://leetcode.com/problems/valid-palindrome/
// Topic: Two Pointers, String

#include <string>
#include <cctype>

using namespace std;

bool isPalindrome(const string& s) {
    int left = 0;
    int right = static_cast<int>(s.length()) - 1;

    while (left < right) {
        while (left < right && !isalnum(static_cast<unsigned char>(s[left]))) {
            left++;
        }
        while (left < right && !isalnum(static_cast<unsigned char>(s[right]))) {
            right--;
        }

        if (tolower(static_cast<unsigned char>(s[left])) != tolower(static_cast<unsigned char>(s[right]))) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}

int main() {
    return 0;
}

