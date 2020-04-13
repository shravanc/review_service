from app import create_app

if __name__ == "__main__":
  #app.run(debug=True, host=constant.HOST, port=constant.PORT_NUMBER)
  application = create_app('development.cfg')
  application.run(debug=True, host="0.0.0.0", port="5000")
