from zeep import Client

client = Client(wsdl='http://localhost:8001/?wsdl')
client.service.download('comments.csv','6NQhTQIHs1E')