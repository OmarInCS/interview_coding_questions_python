
'''

6. Triangle Or Not?
A student is given 3 poles and has been asked to find out if they can form a non-degenerate triangle.  If the 3 poles are placed with tips joined such that they form a triangle with non-zero angles at each vertex, then a non-degenerate triangle is formed.

Poles with length  [3, 4, 5] will make a non-degenerate triangle while [1, 1, 5] will not.



Function Description

Complete the function triangleOrNot in the editor below. The function must return an array of n strings where the value at each index i is Yes if a[i], b[i], and c[i] can form a non-degenerate triangle; otherwise, it is No.

triangleOrNot has the following parameter(s):

    a[a[0],...a[n-1]]:  array of n integers where each index i describes the length of side a for triangle i

    b[b[0],...b[n-1]]:  array of n integers representing lengths of sides b[i]

    c[c[0],...c[n-1]]:  array of n integers representing lengths of sides c[i]

Constraints

1 ≤ n ≤ 105
1 ≤ a[i], b[i], c[i] ≤ 103 , where 0 ≤ i < n

Input Format For Custom Testing

Sample Case 0
Sample Input 0
3
7
10
7
3
2
3
4
3
2
7
4

Sample Output 0
No
No
Yes

Explanation 0
We want to check the following n = 3 possible triangles using the values given by a = [7, 10, 7], b = [2, 3, 4], and c = [2, 7, 4]:

a[0] = 7, b[0] = 2, and c[0] = 2 do not form a valid, non-degenerate triangle, so we store No in index 0 of our return array.
a[1] = 10, b[1] = 3, and c[1] = 7 do not form a valid, non-degenerate triangle, so we store No in index 1 of our return array.
a[2]= 7, b[2]= 4, and c[2] = 4 do form a valid, non-degenerate triangle, so we store Yes in index 2 of our return array.
We then return the array ["No", "No", "Yes"] as our answer.

'''


def triangle_or_not(a_list, b_list, c_list):
    answers = []
    for a, b, c in zip(a_list, b_list, c_list):
        if a + b > c and a + c > b and b + c > a:
            answers.append("Yes")
        else:
            answers.append("No")

    return answers
        

allLists = [[], [], []]
for i in range(3):
    n = eval(input())
    for j in range(n):
        value = eval(input())
        allLists[i].append(value)

ans = triangle_or_not(*allLists)

for value in ans:
    print(value)