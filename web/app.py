from flask import Flask, render_template, request, redirect
import expense_tracker

app = Flask(__name__)

@app.route('/')
def index():
    expenses = expense_tracker.view_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    description = request.form['description']
    expense_tracker.add_expense(float(amount), category, date, description)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
