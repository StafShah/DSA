class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> nums(nums1.size() + nums2.size());
        std::merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), nums.begin());
        int index = nums.size() - 1;

        if (nums.size() % 2 == 0) {
            int first_idx = index / 2;
            int second_idx = std::ceil(index / 2.0);
            double result = (nums[first_idx] + nums[second_idx]) / 2.0;
            return result;
        } else {
            int idx = index / 2;
            double result = nums[idx];
            return result;
        }
    }
};