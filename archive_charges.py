import fire
import requests

#Shopify Response codes https://help.shopify.com/en/api/getting-started/response-status-codes

#####
#The issue:
#Customer support creates new Shopify orders to charge customers for unreturned items.
#Fulfillment would like to archive these orders so that they do not appear as unarchived unfilled orders.
#
#A solution:
#By accessing the nested value of 'Atoms Experience Additional Charge' we identify orders to be archived and archive them.
#####


base_api_url = "https://atoms-k2.myshopify.com/admin/api/2019-04"


'''
def archive_order(order_name):
    url = "{}/orders.json".format(base_api_url)
    querystring = {"name":order_name}
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': HIDDEN_BASIC_KEY}
    response = requests.request("GET", url, headers=headers, params=querystring)
    orders = response.json()
'''

# archives all of the 'Atoms Experience Additional Charge' orders
def archive_all():
    url = "{}/orders.json".format(base_api_url)
    querystring = {
        "page_size":100,}
    payload = ""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': HIDDEN_BASIC_KEY}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    orders = response.json()
    for one_num in orders['orders']:
        if one_num['line_items'][0]['title'] == 'Atoms Experience Additional Charge':
            print(one_num['id'], one_num['name'], one_num['line_items'][0]['title'])
            print('https://atoms-k2.myshopify.com/admin/orders/' + str(one_num['id']), "Order " + str(one_num['name']))
            urlp = '{}/admin/orders/#'.format(base_api_url) + str(one_num['id']) + '/close.json'
            put_archive = requests.put(urlp, data=payload, headers=headers)
            print(put_archive)


if __name__ == "__main__":
    fire.Fire()
    """
    Example usage:
    1. Archive the charge orders :
    python archive_charges.py  archive_all

    2. Archive only one order :
    python archive_charges.py  archive_order --order_name '7895'
    """
