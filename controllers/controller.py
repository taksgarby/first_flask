from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return "Welcome to our Donut Shop!"

@app.route('/orders')
def orders_index():
    return render_template('index.html', title = 'Home', orders = orders)

@app.route('/orders/<index>')
def show_order(index):
    chosen_order = orders[int(index)]
    return render_template('order.html', order=chosen_order)

