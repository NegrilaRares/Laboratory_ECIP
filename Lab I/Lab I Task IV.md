### 1. What is the difference between the true state and the observations?

The true state is the exact value of the system without noise.
The observations are the true state plus Gaussian noise.

The difference between them is the measurement noise:

y(t)−x(t)=v(t)

### 2. How does estimation reduce noise?

The moving average reduces noise by averaging multiple noisy samples.

Since Gaussian noise has zero mean, positive and negative errors cancel out.

### 3. How does changing noise level affect estimation?

If the noise standard deviation increases, the observations become more scattered around the true state. 

As a result, the estimation error increases because the measurements deviate more from the real signal.
To reduce this stronger noise, a larger moving average window is generally required. 

In other words, higher noise levels require stronger smoothing in order to obtain a stable estimate.

### 4. How does window size affect the result?

The window size determines the balance between smoothing and responsiveness. 

A small window performs limited smoothing, so more noise remains in the estimate, but the estimator responds quickly to changes. 
A large window provides stronger smoothing and reduces noise more effectively, but it introduces delay and makes the estimate less responsive. 

Therefore, increasing the window size improves noise reduction but increases lag.
