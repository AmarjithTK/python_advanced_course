from flaskmium import osmium


if __name__ == "__main__":
    osmium.secret_key = '4fssg'

    osmium.run(debug=True,port=5000)
