// Problem: Length of Last Word
// Source: https://leetcode.com/problems/length-of-last-word/
// Topic: strings
// Status: Done

#include <iostream>
#include <string>
#include <cassert>

int lengthOfLastWord(std::string s){
    int k=0;

    for(int i=static_cast<int>(s.length())-1; i>=0; i--){
        if(s[i] != ' '){
            k++;
        }
        if(k != 0 && s[i] == ' ')
            return k;
    }
    return k;
}


int main(){
    // Example 1
    assert(lengthOfLastWord("Hello World") == 5);

    // Example 2
    assert(lengthOfLastWord("   fly me   to   the moon  ") == 4);

    // Example 3
    assert(lengthOfLastWord("luffy is still joyboy") == 6);

    // Edge cases
    assert(lengthOfLastWord("a") == 1);
    assert(lengthOfLastWord("   a   ") == 1);
    assert(lengthOfLastWord("word") == 4);
    assert(lengthOfLastWord("   word   ") == 4);
    return 0;
}