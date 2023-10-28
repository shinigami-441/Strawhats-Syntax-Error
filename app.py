from flask import Flask, request, jsonify
import json
from pandasai import SmartDataframe
import pandas as pd
from pandasai.llm.google_palm import GooglePalm
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST', 'GET'])
def handler():
    try:
        print('received event:')
        json_data = request.get_json()
        length = len(json_data)

        userprompt = json_data[length - 1]["userprompt"]
        json_data.pop()
        df = pd.DataFrame(json_data)

        llm = GooglePalm(api_key="AIzaSyBXEWdQPGgaWIzTwhns0vFZLiBrtZ6lCUs")  # Replace "YOUR_API_KEY" with your actual API key
        columns_to_keep = ["title", "stars", "price", "description", "url", "reviewsCount", "thumbnailImage"]

        df2 = df[columns_to_keep]
        df3 = df2['price'].apply(pd.Series)
        df4 = pd.concat([df2, df3], axis=1)
        columns_to_keep = ["title", "stars", "value", "description", "thumbnailImage", "url", "reviewsCount"]
        df5 = df4[columns_to_keep]

        numeric_columns = ["stars", "value", "reviewsCount"]
        df5[numeric_columns] = df5[numeric_columns].fillna(0)

        # Replace NaN strings with "nothing"
        string_columns = df5.columns.difference(numeric_columns)
        df5[string_columns] = df5[string_columns].fillna("nothing")

        sdf = SmartDataframe(df5, config={"llm": llm})
        result = sdf.chat(f"Recommend me exactly 5 best products based on the query: {userprompt}. Please report only titles, value, stars, thumbnailImage, url, reviewsCount of products. Report the DataFrame and consider price, reviews and description.")
        answer = result.to_dict('record')
        response = {
            'body': json.dumps(answer)
        }
    except Exception as e:
        response = {
            'body': json.dumps(f'Error: {str(e)}')
        }
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
