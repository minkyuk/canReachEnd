**Naive implementation without memoization.** <br />

 
Testing canReachEnd1 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.003669333.<br /> 
&nbsp; Best runtime was 0.002925653.<br />
&nbsp; &nbsp;  Average runtime was 0.0037864106.<br />

<br />
**Implementation with memoization, but using additional function attribute for cache** <br />


Testing canReachEnd2 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.0004544. <br /> 
&nbsp; Best runtime was 0.00044416. <br />
&nbsp; &nbsp;  Average runtime was 0.0004648108. <br />

<br />
**Implementation with memoization; No global cache required.** <br />


Testing Memoized Function <br />
Out of 5 repeats, <br /> 
&nbsp; Worst runtime was 0.00052608. <br /> 
&nbsp; Best runtime was 0.000510294. <br />
&nbsp; &nbsp; Average runtime was 0.0004577282. <br />

<br />
**Fast Implementation by checking reachability up to index i ~ up to last index in O(n) runtime.
(DP-approach)**<br />

Testing canReachEnd4 <br />
Out of 5 repeats, <br />
&nbsp; Worst runtime was 0.002449067. <br /> 
&nbsp; Best runtime was 0.003024213. <br />
&nbsp; &nbsp;  Average runtime was 0.00268288. <br />


Memoization added x8.3 boost in performance on average to a base-line. <br />
Just checking reachability in O(n) was x1.4 boost in performance on average to a base-line. <br />

The description for each function is included in the code in the comment. 
