## Timing report on 4 non-independent implemenations of _canReachEnd_

##### Problem: For an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.
[2,2,0,2,4] -> Yes
[3,2,1,0,4] -> No
[5] -> Yes

## **Naive implementation without memoization** <br />
## *
Testing canReachEnd1 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.003669333. <br />
&nbsp; Best runtime was 0.002925653. <br />
&nbsp; &nbsp;  Average runtime was 0.0037864106.<br />

<br />

## **Impl. with memoization, but using semi-global cache in func. attribute** <br />
## **
Testing canReachEnd2 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.0004544.  <br />
&nbsp; Best runtime was 0.00044416. <br />
&nbsp; &nbsp;  Average runtime was 0.0004648108. <br />

<br />

## **Implementation with memoization; No global cache.** <br />
### ***
Testing Memoized Function <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.00052608. <br />
&nbsp; Best runtime was 0.000510294. <br />
&nbsp; &nbsp; Average runtime was 0.0004577282. <br />

<br />

## **Checking dynamic reachability up to index i ~ last index in O(n) runtime (DP-approach)** <br />
## *

Testing canReachEnd4 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.002449067. <br />
&nbsp; Best runtime was 0.003024213. <br />
&nbsp; &nbsp;  Average runtime was 0.00268288. <br /> 


#### **Memoization added x8.3 boost in performance on average to a base-line.**
#### **Greedy checking on reachability in O(n) was x1.4 boost in performance on average to a base-line.** 
#### **Using global/non-global cache yields no difference in performance as expected**


<br />
More detail for each function is included in the code in the comment. <br />
unit: seconds
