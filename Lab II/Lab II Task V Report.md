The population dynamics were studied using the logistic equation
 
x_(t+1)=r*x_t*(1-x_t)

where x_t represents the population at time step t, and r is the growth factor. In this experiment the growth factor was fixed at r = 4, and several simulations were performed with different initial populations: 0.1, 0.5, 1.0, and 2.0.

When the initial population was 0.1, the population values changed rapidly and irregularly over time. The values jumped between low and high numbers without settling to a stable value. This behavior shows that when r = 4, the system is chaotic and very sensitive to the starting condition. 

For the case where the initial population was 0.5, the first iteration produced a value of 1.0, and the next iteration immediately became 0. After reaching zero, the population remained zero for all remaining steps. 

When the initial population was 1.0, the population also immediately dropped to 0 in the next step and stayed at zero afterwards. 

In the experiment where the initial population was 2.0, the values quickly became extremely large negative numbers and eventually reached negative infinity. This occurs because the logistic model normally assumes population values between 0 and 1, and starting outside this range causes the model to become unstable. 

Overall, these experiments show that for r = 4, the logistic model can produce chaotic or unstable behavior depending on the initial population value. Small differences in the starting value can lead to completely different population outcomes.
