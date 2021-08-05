# RuneGenerator
GAN to make custom characters/kanji/runes using the kuzushiji-mnist dataset found on kaggle

I wanted to prove a point to a friend, the point being that you could theoretically create your own runes for a magic system/fantasy setting by using a Generative Adversarial Network trained on an existing dataset of rune-like images. This led me to further my own knowledge of GANs.

Used in this project was the Kuzushiji-MNIST dataset of Japanese calligraphy found here on Kaggle: https://www.kaggle.com/c/kuzushiji-recognition/data

The first attempt used a GAN design found on a blog that worked well on the well known MNIST dataset. This design was a simple design consisting of dense layers of basic neurons with a LeakyReLU activation. I believed that by using a design that performs well on a similar dataset I could get results with minimal effort. I was wrong and the problem became more interesting. This version of a GAN did not perform well even after 10000 epochs of training. Below is the result after 1000 epochs of training.
![alt text](https://github.com/Kyzarok/RuneGenerator/blob/main/GAN_generated_image%201000.png)

In trying to find an alterative architecture that would work, I looked into Deep Convolutional Generative Adversarial Networks, or DC-GANs. These are GANs that incorporate a convolutional layer, allowing them to extract much more relational data in data in a matrix format. Convolutional layers are probably best known for their use in image recognition in famous network designs such as Resnet. Applying this design resulted in significantly improved results.

![alt texto](https://github.com/Kyzarok/RuneGenerator/blob/main/GAN_generated_image%2010000.png)
