# Auto-Reg Token Sampling.

Created: 2023-07-22 15:25:15
Last Updated: 2023-07-22 15:32:54

### User - 2023-07-22 15:25:15

What does it mean to say "we sample tokens in an auto-regressive manner" from a distribution?

### Assistant - 2023-07-22 15:25:41

In machine learning and natural language processing, a distribution typically refers to the probability distribution of potential outcomes. When we say "we sample tokens in an auto-regressive manner from a distribution", it implies that we are generating sequences of tokens (or words) in a way that each new token depends on the previously generated tokens.

The term "auto-regressive" comes from statistics and is used to describe a type of model where the value of a variable at a given point in time is a function of its previous values. So in the context of language models like GPT (Generative Pre-trained Transformer), each token is predicted one at a time, with each prediction using the previously generated tokens as context.

Here's a simple example. If the task is to generate a sentence and the model has so far generated "The cat is on the", the next token it generates (in this case, most likely "roof" or "ground" or "mat") is sampled from a probability distribution that heavily depends on the previously generated tokens ("The cat is on the").

This auto-regressive property allows these models to generate coherent and contextually relevant sequences of text. Each generated token influences the distribution for the next, hence giving us a distribution that changes as we generate more tokens. This is the essence of "sampling tokens in an auto-regressive manner from a distribution".

### User - 2023-07-22 15:32:54

What are EM and BLEU metrics?

### Assistant - 2023-07-22 15:33:10

EM and BLEU are metrics used in natural language processing (NLP) to evaluate the performance of machine learning models, especially in tasks like machine translation and question answering.

1. **EM (Exact Match):** This is a simple and strict evaluation metric. As the name suggests, it checks if the predicted answer is exactly the same as the ground truth (the correct answer). It's often used in question answering systems where the answer is a short piece of text. If the model's answer and the ground truth are exactly the same, EM is 1; otherwise, it is 0. This means that even minor differences, like an extra space or a missing punctuation mark, can lead to an EM score of 0. 

2. **BLEU (Bilingual Evaluation Understudy):** This metric is often used in machine translation tasks. Instead of requiring an exact match, BLEU considers the overlap of n-grams between the machine-generated output and the reference (correct) output. N-grams are contiguous sequences of n items in the text. For example, in the sentence "I have a cat", the 1-grams (unigrams) are "I", "have", "a", "cat"; the 2-grams (bigrams) are "I have", "have a", "a cat". The more and longer the n-grams match between the generated output and the reference, the higher the BLEU score. The BLEU score is between 0 and 1, with 1 being the best possible score. However, BLEU has its limitations: it does not account for semantic meaning, and it may not perform well with sentences that have the same meaning but different word orders.

Both EM and BLEU scores are useful tools to assess the performance of NLP models, but they do not cover all aspects of language understanding and should be used in combination with other evaluation methods.

