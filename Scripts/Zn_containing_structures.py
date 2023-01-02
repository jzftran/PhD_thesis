import json
import requests
from datetime import date

def fetch_PDB_Zn_codes(to_date):

    """Fetchs PDB codes for all structures with zinc ion in them.
    If the response returned has an 500 error code, an error will
    be comunicated.
    Date 2020-09-18 in the rcsb_accession_info.initial_release_date
    is the publication date of https://doi.org/10.1016/j.tibs.2020.08.011  """
    string = '''
    {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
        {
            "type": "terminal",
            "service": "text_chem",
            "parameters": {
            "operator": "exact_match",
            "value": "ZN",
            "attribute": "rcsb_chem_comp_container_identifiers.comp_id"
          }
        },
      {
         "type": "terminal",
         "service": "text",
            "parameters": {
        "attribute": "rcsb_accession_info.initial_release_date",
        "operator": "range",
        "value": {
        "from": "2020-09-18",
        "to": "'''+to_date.strftime("%Y-%m-%d")+'''"
      }
    }
  }
      ]
    },
    "request_options": {
        "return_all_hits": true
    },
    "return_type": "entry"
    }'''

    query_string= json.loads(string)
    url = 'https://search.rcsb.org/rcsbsearch/v2/query'
    response = requests.post(url,json=query_string)
    if response.status_code == 200: #request has succeeded
        jsonresponse = response.json()
        return [jsonresponse['result_set'][code]['identifier'] for code in range(jsonresponse['total_count'])]

    raise Exception("No fetched codes from RCSB.")

today = date.today()

print(len(fetch_PDB_Zn_codes(today)))
