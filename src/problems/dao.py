from .models import Problem
from .schemas import ProblemCreateDB, ProblemUpdate 

from ..dao import BaseDAO


    
class ProblemDAO(BaseDAO[Problem, ProblemCreateDB, ProblemUpdate]):
    model = Problem