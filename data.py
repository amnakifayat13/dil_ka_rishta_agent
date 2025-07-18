from dataclasses import dataclass
from typing import Dict, List

@dataclass
class UserData:
    age: int
    info: Dict[str, str]
    
@dataclass
class AllPartners:
     partners: List[UserData]       

partners_context = AllPartners(partners=[
    UserData(age=22, info={"name": "Areeba", "qualification": "BS", "passion": "teacher", "religion": "islam", "gender": "female"}),
    UserData(age=30, info={"name": "Hamza", "qualification": "MS", "passion": "engineer", "religion": "islam", "gender": "male"}),
    UserData(age=27, info={"name": "Fatima", "qualification": "PhD", "passion": "scientist", "religion": "islam", "gender": "female"}),
    UserData(age=28, info={"name": "Ali", "qualification": "BS", "passion": "programmer", "religion": "islam", "gender": "male"}),
    UserData(age=24, info={"name": "Hira", "qualification": "MS", "passion": "designer", "religion": "islam", "gender": "female"}),
    UserData(age=35, info={"name": "Usman", "qualification": "PhD", "passion": "pilot", "religion": "islam", "gender": "male"}),
    UserData(age=23, info={"name": "Zainab", "qualification": "BS", "passion": "doctor", "religion": "islam", "gender": "female"}),
    UserData(age=31, info={"name": "Bilal", "qualification": "MS", "passion": "teacher", "religion": "islam", "gender": "male"}),
    UserData(age=29, info={"name": "Mariam", "qualification": "PhD", "passion": "engineer", "religion": "islam", "gender": "female"}),
    UserData(age=26, info={"name": "Tariq", "qualification": "BS", "passion": "scientist", "religion": "islam", "gender": "male"}),
    UserData(age=21, info={"name": "Sana", "qualification": "BS", "passion": "nurse", "religion": "islam", "gender": "female"}),
    UserData(age=25, info={"name": "Arif", "qualification": "PhD", "passion": "doctor", "religion": "islam", "gender": "male"}),
    UserData(age=33, info={"name": "Kashif", "qualification": "PhD", "passion": "programmer", "religion": "islam", "gender": "male"}),
    UserData(age=26, info={"name": "Iqra", "qualification": "MS", "passion": "teacher", "religion": "islam", "gender": "female"}),
    UserData(age=29, info={"name": "Zubair", "qualification": "MS", "passion": "pilot", "religion": "islam", "gender": "male"}),
    UserData(age=20, info={"name": "Nida", "qualification": "BS", "passion": "designer", "religion": "islam", "gender": "female"}),
    UserData(age=34, info={"name": "Noman", "qualification": "MS", "passion": "doctor", "religion": "islam", "gender": "male"}),
    UserData(age=22, info={"name": "Laiba", "qualification": "BS", "passion": "teacher", "religion": "islam", "gender": "female"}),
    UserData(age=27, info={"name": "Saad", "qualification": "PhD", "passion": "engineer", "religion": "islam", "gender": "male"}),
    UserData(age=28, info={"name": "Ayesha", "qualification": "PhD", "passion": "scientist", "religion": "islam", "gender": "female"})
])
