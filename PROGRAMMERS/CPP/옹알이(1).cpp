#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;

int solution(vector<string> babbling) {
    map<string, bool> possible {
        {"aya",false}, {"ye",false}, {"woo",false}, {"ma",false}
    };
    string word;
    int answer = 0;
    
    for (string babb: babbling){
        possible["aya"] = false;
        possible["ye"] = false;
        possible["woo"] = false;
        possible["ma"] = false;
        word = "";
        for (auto b: babb){
            word += b;
            if(possible.find(word) != possible.end()){
                possible[word] = true;
                word = "";
            };
        };
        
        if (word.empty()){
            answer += 1;
        };

    }
    
    return answer;
}