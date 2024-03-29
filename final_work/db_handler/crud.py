from db_handler.scheme import Base, Model
from sqlalchemy import create_engine
from sqlalchemy import delete, select, MetaData
from sqlalchemy.orm import Session, sessionmaker
import datetime
from exceptions.exceptions import UniqueCardError


class BaseCrud():
    def __init__(self, dbpath):
        self.engine = create_engine(dbpath, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=self.engine)
        autocommit_engine = self.engine.execution_options(autocommit=True)
        self.metadata = MetaData()
        Base.registry.configure()
        Base.metadata.create_all(self.engine)

    def get_cards(self):
        with Session(self.engine) as session:
            stmt = select(Model)
            cards = [] 
            for card in session.scalars(stmt):
                cards.append({
                    'user': card.user_name,
                    'cardCode': card.card_code
                })
            return cards
            
    def insert_card(self, Card):
        with Session(self.engine) as session:
            stmt = select(Model).where(Model.user_name.is_(Card.user), Model.card_code.is_(Card.cardCode))
            if len(list(session.scalars(stmt))) != 0:
                raise UniqueCardError("Татая карта уже есть в списке")
            else:
                card = Model(
                    user_name = Card.user,
                    card_code = Card.cardCode,
                    created_at = datetime.datetime.now()
                    )
                session.add(card)
                session.commit()
                return True
    
    def delete_card_by_name(self, Card):
        with Session(self.engine) as session:
            i = session.query(Model).filter(Model.user_name == Card.user, Model.card_code == Card.cardCode).one()
            session.delete(i)
            session.commit()
