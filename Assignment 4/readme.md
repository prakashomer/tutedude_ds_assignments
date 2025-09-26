### Notes and learning points
- Small synthetic dataset requires augmentation or regularization — here we used random pixel flips to create training variability.
- Network: Input (30) -> Hidden (16 with sigmoid) -> Output (3 with softmax).
- Loss: Cross-entropy and optimization via minibatch gradient descent.
- With enough epochs and appropriate learning rate, network reliably classifies the three letter patterns despite noisy inputs.
