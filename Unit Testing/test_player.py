# When writing tests what should you explicitly be testing:
#
#
# Use the same name for the class as the module you are testing
#
# When writing a test method , you have to use "test_" when naming the function so it can be run
#
# Assert method are use in the test functions to confirm the answer againt the expected output
# 

# Assertraises value error == look into test use
# Look into syntax for unit testing using python unittest library

import unittest
import player

class TestPlayer(unittest.TestCase):
    # The setup function runs its code before every single test
    # Used to initialize stuff that will be used in the tests. Eg ; if you have to create an object instance for a class every time you want o run a test,
    # instead of creating an object for every test , create the objects in the setup function.
    def setup(self):
        pass
    
    # The teaRDown function runs its code after every single test
    # uUse it to delete the stufff generated from running the tests eg; databases , allocated memory
    def tearDown(self) -> None:
        pass
    def test_1(self):
        result=player.playing()
        self.assertEqual(result,True)
    
    def test_2(self):
        result=player.defending()
        self.assertEqual(result,False)

if __name__=='__main__':
    unittest.main()

# Mocking
#  
# 
# 
# 
# 