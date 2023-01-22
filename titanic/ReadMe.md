# Titanic Analysis





Contents
1. Understanding the data
2. Imputing missing values



<img src="./img/titanic_stablediff.jpeg" alt="a black and white photo of a steamliner ship">


Building pipelines (https://scikit-learn.org/stable/modules/compose.html)

## Background

The titanic dataset is one of the most widely used sources for data science bootcamps, courses and competitions. There are good reasons for this; the data is freely available, the context is widely understood and the goal (to predict if a passenger survived based on their age, gender etc.) is intuitive. There are some limitations that we shall discuss at the end of the book, but the influence of the dataset is almost unparalleled, with more than 14,000 teams contributing solutions on [Kaggle](https://www.kaggle.com/competitions/titanic) and numerous blog posts, summary articles and youtube videos across the internet.

When reading articles on how to analyse the titanic dataset, I discovered that many were illuminating and picked up on subtle ideas related to missing data (Chapter 2) and over-parameterization (Chapter 3). However, in other cases, I found myself disagreeing with assumptions or interpretation. This is not unsuprising as any data science project involves some subjective decisions. 

At the end of chapters 1-3, we will save a modified version of the training and test data after initial feature engineering (Chapter 1), imputation of missing data (Chapter 2) and advanced feature engineering (Chapter 3). Each modified dataset will allow us to begin the next chapter without repeating the previous steps.

In Chapters 4 onwards, we will produce predictions for testing on Kaggle. 




### Dummy response

The Kaggle competition sets a pretty high baseline by just using passenger's gender to predict survival (performance ~ 74%???). This model predicts that women surive and men perished in the disaster. To improve on the performance, we should start by asking
- why did some men survive?
- why did some women not survive?
Following these threads will help us begin to unravel the story, produce new leads and new questions that build a more complex picture of a dataset with meaning, but also gaps. Our role as data scientists is to recognise that meaning and develop the intuition to accurately bridge those gaps, ultimately leading to our ability to predict the surival outcomes for nearly all passengers (hopefully!)


