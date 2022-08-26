from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle

app.config['TESTING'] = True

testBoard1 = [['T','A','B','A','A'],['A','C','A','A','A'],['N','A','K','A','A'],['K','W','A','R','D'],['S','A','A','A','']]

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_find(self):
        bog = Boggle()
        board = bog.make_board()
        self.assertEqual(len(board), 5)

    #def test_findfrom():

    
    #def test_checkvalid():

    #def test_readdict():

    def test_home(self):
        with app.test_client() as client:
            result = client.get('/')
            self.assertEqual(result.status_code, 200)


    def test_wordTesting(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = testBoard1
            result = client.get('/check-word?word=a').get_data(as_text=True)
            self.assertEqual(result, jsonify('ok'))
            result = client.get('/check-word?word=award').get_data(as_text=True)
            self.assertEqual(result, jsonify('ok'))
            result = client.get('/check-word?word=backward').get_data(as_text=True)
            self.assertEqual(result, jsonify('ok'))


    
    def test_notOnBoard(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = testBoard1
            result = client.get('/check-word?word=zymotechnical').get_data(as_text=True)
            self.assertEqual(result, jsonify('not-on-board'))

    def test_notaWord(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = testBoard1
            result = client.get('/check-word?word=3333333').get_data(as_text=True)
            self.assertEqual(result, jsonify('not-word'))
            result = client.get('/check-word?word = aca').get_data(as_text=True)
            self.assertEqual(result, jsonify('not-word'))
            result = client.get('/check-word?word=l0449jnnrjk3kk4ksfeseeeeeeef').get_data(as_text=True)
            self.assertEqual(result, jsonify('not-word'))


#``