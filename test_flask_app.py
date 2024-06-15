# Import necessary modules
import unittest
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Import the app and database from the main application code
from app import app, db, User, LoginForm, SignupForm

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Configure the Flask app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_signup(self):
        response = self.app.post('/signup', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        self.assertIn(b'Account created successfully!', response.data)

    def test_login(self):
        hashed_password = generate_password_hash('password123', method='sha256')
        user = User(username='testuser', email='testuser@example.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertIn(b'Login successful!', response.data)

    def test_failed_login(self):
        response = self.app.post('/login', data={
            'username': 'nonexistentuser',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertIn(b'Login failed. Check your username and/or password', response.data)

    def test_dashboard_access_without_login(self):
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    def test_dashboard_access_with_login(self):
        hashed_password = generate_password_hash('password123', method='sha256')
        user = User(username='testuser', email='testuser@example.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        with self.app as client:
            with client.session_transaction() as sess:
                sess['user_id'] = user.id

            response = client.get('/dashboard', follow_redirects=True)
            self.assertIn(b'Dashboard', response.data)

    def test_logout(self):
        hashed_password = generate_password_hash('password123', method='sha256')
        user = User(username='testuser', email='testuser@example.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        with self.app as client:
            with client.session_transaction() as sess:
                sess['user_id'] = user.id

            response = client.get('/logout', follow_redirects=True)
            self.assertIn(b'You have been logged out.', response.data)

if __name__ == '__main__':
    unittest.main()