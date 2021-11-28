from flask import Flask, render_template, jsonify
from google.cloud import bigquery
import sys


# Create the app and bootstrap instances
app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
@app.route("/welcome")
def index():
    # Instantiate a query client
    query_client = bigquery.Client()
    # Define the query
    query_definition = """
        SELECT 
        name,
        reviews_rating AS Rating,
        reviews_title AS Title,
        reviews_text AS Review,
        reviews_sourceurls AS URL
        FROM `msds434-w9-dev.product_reviews_5000.raw5000` 
        WHERE (reviews_rating = 1 OR reviews_rating = 2)
        LIMIT 10;
    """
    # Ask for a query job
    df = query_client.query(query_definition).to_dataframe(create_bqstorage_client=True)
    column_names = df.columns.values
    row_data = list(df.values.tolist())
    print(row_data[1], file=sys.stdout)
    product_name = row_data[0][0]
    # print(row_data[0][0], file=sys.stdout)
    return render_template(
        "index.html",
        product_name=product_name,
        column_names=column_names,
        row_data=row_data,
        zip=zip,
    )


@app.route("/unrated")
def unrated():

    return render_template("done.html")


# Start server and run app on host/port: python -m flask run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
