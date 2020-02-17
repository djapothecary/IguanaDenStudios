from iguanadenstudios import create_app, db

app = create_app()

@app.before_first_request
def create_tables():
    import pdb; pdb.set_trace()
    if app.config['ENV'] =='development':
        import pdb; pdb.set_trace()
        db.create_all()
    else:
        db.create_all()

if __name__ == "__main__":
    app.run(debug = True)