# Darwinex Reader

This reader is capable of reading resources from the darwinex API.

## Setup

### Requirements

Need to create a virtual env first and then install the requirements by the following command:
```shell script
 pip install -r requirements.pip
```

Add `API_BASE_URL` & `BEARER_TOKEN` in the `.env` file and you're all set to run the magic.

## How the client works?

Client reads the token and base url from the env file and fetches the list of products from the Rest API that is
written to get several things already. We can add more things to fetch just by writing more methods and 
reading through them. 


## Supported methods

```shell script
 |-- get_products_list: list all the products
```
