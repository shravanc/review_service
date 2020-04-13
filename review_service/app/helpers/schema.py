from flask import request, jsonify, render_template
from urllib.parse import urlparse

SUPPORTED_SUMDOMAIN = ['amazon', 'netflix']

def get_schema():
  url = request.url
  domain = urlparse(request.url).netloc.split(':')[0]
  subdomain = domain.split('.')[0]  

  schema = 'public'
  if subdomain in SUPPORTED_SUMDOMAIN:
    schema = subdomain

  
  return schema


