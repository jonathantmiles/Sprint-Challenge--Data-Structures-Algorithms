Add your answers to the Algorithms exercises here.

=== PART I ===

a) The algorithm will run (n/2) + 1 times.

Each time through a == x * n^2 where x is two times the number of times the loop has been run, minus 1 (because the first loop starts at 0). Since the coefficient x has to exceed the value of n for the loop to stop, it has to run until x >= n. That's half the value of n (n/2) plus the first loop (+1).

b) (n)(n-1)(n-2)9 times or (9n^3 - 27n^2 - 18n)

Each of the first three loops runs one fewer time than its container, starting with the i-loop running n times (0...n-1). The fourth loop, interestingly, always runs 9 times for each k loop (10 + k - 1) times, which I've rendered as a constant 9. 

c) the algorithm will run 'bunnies' + 1 times

Each time through the loop only removes one (-1) from the bunnies value, but it runs a final time when bunnies == 0.

=== PART II ===

For testing with the fewest broken eggs:
for each floor (starting at the first floor _n_ = 0) throw an egg out the window.
if the egg does not break, repeat with the floor next higher up (_n_ + 1)
the first time the egg breaks, record that the previous floor (the current _n_ - 1) is equal to _f_ (the highest floor from which eggs do not break)

For testing the fewest number of eggs overall (and ignoring that _f_ is likely to be very low, assuming real-world physics):
toss the egg off at _n_/2, the halfway point of the building. If it breaks, check that floor divided by 2 (to get lower) otherwise check halfway between the halfway point and the top of the building. The idea is to always check halfway, then go lower if need be, or higher if need be, getting closer and closer to the final output (just like in a guessing game where you're told if the target number is higher or lower than your guess).
