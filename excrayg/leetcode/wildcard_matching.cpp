#include <iostream>
using namespace std;

class Solution {
public:
    bool isMatch(std::string& s1, std::string& p1) {
        const char *s = s1.c_str();
        const char *p = p1.c_str();
        char cs = *s;
        char cp = *p;
        if(cp == '\0') {
            return cs == cp;
        } else if (cp == '?') {
            if (cs == '\0') return false;
            string s1(s+1);
            string p1(p+1);
            return isMatch(s1, p1);
        } else if (cp == '*') {
            const char *st = s;
            for(; *st != '\0'; ++st) {
                string st1(st);
                string p1(p+1);
                if (isMatch(st1, p1)) return true;
            }
            string st1(st);
            string p1(p+1);
            return isMatch(st1, p1);
        } else if (cp != cs)
            return false;
        string st1(s+1);
        string p2(p+1);
        return isMatch(st1, p2);
    }
};

int main()
{
    
    Solution s;
    return 0;
}