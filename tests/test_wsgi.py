# tests/test_wsgi.py
from flask_testing import app
from wsgi import app

class TestViews(TestCare):
    def create_app():
        app.config['TESTING']=True
        return app
    
    def test_one_roll(self):
        roll=self.client.get('/').json['roll']
        self.assertIsInstance(roll,int)
        self.assertGreater(roll,0)
        self.assertless(roll,7)