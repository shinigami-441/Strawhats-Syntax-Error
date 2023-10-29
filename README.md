# StrawHats: Amazon Chatbot
## Submission Link
[https://www.youtube.com/watch?v=4pmDuu2rqbI&ab_channel=AnuragWadhwa](https://www.youtube.com/watch?v=WhX1xFs3n4U)
## Basic Idea

Our solution enhances user shopping experiences and satisfaction by allowing natural language prompts for product discovery. The chatbot features product recommendations based on user preferences and image-to-product searches. Users can ask for recommendations like "I want a laptop under 40,000 Rupees with at least 8GB RAM and 1TB storage," and the chatbot provides real-time Amazon product suggestions. Additionally, users can input images to receive related product recommendations. All suggestions are based on real-time Amazon data obtained through Apify's API service (will be replaced by Amazon API in the future).

## How to Use

**Note:** For real-time data, we use Apify Amazon API, which involves web scraping of public data, making chatbot searches take approximately 2 minutes. Please be patient.
Steps to be followed:
1. Open terminal in the directory which contains the Strawhats App (App.py file specifically).
2.  Run the command "python3 App.py"
3.  A link will be displayed, please copy it. (Example- Running on **http://127.0.0.1.5000**. Copy the bold part)
4.  Open a new terminal tab and run the command  "ngrok http (copy above link here)" and press enter. This will make the system as the endpoint for the app.
5.  Infront of the "Forwarding" session status beneath "Web Interface", there exists a link (Example- **https://fa32-103-37-201-178.ngrok-free.app** -> http://127.0.0.1:5000). Copy the bold text url.
6.  Now open the chatbot.html and find NGROK_URL. Paste this url there and save.
7.  Now Open Index.html and login into account. If you want to go to chatbot open the code of chatbot.html and open live server in vscode. Then you can ask by text or give image input

## Flow of Execution
1. User input is received, calling the `chat_api_dev` Lambda function which uses OpenAI API to parse user requests.

2. Parsed input is passed to the Apify Amazon API, providing results for around 100 products matching the user's query from the current Amazon.com website.

3. Advanced data analysis is performed using generative AI leveraging PandasAi with GooglePalm LLM as the backend. The PandasAi creates embeddings for user requests and product data, storing them in the vector database. It finds the best products using a similarity function like cosine similarity and provides recommendations.

4. Recommended products are sent to the frontend for user viewing. A DynamoDB table is maintained where the primary key is the user ID, and the sort key is the timestamp. This table stores input and output results used for infinite scroll on the frontend.

## Backend: AWS Solutioning

- AWS Amplify is used for creating Lambda functions and a database using DynamoDB.
- Lambda functions handle input parsing, image-to-product conversion, storing, and retrieving data from the database, and obtaining product data from the Apify API.

## Frontend: JavaScript and React

**Generative AI Stack Used:**

- Llava model – Image to product search (by using Replicate API)
- OpenAI Gpt-3.5 Turbo – For parsing user input
- PandasAi and GooglePalm LLM – For analyzing and filtering based on user preferences
- Apify API – For product data

## Future Scope

- **Optimization on Current Techniques:** The current data retrieval from the API uses web scraping, which can be avoided if an API from Amazon for product data is available.

- **Additional Features:**
  - Training based on user chat to continuously improve.
  - Caching for faster access and reduced load.
  - Virtual Try-On for clothes and accessories.
  - Monthly Grocery recommendations.

## Costs Incurred

- OpenAI API - $6
- Replicate (Llava model) - $5
- AWS – $0.25 (For EFS read and write)

