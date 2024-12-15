from flask import Flask, render_template, request
import subprocess
import threading

app = Flask(__name__)

# Function to run the car game script
def run_car_game():
    subprocess.run(["python", "car_game.py"])

# Function to run the light control script
def run_light_control():
    subprocess.run(["python", "light_control.py"])

# Function to run the automated message script
def run_automated_msg():
    subprocess.run(["python", "automated_msg.py"])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run_car_game', methods=['POST'])
def car_game():
    threading.Thread(target=run_car_game).start()  # Run in a new thread
    return render_template("car_game.html")

@app.route('/run_light_control', methods=['POST'])
def light_control():
    threading.Thread(target=run_light_control).start()  # Run in a new thread
    return render_template("light_control.html")

@app.route('/run_automated_msg', methods=['POST'])
def automated_msg():
    threading.Thread(target=run_automated_msg).start()  # Run in a new thread
    return render_template("automated_msg.html")

if __name__ == "__main__":
    app.run(debug=True)
