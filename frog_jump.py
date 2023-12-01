'''A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.''''
 
 def function():
    initial = int(input("Enter the initial position"))
    final = int(input("Enter finalposition"))
    d = int(input("Enter the distance hopped in one jump"))
    diff = final - initial
    if diff % d == 0:
         return (diff)
    else:
         return (diff + 1)     

print(function())
