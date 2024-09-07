class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        int l = 0, r = height.size() - 1;

        while (l < r) {
            int area = (r - l) * std::min(height[l], height[r]);
            result = std::max(result, area);
            if (height[l] < height[r]) {
                l++;
            } else if (height[l] == height[r]) {
                if (height[l + 1] > height[r - 1]) {
                    l++;
                } else {
                    r--;
                }
            } else {
                r--;
            }
        }

        return result;
    }
};