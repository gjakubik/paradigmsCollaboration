# paradigmsCollaboration
Repository for collaboration with group mates on class assignments in Programming Paradigms

OO API

Our program extracts various pieces of information from our data source. The way we store the information is strategic as to be efficient when we later allow the user to interact with the data. The user is able to filter through the data by a variety of factors, including year or the incident and country where the incident took place. When these filters are put in to place, our program will query the dictionary to identify the desired results. The surver makes request to the endpoint using one of three parameters: event id, country, and year. A json object is returned. 

To run the tests, run the following command: python3 test_server.py
