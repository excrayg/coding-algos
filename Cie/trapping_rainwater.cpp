//https://leetcode.com/problems/trapping-rain-water/

//time: from 10:10 to 

//[0,1,0,2,1,0,1,3,2,1,2,1]


int trap(vector<int> &nums) {
  int n = nums.size(); if (n == 0) return 0;
  
  int i = 0; while (i < n - 1 && nums[i] <= nums[i + 1]) ++i;
  
  int res = 0;
  stack <pair<int, int> > premax;
  premax.push(make_pair(i, nums[i])); 
  vector<int> aux = nums;
  
  ++i;
  
  
  while (i < n) {
      //  is to find one bottom
    while (i < n - 1 && nums[i] < nums[i + 1]) ++i;
    
    pair<int, int> tmph;
    
    //why does stack have pair? what is pair in this?
    //what does this while loop do? former will always higher than the later
    while (!premax.empty() && premax.top().second <= nums[i]) {
      tmph = premax.top();
      premax.pop();
    }
    
    if (!premax.empty()) tmph = premax.top();
    //
    int h = min(tmph.second, nums[i]); // 5,3,3,6 2,2,3
    // 
    for (int j = tmph.first + 1; j < i; ++j) {
      if (h - aux[j] > 0) {
        res += h - aux[j];
        aux[j] = h;
      }
    }
    //
    premax.push(make_pair(i, nums[i]));
    ++i;
    // this loop is to find one top
    while (i < n && nums[i - 1] >= nums[i]) ++i;
  }
  return res;
}