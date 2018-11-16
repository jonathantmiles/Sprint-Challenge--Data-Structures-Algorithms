Add your answers to the Algorithms exercises here.

=== PART I ===

a) The algorithm will run (n/2) + 1 times.

Each time through a == x * n^2 where x is two times the number of times the loop has been run, minus 1 (because the first loop starts at 0). Since the coefficient x has to exceed the value of n for the loop to stop, it has to run until x >= n. That's half the value of n (n/2) plus the first loop (+1).

b) (n)(n-1)(n-2)(n+4) times. (Could be simplified into about n^4 times.)

Each of the first three loops runs one fewer time than its container, starting with the i-loop running n times (0...n-1). The fourth loop runs (10 + k - 1) times, for which I've simplified by replacing k with the (n - 3) value from running k-loop.

c) the algorithm will run 'bunnies' + 1 times

Each time through the loop only removes one (-1) from the bunnies value, but it runs a final time when bunnies == 0.
