# Hybrid Recommendation Explanation Model Based on LOD and KG Embeddings

This repository contains the source code of the following research work:

* A hybrid model leveraging linked open data and knowledge graph embeddings for recommendation explanations

The research address the problem of recommendation explanations leveraging knowledge graphs. Motivated by previous works ([Musto et al., 2016](https://dl.acm.org/doi/10.1145/2959100.2959173) and [Musto et al., 2019](https://www.sciencedirect.com/science/article/abs/pii/S1071581918300946)) on this topic, the aim of the research work is to alleviate the shortcomings of the existing approaches, in terms of the explicability precision and the questionable algorithm-independence.

### Considered recommendation algorithms

* LOD-CBRS (Content-Based Recommender system based on Linked Open Data), in which relevance predictions of unrated items are based on their semantic similarities with users' liked items.
* SVD (the collaborative filtering model based Single Value Decomposition), in which relevance predictions of unrated items are based on the learnt user and item factors in the latent space.
* HybridRS (Hybrid recommendation system), which combines predictions of the LOD-CBRS and SVD approaches.

### Code organization

This repository is organized in several subfolders.

#### Dataset

The experiments of the research work are based on a real-world movie rating dataset: the [MovieTweetings](https://github.com/sidooms/MovieTweetings) dataset, which is a dataset consisting of ratings on movies that were contained in well-structured tweets on Twitter. The dataset is updated regularly. The ratings used for our research work were collected on 13/07/2020, from the dataset's website. For more details about the dataset, you may refer to [this link](https://github.com/sidooms/MovieTweetings).


#### Eval_Samples

For the evaluation part, we chose 1,000 random users from the dataset. For each user, we chose randomly 5 of the user's liked items to construct the user input data. This folder contains the corresponding user input data for evaluation.


#### Explanation_Models

This folder contains the implementations of the compared methods.

#### Recommendation_approaches

This folder contains the pre-computed recommendation algorithms, which are then used by the explanation models during the recommendation explanation phase.

### Prerequisites to run the code

Python 3.6 (or later) is needed to run the scripts.

#### Installation of packages
In addition, the following Python packages are also needed:

* The [Surprise](http://surpriselib.com/) package which is a Python scikit for building and analyzing recommender systems.
  * With pip
  ```python
  pip install numpy
  pip install scikit-surprise
  ```

  * With conda
  ```python
  conda install -c conda-forge scikit-surprise
  ```
* The [SPARQLWrapper](https://github.com/RDFLib/sparqlwrapper), a simple Python wrapper around a SPARQL service to remotely execute SPARQL queries.
  * From PyPi
  ```python
  pip install sparqlwrapper
  ```

  * From GitHub
  ```python
  pip install git+https://github.com/rdflib/sparqlwrapper#egg=sparqlwrapper
    ```

Moreover, classic machine learning libraries are also needed, such as pandas, numpy and scipy.

### Run evaluations

To run the exprimentations, do   
```Python
  python 'evaluation.py'
  ```

This script will:
* Load the test data (users for test)
* Generate recommendations with different recommenders systems
* Build different explanation models
* Drawing explanations
* Writing results to files


### A Running Example

To run the code with an example, do   
```Python
  python 'running_example.py'
  ```
  Specifically, to run the example, you can define:
  * the input_dict, which is the user input (profile), keys are item IDs (see 'movies.csv' in the Dataset folder), values are ratings (of a 1 to 10 scale)
  * the recommender system used (recommender), which has to be one of the followings ('cbf', 'svd', 'hybrid')
  * the explanation pattern used for the ExpLOD model (pattern), which has to be one of the two options ('basic', 'broader'), and
  * the number of recommended items (nb_recs)

See the 'running_example.py' for details.
