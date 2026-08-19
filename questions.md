# Interview questions

## Resources
[andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions)
[Deep Learning Interviews](https://arxiv.org/pdf/2201.00650)
[ML Interview Book](https://huyenchip.com/ml-interviews-book)

## General

Source: [andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions)

1. What's the trade-off between bias and variance?
2. What is gradient descent?
3. Explain over- and under-fitting and how to combat them?
4. How do you combat the curse of dimensionality?
5. What is regularization, why do we use it, and give some examples of common methods?
6. What is vanishing gradient?
7. What are dropouts?
8. What's the difference between a generative and discriminative model?
9. Instance-Based Versus Model-Based Learning.
10. What is the difference between LDA and PCA for dimensionality reduction?
11. What is the difference between t-SNE and UMAP for dimensionality reduction?
12. How Random Number Generator Works, e.g. rand() function in python works?
13. Given that we want to evaluate the performance of 'n' different machine learning models on the same data, why would the following splitting mechanism be incorrect:
14. What is the basic difference between LSTM and Transformers?
15. What are RCNNs?

## Logistic Regression

Source: [Deep Learning Interviews](https://arxiv.org/pdf/2201.00650)

1. (Logistic Regression) True or False: For a fixed number of observations in a data set, introducing more variables normally generates a model that has a better fit to the data. What may be the drawback of such a model-fitting strategy?
2. (Logistic Regression) Define the term "odds of success" both qualitatively and formally. Give a numerical example that stresses the relation between probability and odds of an event occurring.
3. (Logistic Regression) Define what is meant by the term "interaction", in the context of a logistic regression predictor variable.
4. (Logistic Regression) What is the simplest form of an interaction? Write its formulae.
5. (Logistic Regression) What statistical tests can be used to attest the significance of an interaction term?
6. (Logistic Regression) True or False: In machine learning terminology, unsupervised learning refers to the mapping of input covariates to a target response variable that is attempted at being predicted when the labels are known.
7. (Logistic Regression) Complete the following sentence: In the case of logistic regression, the response variable is the log of the odds of being classified in [...].
8. (Logistic Regression) Describe how in a logistic regression model, a transformation to the response variable is applied to yield a probability distribution. Why is it considered a more informative representation of the response?
9. (Logistic Regression) Complete the following sentence: Minimizing the negative log likelihood also means maximizing the [...] of selecting the [...] class.

## ML / deep-learning fundamentals
1. Training loss decreases, validation loss increases after epoch 12, while validation accuracy stays flat. What is happening and what would you try?
2. Why can validation loss increase while validation accuracy remains constant?
3. You have a binary classifier with 1% positives and 99% negatives and it achieves 99% accuracy. Why is accuracy almost useless?
4. Which metrics would you use for that heavily imbalanced classifier?
5. A classifier has 95% recall but 20% precision. What does that tell you?
6. How could you change that classifier's operating point without retraining?
7. Adam vs SGD: when might SGD generalize better?
8. What happens when the learning rate is too high?
9. What happens when the learning rate is too low?
10. Why can mixed-precision training become unstable?
11. How would you detect data leakage?
12. Your positive class is only 0.1%. How would you train and evaluate the model?
13. What is overfitting vs underfitting?
14. What regularization methods would you consider?
15. How do CNNs work?
16. What is the relationship/difference between covariance and independence?

## Testing / software engineering / CI
1. You inherit a research repo full of notebooks, globals, hard-coded paths, and duplicated preprocessing. How would you make it usable by five researchers without slowing experimentation?
2. What would you deliberately not productionize yet?
3. How would you design a Python repository for researchers that may eventually become production software?
4. You add CI to that repository. What checks belong on every pull request?
5. Which checks should not run on every PR, and why?
6. What are examples of checks better suited to release/main/nightly pipelines?
7. What is the difference between a unit test, integration test, and smoke test? Give an ML example of each.
8. When would you use a mock in a unit test?
9. What can go wrong if you mock too much?
10. Why not mock everything?
11. A researcher sets torch.manual_seed(42) but training remains non-reproducible. Why?
12. How would you make an ML experiment as reproducible as reasonably possible?
13. Why can deterministic algorithms make training slower?
14. Why copy dependency files into a Docker image before copying source code?
15. Why pin dependencies?
16. Why use a virtual environment?
17. Why separate development dependencies?
18. What does a lockfile buy you?
19. What problems arise when a research environment isn't reproducible?
20. What is the difference between CI artifacts and caches?
