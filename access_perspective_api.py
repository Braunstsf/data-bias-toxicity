from googleapiclient import discovery
import json

API_KEY = XXX

def find_toxicity_score(comment): 
    client = discovery.build(
      "commentanalyzer",
      "v1alpha1",
      developerKey=API_KEY,
      discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
      static_discovery=False,
    )

    analyze_request = {
      'comment': { 'text': comment},
      'requestedAttributes': {'TOXICITY': {}}
    }

    response = client.comments().analyze(body=analyze_request).execute()
    toxicity_score = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
    
    return(toxicity_score)