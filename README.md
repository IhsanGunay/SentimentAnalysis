# movie_classifier

  We decided to base our project on creating a sentiment classifier specifically geared toward determining the sentiment among movie reviews. In order to implement our algorithm, we used the IMDB corpus which consisted of two simple tags, which were positive and negative. 

  To create our features we made use of wordnet, more specifically sentiwordnet, and part of speech  taggers. In our algorithm we made use of two features. One of which is the Osgood semantic differentiation. Osgood believed in investigating the connotations of words themselves. He specifically looked at three different metrics which were evaluation, potency, and activity. We specifically were looking at evaluation. Osgood in particular investigated how closely related a word was to words 'good' and 'bad'. Therefore, we used the same metric in our own implementation. Treating each of the documents as bags of words, we used sentiwordnet to compile a list of words that we classified as subjective. With this, we were  able to create a set of subjective words which we used as a feature.
	
  Next, we looked at descriptive phrases. We thought it might be useful to find the users' feelings about the movie. We wanted to extract positive objective phrases in a document. We used the PMI-IR method in order to extract out these phrases. To extract the phrases, we defined our own grammar which lead to sentences that contained descriptive phrases only. Then we part of speech tagged the files and checked for sentences according to our own grammar. We used the presence of these descriptive phrases as features.

  In the end, we represented our dataset in a 5000x17173 matrix. We used this matrix to train a linear kernel support vector machine. To set the hyperparameter C,we grid searched loglinearly over 1e-3 to 1e3.  

  We tested the support vector machine classifier on 1000 randomly selected movie reviews from the test set. From our tests results, we received an accuracy of roughly 81%. We noticed that when we increased the training set from 5000 to 25000, the accuracy improved an additional 5%.

  To run this program, the run ./pipelined_classifier.sh
