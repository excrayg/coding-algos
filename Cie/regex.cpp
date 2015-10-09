// Implement regular expression matching with support for ‘.’ and ‘*’.

// ‘.’ Matches any single character.
// ‘*’ Matches zero or more of the preceding element.
// The matching should cover the entire input string (not partial).

// The function prototype should be:
// bool isMatch(const char *s, const char *p)

// Some examples:
// isMatch(“aa”,”a”) → false
// isMatch(“aa”,”aa”) → true
// isMatch(“aaa”,”aa”) → false
// isMatch(“aa”, “a*”) → true
// isMatch(“aa”, “.*”) → true
// isMatch(“ab”, “.*”) → true
// isMatch(“aab”, “c*a*b”) → true

// time: from 9:45 to 10:10 
// first try: misunderstood the problem
// second try: succeed
#include "utils.h"


string formatP(string p) {
  string res = "";
  res += p[0];
  int i = 1, j = 0, len_p = p.length();
  while (i < len_p) {
    if (p[i] == '*' && i + 2 < len_p && p[i - 1] == res[j] && p[i + 1] == res[j] && p[i + 2] == '*') {
      i += 2;
    } else {
      res += p[i];
      i++; j++;
    }
  }
  return res;
}
bool isMatch(string s, string p) {
  int i = 0, j = 0, len_s = s.length(), len_p = p.length();
  if (len_p == 0 && len_s == 0) return true;
  if (len_p == 0) return false;
  p = formatP(p);
  len_p = p.length();
  if (len_s == 0) {
    int tmpj = j;
    while (tmpj + 1 < len_p && p[tmpj + 1] == '*') tmpj += 2;
    if (tmpj == len_p) {
      return true;
    } else {
      return false;
    }
  }
  while (i < len_s && j < len_p) {
     if (j + 1 < len_p && p[j + 1] == '*') {
      //.*
      if (p[j] == '.') {
        //last .*
        if (j + 2 == len_p) return true;

        //middle .*
        //not use .*
        if (isMatch(s.substr(i), p.substr(j + 2))) return true;
        //use .* as one char
        i++;
      } else {//c*
        //useless char*
        if (s[i] != p[j]) {
          j += 2;
          continue;
        }
        //last c*
        if (j + 2 == len_p) {
          int tmpi = i;
          while (tmpi < len_s && s[tmpi] == p[j]) tmpi++;
          if (tmpi == len_s) return true;
        }
        //middle c* and s[i] = p[j]
        //not use c*
        if (isMatch(s.substr(i), p.substr(j + 2))) return true;
        //use c* as one char
        i++;
      }
    } else if (p[j] == '.' || p[j] == s[i]) {
       i++; j++;
    } else {
      return false;
    }
  }
  while (j + 1 < len_p && p[j + 1] == '*') j += 2;
  return i == len_s && j == len_p;
}

int main() {
    // res: 0,1,1,1,0,1,0,1,1,0
    string ss[] = {"aa","aa","aa","aa","aa", "aa", "aa", "aa", "aa", "abababababab"};
    string ps[] = {"a", "a.","a*",".*",".*b","a*a","a.a","a*.","a.*", "a*.b*.a*.b*.b"};
    int sz = 10;
    for (int i = 0; i < sz; ++i) {
        cout << isMatch(ss[i], ps[i]) << endl;
    }
    return 0;
}