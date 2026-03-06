# social-momentum-nlp-research

An educational, read-only Python data ingestion pipeline for analyzing aggregate social sentiment using NLP models like FinBERT

# Public Sentiment NLP Analyzer (Educational Research)

## Overview
This repository contains the data ingestion pipeline for an educational machine learning project focused on Natural Language Processing (NLP). The core objective is to sample localized public sentiment from financial subreddits and process the text using NLP models (such as FinBERT and Anthropic Claude) to study the correlation between aggregate social momentum and broader market volatility. 

This project is strictly for **personal data science research** and non-commercial academic development.

## Architecture & Data Flow
This script acts as the primary "read-only" data ingestion layer:
1. **Fetch:** Utilizes the Python Reddit API Wrapper (PRAW) to stream text from public financial communities.
2. **Sanitize:** Strips URLs, markdown formatting, and non-text elements to prepare clean strings.
3. **Analyze:** Passes the sanitized text batches to an external NLP model to generate an aggregate "Bullish" vs. "Bearish" sentiment score.
4. **Log:** Stores the anonymized aggregate scores in a local SQLite database for historical backtesting and correlation research.

## Compliance & API Ethics
This application is built with strict adherence to Reddit's Responsible Builder Policy:
* **Read-Only Access:** The application requires only `read` permissions. It does not (and cannot) post, comment, upvote, or interact with users in any way.
* **Rate Limit Adherence:** The ingestion loop is hard-coded to respect Reddit's standard API limits (maximum 100 requests per minute) and utilizes PRAW's built-in rate-limit handling to prevent server strain.
* **No PII Storage:** The system does not store usernames, user IDs, or any Personally Identifiable Information (PII). Only the sanitized body text of the posts is temporarily held in memory for NLP scoring before being discarded.
* **Non-Commercial:** This is an isolated, local sandbox project. No data is sold, redistributed, or monetized.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/social-momentum-nlp-research.git](https://github.com/yourusername/social-momentum-nlp-research.git)
