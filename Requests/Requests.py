import unittest
import json, requests

class Requests(unittest.TestCase):
    # pip install requests

    def test_requests(self):
        print '----------------test_requests----------------'
        
        print '--------get'
        response = requests.get("http://jsonplaceholder.typicode.com/comments")
        print response.status_code  # codigo para saber se deu certo (200) ou errado (404)
        print response.content
        obj_python = json.loads(response.content)

        print '--------post'
        # inserção de dados em um serviço
        dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
        response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=dados)
        print response.content

        print '--------put'
        # utilizado sobre um determinado recurso quando desejarmos alterá-lo
        dados = {"email": "john@doe.com"}
        response = requests.put("http://jsonplaceholder.typicode.com/comments/10", data=dados)
        print response.content

        print '--------delete'
        # Para apagar um registro
        response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")
        print response.content

if __name__ == "__main__":
    print('____Teste da classe Requests')
    unittest.main()
