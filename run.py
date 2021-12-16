from flaskmium import osmium


if __name__ == "__main__":
    osmium.secret_key = '4sgswadfsg'

    osmium.run(debug=True,port=4500)
