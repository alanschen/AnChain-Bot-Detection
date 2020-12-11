# AnChain Bot Detection: 
# UC Berkeley Data X Fall 2020 Final Project

In this project, we created machine learning models deciding whether or not certain EOS accounts registered on `EndlessGame dapp` is a bot, or a human. 

We want to thank our mentor **Victor Fang** and partnering company AnChain.ai for providing us with huge amount of support, and discussing progress each week with us for this project.

For data privacy reasons, not all files will be avaliable in this repo. Only data generated from public information will be avaliable.

## Blockchain Dataset
  - We were provided 1 month of smart contract output data, scrapped from web, containing around 5 million transaction in total.
  - We made the data set avaliable in Google Drive so we could work in `Google Colab`, capitalizing on memory and productivity.
  - Note: Parts of the data pipeline is not show in this repo, since we added external and often private information during feature extraction.
 
## Solution Description & Architecture
The first obstacle we tackled was developing intuition about how bots behave in general, and how to quickly visualize information such as activity and transaction data. So after constructing a basic data pipeline, we used a combination of clustering and visualization techniques and determined that in addition to automatic filtering and acquiring labels from external data set (i.e from previous literature on this problem), we need to label some of the ambiguous data ourselves though majority or unanimous vote.

The second obstacle we tackled was labelling 40% of our training and testing data manually using human intuition. Though a productivity tool we build and crowdsourcing, we generated enough labels to diverify our dataset, and was able to successfully solve the biased dataset issue we saw later. This was an iterative process where labelling & training happened in the same time.

The last obstacle we tackled was dealing with an extremely biased data. Since around 90% of our final labelled set were bots, we had to balance the data set before fitting machine learning models. Here, we balanced the training set with 30% humans, and 70% bots generated using bootstrapping from our EDA and clustering heuristics in the beginning of our project.

## Data Labelling
  - See notebook `labeler.ipynb` and `combine-labels.ipynb`.
  - The first file `labeler.ipynb` contains our IPython widget based labelling productivity tool. It is used to display activity heat-map and statistics from our data-set for a particular user, record our votes and write them to an existing csv. 
  - The second file `combine-labels.ipynb` combines our three sources of labels. Majority vote set, research labelled set, and automatically filtered set.
## Clustering & EDA
  - See notebook `clustering.ipynb`. We used the elbow method to determine the best distribution for training data balancing and upsampling.
## Baseline ML Model & Features
  - See notebook `model.ipynb`. This contains both code for engineered features & ML models.
