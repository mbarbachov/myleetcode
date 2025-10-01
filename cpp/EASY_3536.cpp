/**
 * @brief You are given a positive integer n.
 * Return the maximum product of any two digits in n.
 * Note: You may use the same digit twice if it appears more than once in n.
 * @author mbarbachov
 *
 * @date 09/29/2025 - Created by mbarbachov
 * @date 09/29/2025 - Solved w/
 */

#include <iostream>

class EASY_3536 {
public:
    int maxProduct(int n) {
        // intialize 
        int max1 = n % 10, max2 = n / 10;
        std::string nToString = std::to_string(n);

        // Loop through list O(n) & find value of max
        for (char c : nToString) {
            int currC = c - '0';  // c - '0' returns just the digit that c represents
            if (currC > max1) {
                max2 = max1;
                max1 = currC;
            } else if (currC > max2) {
                // New max is found for max 2 but max1 isn't updated
                max2 = currC;
            }   
        }

        return max1 * max2;
    }
};
