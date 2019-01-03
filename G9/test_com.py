import pytest
from wifi import wifi_connection as w
from game import gaming as g
import time

Iterations=1
"""
pass_cnt=0
fail_cnt=0
"""
class Test():
    def test_wifi(self):
        w.launch_wifi()
        for n in range(int(Iterations)):
            state = w.Checkwifistate()
            if state:
                print("wifi enabled")
                assert w.Checkwifistate() == True
                """
                #self.assertTrue(True)
                #pass_cnt += 1

            else:
                print("wifi disabled")
                w.toggle_wifi()
                state =w.Checkwifistate()

                if state:
                    print("wifi enabled")
                    assert w.Checkwifistate() == True
                    #self.assertTrue(True)
                    #pass_cnt += 1

                else:
                    print("wifi disabled")
                    assert w.Checkwifistate() == True
                    #self.assertFalse(False)
                    #fail_cnt += 1
"""
            time.sleep(5)
        w.toggle_wifi()
        #print("pass_cnt:", pass_cnt)
        #print("fail_cnt:", fail_cnt)
    def test_game(self):
        g.KillGame()
        g.LaunchGame()
        #if (g.validate()):
        assert g.validate() ==True
            #self.assertTrue(True)
            #pass_cnt += 1
        #else:
        #assert g.validate() == False
            #self.assertFalse(False)
            #fail_cnt += 1
        g.KillGame()
       #print("pass_cnt:", pass_cnt)
       #print("fail_cnt", fail_cnt)
if __name__=='__main__':
    pytest.main()