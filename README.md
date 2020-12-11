# AnChain Bot Detection: 
# UC Berkeley Data X Fall 2020 Final Project

In this project, we created machine learning models deciding whether or not certain EOS accounts registered on `EndlessGame dapp` is a bot, or a human. 

We want to thank our mentor **Victor Fang** and partnering company AnChain.ai for providing us with huge amount of support, and discussing progress each week with us for this project.

For data privacy reasons, not all files will be avaliable in this repo. Only data generated from public information will be avaliable.

# Blockchain Dataset
  - We were provided 1 month of smart contract output data, scrapped from web, containing around 5 million transaction in total.
  - We made the data set avaliable in Google Drive so we could work in `Google Colab`, capitalizing on memory and productivity.
  - Note: Parts of the data pipeline is not show in this repo, since we added external and often private information during feature extraction.
# Data Labelling
  - See notebook `labeler.ipynb` and `combine-labels.ipynb`.
  - The first file `labeler.ipynb` contains our IPython widget based labelling productivity tool. It is used to display activity heat-map and statistics from our data-set for a particular user, record our votes and write them to an existing csv. 
  - The second file `combine-labels.ipynb` combines our three sources of labels. Majority vote set, research labelled set, and automatically filtered set.
# Clustering & EDA
  - See notebook `clustering.ipynb`. We used the elbow method to determine the best distribution for training data balancing and upsampling.
# Baseline ML Model & Features
  - See notebook `model.ipynb`. This contains both code for engineered features & ML models.
