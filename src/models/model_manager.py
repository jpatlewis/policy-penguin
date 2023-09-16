from sqlalchemy.orm import Session

class ModelManager:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()

    def read(self, id):
        return self.session.query(self.model).get(id)

    def read_all(self):
        return self.session.query(self.model).all()

    def update(self, entity):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
