"""
input: string of question
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer
import scipy.spatial
import string
from .models import Query

class nlp_module:
    """
    nlp_module class for handling NLP tasks.

    It takes in questions from the database using the getData, 
    computes feature vector representation of the questions.
    Then whenever user text is passed, the best matching questions from above are returned.

    Attributes
        remove_punct_dict (dict) : Constains puncuations to be removed from any input text
        embedder(SentenceTransformer) : Pretrained BERT Model to convert input text to feature vectors
        questions(list) : Contains the list of questions obtained from the database
        corpus(list) : Contains the list of questions in lower case, without punctuations
        corpus_embeddings(list(numpy.ndarray)) : list of feature vectors of questions
    """
    
    def __init__(self):
        """
        Constructor for nlp_module class.
       ` __init__` function calls the `getData` function to get the list of questions from database.
        Then the questions are converted to lowercase and their punctuations are removed.
        Then feature vectors of these questions are computed.
        """
        self.remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        self.embedder = SentenceTransformer('bert-base-nli-mean-tokens') 
    
        # Corpus with example sentences

        self.questions = self.getData()  #change this for input
        self.corpus = self.questions.lower().translate(self.remove_punct_dict).splitlines()
        self.questions=self.questions.splitlines()
        self.corpus_embeddings = self.embedder.encode(self.corpus)

    #import data
    def getData(self):
        """
        `getData` function obtains the list of questions from the database.
        The questions are returned as a single string where the individual questions are separated
        by a `\n` character.

        Returns:
            data : single string containing all the questions
        """
        data = ""
        queries_all = Query.objects.all()
        for q in queries_all:
            data += "\n" + q.intent
        data = data[1:]
        return data

    def respond(self, query):
        """
        `respond` function takes the user query, computes its feature vector and
        compares with the feature vectors of predefined questions.

        Args:
            query(string) : The user query

        Returns:
            question(string) : The question that best matches with the user query
        """
        query.lower().translate(self.remove_punct_dict)
        query_embedding=self.embedder.encode([query])[0]
        distances = scipy.spatial.distance.cdist([query_embedding], self.corpus_embeddings, "cosine")[0]
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])
        
        max_score=1-results[0][1]
        if max_score>0.75:
            return self.questions[results[0][0]]
        else:
            return -1
