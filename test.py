import unittest
import json

class JsonDumpable(object):
    def to_json(self):
        """converts the class object into a json object 
        code is coppied from stackoverflow 
        https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
        """

        return json.dumps (self, 
            default= lambda o: o.__dict__ , 
            sort_keys=True, 
            indent=4
        )


class User(JsonDumpable):
    def __init__(self,name,email):
        """Constructor function requires a string name and returns goal object"""
        self.name = name
        self.email = email # must be unique
        self.goals_array = []


class Goal(JsonDumpable):
    """A goal object """
    def __init__(self,name):
        """Constructor function requires a string name and returns goal object"""
        self.name = name
        self.achieved = False
        self.archived = False
        self.tasks_array = []
    


    def get_goal_by_id(goal_id,user_id):
        
        return 
        
    

class TestGoalsApi(unittest.TestCase):
    def test_get_goal_by_id(self):
        
        actual = Goal.get_goal_by_id(goal_id=1,user_id=1)
        
        goal = Goal('Goal 1').to_json()
        
        expected = json.dumps(goal)

        self.assertEqual(actual, expected)

### bash :
#  python -m unittest tests.py 
