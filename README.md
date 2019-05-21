# Timing report on 4 non-independent implemenations of _canReachEnd_

##### Problem: For an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.
[2,2,0,2,4] -> Yes
[3,2,1,0,4] -> No
[5] -> Yes

## **Naive implementation without memoization** 
## *
Testing canReachEnd1 
Out of 5 repeats, 
&nbsp; Worst runtime was 0.003669333.
&nbsp; Best runtime was 0.002925653.
&nbsp; &nbsp;  Average runtime was 0.0037864106.



## **Impl. with memoization, but using semi-global cache in func. attribute** 
## **
Testing canReachEnd2 
Out of 5 repeats, 
&nbsp; Worst runtime was 0.0004544.  
&nbsp; Best runtime was 0.00044416. 
&nbsp; &nbsp;  Average runtime was 0.0004648108. 



## **Implementation with memoization; No global cache.** 
### ***
Testing Memoized Function 
Out of 5 repeats, 
&nbsp; Worst runtime was 0.00052608. 
&nbsp; Best runtime was 0.000510294. 
&nbsp; &nbsp; Average runtime was 0.0004577282. 


## **Implementation by checking dynamic reachability up to index i ~ last index in O(n) runtime (DP-approach)** 
## *

Testing canReachEnd4 
Out of 5 repeats, 
&nbsp; Worst runtime was 0.002449067. 
&nbsp; Best runtime was 0.003024213. 
&nbsp; &nbsp;  Average runtime was 0.00268288. 


##### **Memoization added x8.3 boost in performance on average to a base-line.**
##### **Greedy checking on reachability in O(n) was x1.4 boost in performance on average to a base-line.** 
##### **Using global/non-global cache yields no difference in performance as expected**



More detail for each function is included in the code in the comment. 
unit: seconds
