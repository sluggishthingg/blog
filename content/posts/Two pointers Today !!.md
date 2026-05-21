---
title: dsa learning
date: 2026-05-21
author: Sluggishthing
description: two pointer problems
---
Recently i came across a new technique to learn dsa fast thats's pattern recognition so i hopped on chatgpt and asked a list of questions to learn for dsa from each topic based on patterns it gave me a bunch of questions to practice on pattern wise so i set my starting point there.

when i solve a problem i also look for the
      . brute
      .optimal

## 1. LeetCode Two Sum II – Input Array Is Sorted

[LeetCode 167 – Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?utm_source=chatgpt.com)


THOUGHT PROCESS

i analyzed the question and found that the array is 1- indexed, already sorted , similar to two sum and the output should be returned in an array format

 APPROACH 
 
for brute force i thought to go with nested loops and finding the target ,initializing a new array with the values {-1,-1}  and assigning the matched (i,j) values to indexes res[0],res[1] while increasing them by one place

#### CODE (BRUTE FORCE)
![](Pasted%20image%2020260521195521.png)

#####  CODE OPTIMAL 

THOUGHT  PROCESS

next for the optimal approach i thought why not go for 2 pointers initialize a left and a right pointer iterate it only O(N) as opposed to O(N^2)

![](Screenshot%20From%202026-05-21%2019-59-00.png)

 ##### HASH BASED CAUSE WHY NOTT MAKE IT MORE OPTIMAL !!

THOUGHT PROCESS

i initialized a hashmap and used a for loop to iterate the array values then i found out the remainder of each value when subtracted from target (int rem=target-arr[i]) that way i can easily find out the target without going through the whole array . I push the array values to the map if not found and if rem is in map i find out its index return it along with the original i value

... i know i sound  a little confused in the headd ... please bear with me i'm just adjusting the thoughts in my head


##### CODE HASH
![](Screenshot%20From%202026-05-21%2020-07-54.png)

## 2. LeetCode Valid Palindrome

[LeetCode 125 – Valid Palindrome](https://leetcode.com/problems/valid-palindrome/?utm_source=chatgpt.com)

THOUGHT PROCESS

i thought first i should go with removing all the spaces along with converting them to lowercase.. I didnt know exactly how to remove the white spaces when it got those ' , : ' and other punctuation marks i referred google and got the syntax replaceAll("[^a-z0-9]","")

##### CODE
![](Screenshot%20From%202026-05-21%2020-13-18.png)

on the side note i didnt try out any optimal or better solutions for this problem .. thats for another day i guess

## 3. LeetCode Container With Most Water

[LeetCode 11 – Container With Most Water](https://leetcode.com/problems/container-with-most-water/?utm_source=chatgpt.com)


THOUGHT PROCESS

i didnt get the question first i thought to take the maximum values btw those maximum take the min value and square it and thats it

then i found out that you gotta find the maximum area that means max heights along with max width area =height * width (-------------)

##### BRUTE CODE
![](Screenshot%20From%202026-05-21%2020-20-34.png)

THOUGHT PROCESS

for the optimal i went with two pointer approach a left and right pointer and used the greedy approach to arrive to a solution condition left =0 , right = n-1 (if left<right) left++ else (right--)

##### OPTIMAL CODE
![](Screenshot%20From%202026-05-21%2020-26-05.png)

#### THATS IT FOR TODAY THANK FOR READING------- peace outt  !!!!!----------