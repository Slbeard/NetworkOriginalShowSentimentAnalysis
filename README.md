# **TV Show Sentiment Analysis using TMDB and Reddit**

## **Project Overview**  
This project gathers TV show data, including network details, and performs sentiment analysis on social media discussions from Reddit. By integrating The Movie Database (TMDB) API and Reddit's social data, we analyze public opinion on popular TV shows across different networks.

## **Process Workflow**  

### **Step 1: Identifying Network IDs via TMDB API**  
- Searching for a network directly in TMDB often returns multiple IDs, making it difficult to pinpoint a single identifier.  
- Instead, a well-known TV show from each network was used to retrieve detailed show information via the `/tv/{id}` endpoint.  
- The correct **network ID** was extracted from the show's metadata.  

### **Step 2: Discovering Top Shows from Each Network**  
- Using the obtained **network ID**, we queried the `/discover/tv` endpoint to retrieve a list of the top TV shows associated with that network.  
- The **top 10 shows per network** were collected for further analysis.  

### **Step 3: Retrieving Show Metadata**  
- For each identified TV show, detailed metadata was extracted, including title, popularity, and network affiliation, ensuring a complete dataset for sentiment analysis.  

### **Step 4: Collecting Sentiment Data from Reddit**  
- For each of the **top 10 TV shows per network**, Reddit was searched for mentions and discussions.  
- Relevant posts and comments were collected to analyze public sentiment.  

### **Step 5: Sentiment Analysis**  
- A sentiment analysis tool was used to classify Reddit posts into **positive, negative, and neutral** categories.  
- Both the **average and median sentiment scores** were computed for each TV show.  

## **Technologies & APIs Used**  
- **Programming Language:** Python  
- **APIs:**  
  - [TMDB API](https://www.themoviedb.org/documentation/api) – To fetch TV show and network details.  
  - [Reddit API (PRAW or Pushshift)](https://www.reddit.com/dev/api/) – To extract social media discussions.  
- **Libraries:**  
  - `requests` – To interact with APIs.  
  - `pandas` – For data processing and analysis.  
  - `NLTK` or `VADER` – For sentiment analysis.  

## **Expected Outcomes**  
- A structured dataset containing TV shows categorized by network.  
- Insights into audience sentiment for each top show across various networks.  
- A comparative analysis of networks based on public reception.  

## **Future Enhancements**  
- Expand data sources to include **Twitter/X and YouTube comments** for a broader sentiment analysis.  
- Implement **real-time tracking** of sentiment trends over time.  
- Develop a **dashboard using Tableau or Streamlit** for interactive data visualization.  
