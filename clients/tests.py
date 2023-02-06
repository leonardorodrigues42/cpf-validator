from rest_framework.test import APITestCase
from .serializers import ClientSerializer
from .models import Client


class ClientTest(APITestCase):    
    @classmethod
    def setUpTestData(cls):
        valids_CPFs = [
            "34046505060",
            "20195011040",
            "60639409016",
            "22322178098",
            "21418975052",
            "45191567005",
        ]
        cls.clients = [Client.objects.create(name="Teste", birth="2000-09-13", cpf=cpf) for cpf in valids_CPFs]
    
    def test_can_list_clients(self):
        response = self.client.get("/clients/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), len(self.clients))
        
    def test_can_create_client(self):
        data = {
            "name": "Teste Create",
            "birth": "13/09/2000",
            "cpf": "162.568.220-48"
        }
        response = self.client.post("/clients/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), len(self.clients) + 1)
        self.assertEqual(Client.objects.get(cpf="16256822048").name, "Teste Create")
        
    def test_not_can_create_client_whit_invalid_cpf(self):
        data = {
            "name": "Teste Create",
            "birth": "13/09/2000",
            "cpf": "152.548.222-39"
        }
        response = self.client.post("/clients/", data, format="json")
        self.assertEqual(response.status_code, 422)
        
    def test_can_retrieve_client(self):
        cpf = self.clients[2].cpf
        response = self.client.get(f"/clients/{cpf}/", format="json")
        
        self.assertEqual(response.status_code, 200)