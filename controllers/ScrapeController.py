from flask import Blueprint

# controller for all scraping methods

sc = Blueprint("scrapeController", __name__)

@sc.route('/test', methods=['GET'])
def get():
    return {
        "message": "get: test from scrape controller"
    }