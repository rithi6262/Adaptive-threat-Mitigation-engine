from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from app import db
from models import User, Log
from app import blockchain

admin_bp = Blueprint('admin', __name__)

# Static admin credentials
def is_admin_authenticated():
    return session.get('admin_authenticated', False)

@admin_bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if is_admin_authenticated():
        return redirect(url_for('admin.admin_dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['admin_authenticated'] = True
            return redirect(url_for('admin.admin_dashboard'))
        else:
            flash('Invalid admin credentials', 'danger')
    return render_template('admin_login.html', title='Admin Login')

@admin_bp.route('/admin/logout')
def admin_logout():
    session.pop('admin_authenticated', None)
    flash('Logged out from admin panel', 'info')
    return redirect(url_for('admin.admin_login'))

@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    if not is_admin_authenticated():
        return redirect(url_for('admin.admin_login'))
    users = User.query.all()
    # Try to import Prediction model and query predictions
    try:
        from models import Prediction
        predictions = Prediction.query.order_by(Prediction.timestamp.desc()).all()
    except Exception:
        predictions = []
    ledger = blockchain.get_chain()
    return render_template('admin_dashboard.html', users=users, predictions=predictions, ledger=ledger, title='Admin Dashboard')
