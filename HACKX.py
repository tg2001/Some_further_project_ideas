import pandas as pd
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

df1 = pd.read_csv(r'C:\Users\user\Downloads\train.txt', sep = ';', names = ['Text', 'Mood'])
print(df1.head())

cv = TfidfVectorizer(stop_words = 'english', min_df = 3, max_df = 300, ngram_range = (1,3))
X_train = cv.fit_transform(df1.iloc[:, 0])

le = LabelEncoder()
y_train = le.fit_transform(df1.iloc[:, 1])

df2 = pd.read_csv(r'C:\Users\user\Downloads\val.txt', sep = ';', names = ['Text', 'Mood'])
df3 = pd.read_csv(r'C:\Users\user\Downloads\test.txt', sep = ';', names = ['Text', 'Mood'])

X_val = cv.transform(df2.iloc[:, 0])
y_val = le.transform(df2.iloc[:, 1])

X_test = cv.transform(df3.iloc[:, 0])
y_test = le.transform(df3.iloc[:, 1])

nb = MultinomialNB()
nb.fit(X_train, y_train)

score_nb = nb.score(X_val, y_val)
print('\nValidation set accuracy using Naive Bayes: ', score_nb)

svc = LinearSVC(loss = 'hinge')
svc.fit(X_train, y_train)

score_svc = svc.score(X_val, y_val)
print('\nValidation set accuracy using SVC: ', score_svc)

score_svc_val = svc.score(X_train, y_train)
print('\nTraining set accuracy using SVC: ', score_svc_val*100)

score_svc_test = svc.score(X_test, y_test)
print('\nTest set accuracy using SVC: ', score_svc_test*100)

input_1 = [input("\nEnter the text: ")]
input_2 = cv.transform(input_1)

pred_1 = svc.decision_function(input_2)
pred_2 = svc.predict(input_2)
pred_3 = le.inverse_transform(pred_2)

print(pred_1)
print(le.classes_)
print("\nYour current mood is: ", pred_3)

if pred_3 == 'sadness' or pred_3 == 'anger':
	print("Would you like to: \n (1) watch some comedy \n (2) play games \n (3) watch movie \n (4) nothing? ")
	i = int(input())
	q = 1
	
elif pred_3 == 'joy' or pred_3 == 'love' or pred_3 == 'surprise':
	print("Would you like to: \n (1) watch some video \n (2) play games \n (3) watch movie \n (4) read book \n (5) Listen to music \n (6) nothing? ")
	i = int(input())
	q = 2
	
else:
	print("Would you like to: \n (1) watch some comedy \n (2) play games \n (3) nothing? ")
	i = int(input())
	q = 3

if i == 1:
	if q != 2:
		os.system("start \"\" https://www.youtube.com/results?search_query=stand+up+comedy")
	
	else:
		os.system("start \"\" https://www.youtube.com")

elif i == 2:
	os.system("start \"\" https://www.roundgames.com/")

elif i == 3:
	if q != 3:
		os.system("start \"\" https://www.netflix.com/in/")

elif i == 4:
	if q == 2:
		os.system("start \"\" https://openlibrary.org/")

elif i == 5:
	if q == 2:
		os.system("start \"\" https://www.spotify.com/us/")
