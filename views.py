from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        jumlah = request.form.get('jumlah')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        elif len(jumlah) < 1:
            flash('Jumlah sedikit!', category='error')
        else:
            new_note = Note(data=note, jumlah=jumlah, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['id']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(id)
            db.session.commit()

    return jsonify({})