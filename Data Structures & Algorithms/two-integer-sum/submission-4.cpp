class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> mapper; // value : index

        for(int i = 0; i < nums.size(); i++){

            if(mapper.contains(target - nums[i])){
                return {mapper[target - nums[i]], i};
            }
            mapper[nums[i]] = i;

        }
    }
};
