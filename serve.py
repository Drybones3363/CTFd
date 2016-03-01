from CTFd import create_app
app = create_app()
app.run(debug=True, host="bibb.dreamhost.com", port=21)
