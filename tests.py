import unittest
from worker import WorkersHandler
from worker import Worker
from clients import ClientsHandler
from clients import Client
from shipment import ShipmentHandler
from shipment import Shipment

class TestWorker(unittest.TestCase):
    def test_patern(self):
        worker = WorkersHandler()
        t = worker.setName("456", "FDG", "df")
        self.assertEqual(t, False, "Should False")

    def test_change(self):
        Worker(0).changeData("Дмитрий", "Дуплий", "Олегович")
        self.assertEqual([Worker(0).name, Worker(0).surename, Worker(0).patronymic], ["Дмитрий", "Дуплий", "Олегович"], "Should False")

class TestClients(unittest.TestCase):
    def test_patern(self):
        client = ClientsHandler()
        t = client.setName("456", "FDG", "df", "fdg", "ffdg", "fg")
        self.assertEqual(t, False, "Should False")

    def test_change(self):
        Client(0).changeData("Дмитрий", "Дуплий", "Олегович", "Пушкниа", "Колотушкина", 69)
        self.assertEqual([Client(0).name, Client(0).surename, Client(0).patronymic, Client(0).street, Client(0).house, Client(0).phone_number],
         ["Дмитрий", "Дуплий", "Олегович", "Пушкниа", "Колотушкина", 69], "Should False")

class TestShipment(unittest.TestCase):
    def test_change(self):
        Shipment(0).changeData("Никита Алексеенко", "22.10.2000", "Сахар", 1, "Алексеенко Алексеевич", "Колотушкина")
        self.assertEqual([Shipment(0).Courier, Shipment(0).Date, Shipment(0).Product, Shipment(0).Count, Shipment(0).Client, Shipment(0).Address],
         ["Никита Алексеенко", "22.10.2000", "Сахар", 1, "Алексеенко Алексеевич", "Колотушкина"], "Should False")

if __name__ == '__main__':
    unittest.main()
