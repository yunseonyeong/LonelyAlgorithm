#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(string s) {
    stringstream ss(s);
    string answer;
    string splitted;
    vector<int> numbers;
    
    while(getline(ss,splitted,' ')) {
        int num = stoi(splitted);
        numbers.push_back(num);
    }
    auto minmax = minmax_element(numbers.begin(), numbers.end());
    answer = to_string(*minmax.first) + ' ' + to_string(*minmax.second);
    return answer;
}

int main() {
    string answer = "1 2 3 4";
    string result = solution(answer);
    cout << result << endl;
}