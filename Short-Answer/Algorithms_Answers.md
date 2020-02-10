#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This one is O(n) as it loops once through the data scaling in a lenear fashion in relation to the input size.

b) This is O(log n) When the function hits the while loop, it runtime will grow at a slower rate as n increases.

c) It is using a linear runtime, O(n). It is a basic recursive function that scales proportional to n. This allows the runtime to be quick as n increase in scale.

## Exercise II

The approach this problem requires would be making use of a binary seach as we will look at the building floors as a sorted list. This approach will allow us to find the highest floor. This will save time as we will not have to test each individual floor. An example would be if it was a 50 story building, we drop the egg from the midpoint of the list, which is 25 stories. if the egg breaks then move down to 12 stories. If it doesnt we move up to 37 stories. If it breaks then we half and move down to 18 stories. Binary seach is a powerful tool as it allows us to halve the number of floors each time we make an attempt to solve the problem. Stoping once we find our answer.

It would have a time complexity of O(Log n)
