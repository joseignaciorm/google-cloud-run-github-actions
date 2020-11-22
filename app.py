import pprint
import requests

# import streamlit as st
from datetime import datetime


def debug_access_token(access_token):
    """
    API Endpoint: https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}
    """
    debug_url = f"https://graph.facebook.com/debug_token?input_token={access_token}&access_token={access_token}"
    response = requests.get(debug_url)

    return response.json()


def get_token_expiry_dates(debug_response):
    token_dates = {}
    token_dates["issued_at"] = datetime.fromtimestamp(
        debug_response["data"]["issued_at"]
    ).strftime("%m/%d/%Y, %H:%M:%S")
    token_dates["data_access_expires_at"] = datetime.fromtimestamp(
        debug_response["data"]["data_access_expires_at"]
    ).strftime("%m/%d/%Y, %H:%M:%S")
    token_dates["expires_at"] = datetime.fromtimestamp(
        debug_response["data"]["expires_at"]
    ).strftime("%m/%d/%Y, %H:%M:%S")

    return token_dates


def exchange_token(client_id, client_secret, access_token, api_version="v8.0"):
    """
    API Endpoint =  https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    """
    exchange_url = f"https://graph.facebook.com/{api_version}/oauth/access_token?grant_type=fb_exchange_token&client_id={client_id}&client_secret={client_secret}&fb_exchange_token={access_token}"
    response = requests.get(exchange_url)

    return response.json()


def refresh_long_lived_access_token(long_lived_access_token):
    """
    API Endpoint =  https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={long-lived-access-token}
    """
    exchange_url = f"https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={long_lived_access_token}"
    response = requests.get(exchange_url)

    return response.json()
