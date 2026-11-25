// Problem: Length of Last Word
// Source: https://leetcode.com/problems/length-of-last-word/
// Topic: strings
// Status: Done

#include <string>

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
    return 0;
}