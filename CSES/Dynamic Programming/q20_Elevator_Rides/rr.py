"""


                Elevator Rides

Task
Submit
Results
Statistics
Tests







CSES - Elevator Rides




addEventListener("DOMContentLoaded", function (e) {
    const mathElements = document.getElementsByClassName("math");
    const macros = {};
    for (let element of mathElements) {
        katex.render(element.textContent, element, {
            displayMode: element.classList.contains("math-display"),
            throwOnError: false,
            globalGroup: true,
            macros,
        });
    }
});


Time limit: 1.00 s
Memory limit: 512 MB

There are n people who want to get to the top of a building which has only one elevator. You know the weight of each person and the maximum allowed weight in the elevator. What is the minimum number of elevator rides?
Input
The first input line has two integers n and x: the number of people and the maximum allowed weight in the elevator.
The second line has n integers w_1,w_2,\dots,w_n: the weight of each person.
Output
Print one integer: the minimum number of rides.
Constraints

1 \le n \le 20
1 \le x \le 10^9
1 \le w_i \le x

Example
Input:
4 10
4 8 6 1

Output:
2

"""
