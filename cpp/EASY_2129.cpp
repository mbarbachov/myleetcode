/**
 * @brief You are given a positive integer n.
 * Return the maximum product of any two digits in n.
 * Note: You may use the same digit twice if it appears more than once in n.
 * @author mbarbachov
 *
 * @date 09/29/2025 - Created by mbarbachov
 * @date 09/29/2025 - Solved
 */

#include <iostream>

class EASY_2129 {
public:
    std::string capitalizeTitle(std::string title) {
        std::string result;
        int idx = 0, flag = 0;

        for (char c : title) {
            if (c == ' ' || idx == 0) {
                // Space means that the next letter has to be capitalized - so we set flag to 1
                flag = 1;
                idx++;  // doesn't matter if it keeps incrementing we only use this once (beggining of the title)
                continue;
            } 
            
            // calculate letter's position in alphabet (a -> 0, z -> 25)
            int cAscii = (int) c;
            if (c >= (int) 'a') {
                // 
            }

            if (flag == 1) {
                // Previous letter was a space
                flag == 0; // reset flag, make letter capital

            }
            result += c;
        }
        return "FAIL";
    }
};

/*
0MS solution from solutions tab on leet code - solved problem in python, did not know about tolower function; Had right idea, wrong implementation

class Solution {
public:
    string capitalizeTitle(string& title) {
        const int& len = title.size();
        int s = 0; // start index

        for(int i = 0; i < len; ++i){

            title[i] = tolower(title[i]); // convert all char to lower case

            if(title[i] == 32){ // similar to: title[i] == ' '

                if(i - s > 2) // check the length of word
                    title[s] = toupper(title[s]);

                s = i+1;
            }
        }

        if(len - s > 2) // check last word
            title[s] = toupper(title[s]);

        return move(title);// move fun to save memory
    }
};

*/