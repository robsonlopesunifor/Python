import unittest
import json

class Pandas(unittest.TestCase):

    def test_pickle_serealizacao_dados(self):
        print '----------------test_pickle_serealizacao_dados----------------'
        # pickle é um módulo que provê a serialização de objetos Python,
        # transformando objetos quaisquer em sequências de bytes. 
        import pickle
        lista = [1, 'hello!', [1, 2, 3]]
        s = pickle.dumps(lista)             # serializa
        print s
        lista_recuperada = pickle.loads(s)  # desserealiza
        print lista_recuperada

    def test_pickle_serealizacao_arquivo(self):
        print '----------------test_pickle_serealizacao_arquivo----------------'
        # sem 's': dump   load
        import pickle
        lista = [1, 'hello!', [1, 2, 3]]
        pickle.dump(lista, open('data.pkl', 'wb'))
        recuperada = pickle.load(open('data.pkl'))
        print recuperada

    def test_json_serealizacao_dados(self):
        print '----------------test_json_serealizacao_dados----------------'
        import json
        lista = [1, 'hello!', [1, 2, 3]]
        s = json.dumps(lista)
        print s
        print type(s)
        l = json.loads(s)
        print l
        print type(l)

    def test_json_serealizacao_arquivo(self):
        print '----------------test_json_serealizacao_arquivos----------------'
        import json
        lista = [1, 'hello!', [1, 2, 3]]
        s = json.dump(lista,open('data.json', 'w'))
        print s
        print type(s)
        l = json.load(open('data.json'))
        print l
        print type(l)

    def test_convercoes_json(self):
        print '----------------test_convercoes_json----------------'
        import json

        print '---------json para dicionario'
        json_data = '{"name": "Brian", "city": "Seattle"}'
        python_obj = json.loads(json_data)
        print python_obj["name"]
        print python_obj["city"]

        print '---------json para lista'
        lista = '{"drinks": ["coffee", "tea", "water"]}'
        data = json.loads(lista)
 
        for element in data['drinks']:
            print element

        print '---------passa para decimal'
        from decimal import Decimal
 
        jsondata = '{"number": 1.573937639}'
        x = json.loads(jsondata, parse_float=Decimal)
        print x['number']
        print type(x['number'])

        print '---------imprimir de forma mais organizada'
        json_data = '{"name": "Brian", "city": "Seattle"}'
        python_obj = json.loads(json_data)
        print json.dumps(python_obj, sort_keys=True, indent=4)

    def test_Shelve(self):
        print '----------------test_Shelve----------------'
        # permite a persistir para uso posterior
        import shelve
        user = shelve.open('data.txt')
        user['nickname'] = 'stummjr'
        user['city'] = 'Blumenau'
        user['twitter'] = [1,2,3,4]
        user['blog'] = ''
        print user
        user.close()

        user = shelve.open('data.txt')
        print user
        user['blog'] = 'pythonhelp.wordpress.com'
        user['novo'] = 'texto novo'
        user.close()

        user = shelve.open('data.txt')
        print user['twitter']
        print type(user['twitter'])


if __name__ == "__main__":
    print('____Teste da classe serealizacao')
    unittest.main()
