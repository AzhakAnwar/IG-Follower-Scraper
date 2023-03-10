# Instagram Followers Matrix Generator / Instagram Followers Analysis
## Disclaimer
This is an educational project and should not be used for any malicious or unauthorized purposes.

## Overview
This project is designed to create a matrix of followers of a given Instagram user. The matrix will show whether two users are following each other or not. The project is divided into two phases:

## Phase 1: Web Scraping / Collecting Instagram Followers
1. User logs in to their Instagram account.
2. The script fetches all the followers of the logged-in user.
3. The script then fetches all the followers of the followers from step 2.
4. The data is stored in a JSON file.

## Phase 2: Data Processing / Generating Followers Matrix
1. The script reads the JSON file from phase 1.
2. A matrix is created where each row represents a user, and each column represents a follower.
3. If two users are following each other, the corresponding cell in the matrix will be 1. Otherwise, it will be 0.
4. The matrix is then exported as a CSV file.


The goal of this project is to analyze the followers of an Instagram account in order to understand the reach and influence of the account. The data collected in this project can be used for various purposes such as analyzing audience demographics, understanding the spread of information, and identifying key influencers.

Please note that the project uses Python programming language and makes use of the json and csv libraries. Also it uses Instagram Private API package.

Please use the code at your own risk and make sure to comply with Instagram's terms of service.



