from flask import Flask, render_template, request, redirect, url_for
from peewee import *
from datetime import datetime

app = Flask(__name__)

# Single SQLite database file
db = SqliteDatabase('tickets.db')

# Single Ticket table as required by the project guide
class Ticket(Model):
    name = CharField(max_length=100)
    email = CharField(max_length=120)
    subject = CharField(max_length=150)
    description = TextField()
    status = CharField(default='Open')  # Open, In Progress, Resolved
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db

# Create the table automatically on startup
with db:
    db.create_tables([Ticket])

# 1. Short page explaining the support service
@app.route('/')
def index():
    total_tickets = Ticket.select().count()
    open_tickets = Ticket.select().where(Ticket.status != 'Resolved').count()
    return render_template('index.html', total=total_tickets, open_count=open_tickets)

# 2. Page listing submitted tickets
@app.route('/tickets')
def list_tickets():
    tickets = Ticket.select().order_by(Ticket.created_at.desc())
    return render_template('tickets.html', tickets=tickets)

# 3. Form to create a ticket
@app.route('/tickets/new', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        Ticket.create(
            name=request.form['name'].strip(),
            email=request.form['email'].strip(),
            subject=request.form['subject'].strip(),
            description=request.form['description'].strip(),
            status='Open'
        )
        return redirect(url_for('list_tickets'))
    return render_template('create.html')

# 4. Detail page for each ticket
@app.route('/tickets/<int:ticket_id>')
def ticket_detail(ticket_id):
    ticket = Ticket.get_or_none(Ticket.id == ticket_id)
    if not ticket:
        return "Ticket not found", 404
    return render_template('detail.html', ticket=ticket)

# 5. Form to edit an existing ticket (including status)
@app.route('/tickets/<int:ticket_id>/edit', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    ticket = Ticket.get_or_none(Ticket.id == ticket_id)
    if not ticket:
        return "Ticket not found", 404

    if request.method == 'POST':
        ticket.name = request.form['name'].strip()
        ticket.email = request.form['email'].strip()
        ticket.subject = request.form['subject'].strip()
        ticket.description = request.form['description'].strip()
        ticket.status = request.form['status']
        ticket.save()
        return redirect(url_for('ticket_detail', ticket_id=ticket.id))

    return render_template('edit.html', ticket=ticket)

if __name__ == '__main__':
    app.run(debug=True)