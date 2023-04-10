#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(vector<int> command: commands) {
        int s = command[0];
        int e = command[1];
        int k = command[2];
        vector<int> tmp;
        for (int i=0; i<array.size(); i++) {
            if(i+1 >= s && i+1 <= e) {
                tmp.push_back(array[i]);
            }
        }
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp[k-1]);
    }
    
    return answer;
}