import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

#####################################################################################################################################################

def init_api():
	global api
	client_id = INTRA_CLIENT
	client_secret = INTRA_SECRET
	client = BackendApplicationClient(client_id=client_id)
	api = OAuth2Session(client=client)
	token = api.fetch_token(token_url='https://api.intra.42.fr/oauth/token', client_id=client_id, client_secret=client_secret)
	return(api)


async def request(url) :
	try :
		raw = api.get(f'https://api.intra.42.fr/v2/{url}')
	except :
		init_api()
		raw = api.get(f'https://api.intra.42.fr/v2/{url}')
	finally :
		if str(raw) == "<Response [200]>" or str(raw) == "<Response [404]>":
			return raw.json()
		else:
			await print(f"bad request with : {url}")
			return raw.json()

#####################################################################################################################################################


class IntraGroups :
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str

class IntraCursusUsers :
    def __init__(self,id:int, name:str, level:int, begin_at, end_at) -> None:
        self.id = id
        self.name = name
        self.level = level
        self.begin_at = begin_at
        self.end_at = end_at
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str
    level = int
    begin_at = str
    end_at = str

class IntraProjectsUser :
    def __init__(self, id: int,name:str,  occurrence: int, final_mark: int, status: str, validated: bool, cursus_ids:list, marked_at:str, marked:bool, retriable_at:str) -> None:
        self.id = id
        self.name = name
        self.occurrence = occurrence
        self.final_mark = final_mark
        self.status = status
        self.validated = validated
        self.cursus_ids = cursus_ids
        self.marked_at = marked_at
        self.marked = marked
        self.retriable_at = retriable_at
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str
    occurrence = int
    final_mark = int
    status = str
    validated = bool
    cursus_ids = []
    marked_at = str
    marked = bool
    retriable_at = str

class IntraLanguage :
    def __init__(self, id: int, position: int) -> None:
        self.id = id
        self.position = position
        pass
    def __str__(self) -> str:
        return(self.language_id)
    id = int
    position = int

class IntraAchievement :
    def __init__(self, id: int, name: str, description: str, value:int) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.value = value
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str
    description = str
    value = int

class IntraTitleUser :
    def __init__(self, id: int, name: str, selected:bool) -> None:
        self.id = id
        self.name = name
        self.selected = selected
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str
    selected = bool

class IntraPartnership :
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str

class IntraExpertiseUser :
    def __init__(self, id: int, interested: bool, value: int) -> None:
        self.id = id
        self.interested = interested
        self.value = value
        pass
    def __str__(self) -> str:
        return(self.value)
    id = int
    interested = bool
    value = int

class IntraRoles :
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str

class IntraCampus :
    def __init__(self, id: int, name: str, is_primary:bool) -> None:
        self.id = id
        self.name = name
        self.is_primary = is_primary
        pass
    def __str__(self) -> str:
        return(self.name)
    id = int
    name = str
    is_primary = bool

class IntraUser :
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return(self.login)

    def printall(self) -> None:
        #print all the user data
        print(f"User id: {self.id}")
        print(f"User login: {self.login}")
        print(f"User correction_point: {self.correction_point}")
        print(f"User pool_month: {self.pool_month}")
        print(f"User pool_year: {self.pool_year}")
        print(f"User location: {self.location}")
        print(f"User wallet: {self.wallet}")
        print(f"User alumni: {self.alumni}")
        print(f"User active: {self.active}")
    
        #print all the groups
        print(f"User groups:")
        for group in self.groups:
            print(f"    Group id: {group.id}")
            print(f"    Group name: {group.name}")
            print(f"    ____________________________________________________________")
        
        #print all the cursus
        print(f"User cursus:")
        for cursus in self.cursus:
            print(f"    Cursus id: {cursus.id}")
            print(f"    Cursus name: {cursus.name}")
            print(f"    Cursus level: {cursus.level}")
            print(f"    Cursus begin_at: {cursus.begin_at}")
            print(f"    Cursus end_at: {cursus.end_at}")
            print(f"    ____________________________________________________________")
        
        #print all the projects
        print(f"User projects:")
        for projects in self.projects:
            print(f"    Projects id: {projects.id}")
            print(f"    Projects name: {projects.name}")
            print(f"    Projects occurrence: {projects.occurrence}")
            print(f"    Projects final_mark: {projects.final_mark}")
            print(f"    Projects status: {projects.status}")
            print(f"    Projects validated: {projects.validated}")
            print(f"    Projects cursus_ids: {projects.cursus_ids}")
            print(f"    Projects marked_at: {projects.marked_at}")
            print(f"    Projects marked: {projects.marked}")
            print(f"    Projects retriable_at: {projects.retriable_at}")
            print(f"    ____________________________________________________________")
    
        #print all the languages
        print(f"User languages:")
        for languages in self.languages:
            print(f"    Languages id: {languages.id}")
            print(f"    Languages position: {languages.position}")
            print(f"    ____________________________________________________________")
    
        #print all the achievements
        print(f"User achievements:")
        for achievement in self.achievements:
            print(f"    Achievement id: {achievement.id}")
            print(f"    Achievement name: {achievement.name}")
            print(f"    Achievement description: {achievement.description}")
            print(f"    Achievement value: {achievement.value}")
            print(f"    ____________________________________________________________")
    
        #print all the titles
        print(f"User titles:")
        for titles in self.titles:
            print(f"    Titles id: {titles.id}")
            print(f"    Titles name: {titles.name}")
            print(f"    Titles selected: {titles.selected}")
            print(f"    ____________________________________________________________")
    
        #print all the partnerships
        print(f"User partnerships:")
        for partnership in self.partnerships:
            print(f"    Partnership id: {partnership.id}")
            print(f"    Partnership name: {partnership.name}")
            print(f"    ____________________________________________________________")
    
        #print all the expertises
        print(f"User expertises:")
        for expertises in self.expertises:
            print(f"    Expertises id: {expertises.id}")
            print(f"    Expertises interested: {expertises.interested}")
            print(f"    Expertises value: {expertises.value}")
            print(f"    ____________________________________________________________")
    
        #print all the roles
        print(f"User roles:")
        for role in self.roles:
            print(f"    Role id: {role.id}")
            print(f"    Role name: {role.name}")
            print(f"    ____________________________________________________________")
    
        #print all the campus
        print(f"User campus:")
        for campus in self.campus:
            print(f"    Campus id: {campus.id}")
            print(f"    Campus name: {campus.name}")
            print(f"    Campus is_primary: {campus.is_primary}")
            print(f"    ____________________________________________________________")

    id = int
    login = str
    correction_point = int
    pool_month = str
    pool_year = int
    location = str
    wallet = int
    alumni = bool
    active = bool

    def addgroups(self, id: int, name: str) -> None :
        self.groups.append(IntraGroups(id, name))
    groups = []

    def addcursus(self, id:int, name:str, level:int, begin_at, end_at) -> None :
        self.cursus.append(IntraCursusUsers(id, name, level, begin_at, end_at))
    cursus = []

    def addprojects(self, id: int, name:str, occurrence: int, final_mark: int, status: str, validated: bool, cursus_ids: list, marked_at, marked: bool, retriable_at) -> None :
        self.projects.append(IntraProjectsUser(id, name, occurrence, final_mark, status, validated, cursus_ids, marked_at, marked, retriable_at))
    projects = []

    def addlanguages(self, id: int, position: int) -> None :
        self.languages.append(IntraLanguage(id, position))
    languages = []

    def addachievements(self, id: int, name: str, description: str, value) -> None :
        self.achievements.append(IntraAchievement(id, name, description, value))
    achievements = []

    def addtitles(self, id: int, name: str, selected: bool) -> None :
        self.titles.append(IntraTitleUser(id, name, selected))
    titles = []

    def addpartnerships(self, id: int, name: str) -> None :
        self.partnerships.append(IntraPartnership(id, name))
    partnerships = []

    def addexpertises(self, id: int, interested: bool, value: int) -> None :
        self.expertises.append(IntraExpertiseUser(id, interested, value))
    expertises = []

    def addroles(self, id: int, name: str) -> None :
        self.roles.append(IntraRoles(id, name))
    roles = []

    def addcampus(self, id: int, name: str, is_primary:str) -> None :
        self.campus.append(IntraCampus(id, name, is_primary))
    campus = []

async def get_user(login: str) -> IntraUser:

    json = await request(f"users/{login}")
    try:
        user = IntraUser()
        user.login = json["login"]
        user.id = json["id"]
        user.login = json["login"]
        user.correction_point = json["correction_point"]
        user.pool_month = json["pool_month"]
        user.pool_year = json["pool_year"]
        user.location = json["location"]
        user.wallet = json["wallet"]
        user.alumni = json["alumni?"]
        user.active = json["active?"]
        for group in json["groups"]:
            user.addgroups(group["id"], group["name"])

        for cursus_user in json["cursus_users"]:
            user.addcursus(cursus_user["cursus"]["id"], cursus_user["cursus"]["name"], cursus_user["level"], cursus_user["begin_at"], cursus_user["end_at"])
        
        for projects_user in json["projects_users"]:
            user.addprojects(projects_user["project"]['id'], projects_user["project"]['name'], projects_user["occurrence"], projects_user["final_mark"], projects_user["status"], projects_user["validated?"], projects_user["cursus_ids"], projects_user["marked_at"], projects_user["marked"], projects_user["retriable_at"])
        
        for language_user in json["languages_users"]:
            user.addlanguages(language_user["language_id"], language_user["position"])

        for achievement in json["achievements"]:
            user.addachievements(achievement["id"], achievement["name"], achievement["description"], achievement["nbr_of_success"])
        i = 0
        for title_user in json["titles"]:
            selected = json["titles_users"][i]
            selected = selected["selected"]
            user.addtitles(title_user["id"], title_user["name"], selected)
            i += 1
        
        for partnership in json["partnerships"]:
            user.addpartnerships(partnership["id"], partnership["name"])
        
        for expertise_user in json["expertises_users"]:
            user.addexpertises(expertise_user["expertise_id"], expertise_user["interested"], expertise_user["value"])
        
        for role in json["roles"]:
            user.addroles(role["id"], role["name"])
        
        i = 0
        for campus in json["campus"]:
            primary = json["campus_users"][i]
            primary = primary["is_primary"]
            user.addcampus(campus["id"], campus["name"], primary)
            i += 1
        
        return(user)
    except:
        return(None)

