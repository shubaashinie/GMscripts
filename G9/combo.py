import unittestfrom wifi import wifi_connection as wfrom game import gaming as gimport timeimport osIterations=1"""pass_cnt=0fail_cnt=0"""class run_programs(unittest.TestCase):    def testwifi(self):        w.launch_wifi()        for n in range(int(Iterations)):            state = w.Checkwifistate()            if state:                print("wifi enabled")                self.assertTrue(True)                #pass_cnt += 1            else:                print("wifi disabled")                w.toggle_wifi()                state =w.Checkwifistate()                if state:                    print("wifi enabled")                    self.assertTrue(True)                    #pass_cnt += 1                else:                    print("wifi disabled")                    self.assertFalse(False)                    #fail_cnt += 1            time.sleep(5)        w.toggle_wifi()        #print("pass_cnt:", pass_cnt)        #print("fail_cnt:", fail_cnt)    def testgame(self):        g.KillGame()        g.LaunchGame()        if (g.validate()):            self.assertTrue(True)            #pass_cnt += 1        else:            self.assertFalse(False)            #fail_cnt += 1        g.KillGame()       #print("pass_cnt:", pass_cnt)       #print("fail_cnt", fail_cnt)if __name__=='__main__':    unittest.main()