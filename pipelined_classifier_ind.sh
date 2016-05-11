echo 'Generating a test matrix'
rm test_ind.matrix
rm test.feat
python3 test_ind.py
echo 'Predicting the sentiment classification'
python3 classifier_ind.py
