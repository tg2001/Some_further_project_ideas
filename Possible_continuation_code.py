import os

# Assume that the model of Sentiment Analysis is already trained and is now further extended using the following code.

input_1 = [input("\nEnter the text: ")]
input_2 = cv.transform(input_1)			# cv being the Tfidf Vectorizer used in the project

pred_1 = svc.decision_function(input_2)		# svc being the model used to fitthe dataset
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
