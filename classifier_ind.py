from pickle import load, dump

with open('test_ind.matrix', 'rb') as f:
    problem_features = load(f)

with open('classifier.svm', 'rb') as f:
    classifier = load(f)

predicted_label = classifier.predict(problem_features)

print(predicted_label)
