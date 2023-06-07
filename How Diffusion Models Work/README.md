# [How Diffusion Models Work](https://learn.deeplearning.ai/diffusion-models/lesson/1/introduction)

## Intuition
- Goal: From a fixed dataset of images and you want to generate new images that look like the others
- Process:
- - 1. add gradually harsher noise layers on top of your images
- - 2. train a NN to 'extract' the noise layer
- - 3. remove the noise layer from the initial noisy image
- - 4. add a new noise layer in order to keep the NN inputs as expected (Guassian noise)*
- - - * If we don't add the extra noise layer after removing the initial noise, the process will yield a 'blob' that is kind of an average of the elements in the training data
- - 5. repeat until results are good enough



