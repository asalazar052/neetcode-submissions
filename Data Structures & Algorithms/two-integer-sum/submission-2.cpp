class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> mapper; // value : index

        for(int i = 0; i < nums.size(); i++){
            int want = target - nums[i];

            if(mapper.contains(want)){
                return {mapper[want], i};
            }
            mapper[nums[i]] = i;

        }
    }
};
