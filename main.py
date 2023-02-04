from client.client import DarwinClient


if __name__ == '__main__':
    client = DarwinClient()
    products = client.get_products_list()
    print(products)
