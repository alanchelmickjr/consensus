def moderate_responses(responses, models):
    voting_results = {}
    for model in models:
        votes = model.vote_on_responses(responses)
        voting_results[model.name] = votes
    
    # Calculate the best response based on votes
    best_response = max(responses.items(), key=lambda x: sum(v[x[0]] for v in voting_results.values()))[1]
    
    return best_response, voting_results