class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> duplicateMap;
        bool result=false;
        for(int i:nums)
        	if(duplicateMap.count(i)==0)
        		duplicateMap[i]=1;
        	else 
        		result=1;
        return result;
    }
};