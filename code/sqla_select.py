from sqlalchemy import and_
from seabass_model import *


session = get_session('postgres:///seabass_db')
species = session.query(Species).filter(Species.common_name == 'seabass').one()
query = session.query(Protein.name, 
                      GoTerm.name, 
                      GoTerm.namespace).join(Protein.goterms).filter(Protein.species == species).limit(10)
