from SPARQLWrapper import SPARQLWrapper, JSON

class Anzo_conn:
    def __init__(self):

        # Replace these with your AnzoGraph server details
        # Assuming AnzoGraph is running in a Docker container with port mapping 80:8080
        self.endpoint_url = "http://localhost:80/sparql"

        # Set the username and password
        self.username = "admin"
        self.password = "Passw0rd1"

        self.sparql = SPARQLWrapper(self.endpoint_url)

        self.sparql.setCredentials(self.username, self.password)

    def connect(self):
        try:
            # Attempt to connect by fetching the AnzoGraph service description
            self.sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
            self.sparql.setReturnFormat(JSON)
            
            # Execute the query and fetch results
            results = self.sparql.query().convert()
            
            # If there are results, the connection is successful
            if results and "results" in results:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")