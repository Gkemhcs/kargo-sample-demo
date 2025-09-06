from flask import Flask,jsonify 
import os 
app=Flask(__name__)
message=os.getenv("MESSAGE",default="welcome to kargo-demo")
port=int(os.getenv("PORT",default="8080"))

@app.route("/")
def home():
    return jsonify({
        "message":message,
        "description":"serving from version1🎉"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
