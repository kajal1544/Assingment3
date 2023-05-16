import json

# Open JSON file
with open('input.json') as file:
    # Load JSON object as a dictionary
    data = json.load(file)

    # Iterate through the parametersList in the JSON
    List = []
    for parameter in data['parametersList']:
        myDict = {
            "parameterName": parameter.get('parameterName'),
            "max": parameter.get('max'),
            "min": parameter.get('min'),
            "avg": parameter.get('avg')
        }
        List.append(myDict)
        myList: str = json.dumps(List, indent=4)

    # Print the extracted values
    print(myList)

    jsonString = json.dumps(List)
    jsonFile = open("output.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
