class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> freqs; // num : count
        vector<int> res;

        // initialize counts
        for(int i = 0; i < nums.size(); i++){
            freqs[nums[i]]++;
        }

        // put them into buckets indexed by frequency
        vector<vector<int>> buckets(nums.size() + 1);
        for (const auto& [num, count] : freqs) {
            buckets[count].push_back(num);

        }

        // iterate backwards until k is 0
        for(int i = buckets.size(); i > 0; i--){
            

            for(int j = buckets[i - 1].size(); j > 0; j--){
                res.push_back(buckets[i - 1][j - 1]);
                k--;
                if(k == 0){
                    return res;
                }
                //cout << buckets[i - 1][j - 1] << endl;
            }   
        }
        return res;
    }
};
