# HackX_Hackathon
### Theme: Entertainment
This is the Repository for the assignment of the HackX Hackathon by Scalar Academy

This code used os library for opening up a website in the default browser,
pandas for reading in the train, val and text files and
scikit-learn for TfidfVectorizer, LabelEncoder, LinearSVC and MultinomialNB

This code gets the mood of the user from his text and recommends him appropriate stuffs
improve his mood, incase if he is sad, or angry.

It compared the two most reliable algorithms for sentiment analysis: Linear SVM and naive bayes algo

It is seen that the LinearSVC performed much better then MultinomialNB, thus the rest of the code uses LinearSVC

Now it takes in input from the user and determines the mood, and accordingly recommends him videos, games, etc.
