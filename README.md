# RuneGenerator
GAN to make custom characters/kanji/runes using the kuzushiji-mnist dataset found on kaggle

I wanted to prove a point to a friend, the point being that you could theoretically create your own runes for a magic system/fantasy setting by using a Generative Adversarial Network trained on an existing dataset of rune-like images. This led me to further my own knowledge of GANs.

Used in this project was the Kuzushiji-MNIST dataset of Japanese calligraphy found here on Kaggle: https://www.kaggle.com/c/kuzushiji-recognition/data

The first attempt used a GAN design found on a blog that worked well on the well known MNIST dataset. I believed that by using a design that performs well on a similar dataset I could get results with minimal effort. I was wrong and the problem became more interesting. This version of a GAN did not perform well even after 10000 epochs of training.

![alt text](https://github.com/Kyzarok/RuneGenerator/blob/main/GAN_generated_image%201000.png)

