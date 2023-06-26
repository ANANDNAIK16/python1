class TV:
     def __init__(self):
        self._maxprice=10000#protected number
        def sp (self):
            print(self._maxprice)
        def setmaxsp(self,price):
            self._maxprice=price
            t=TV()
            t.sp()


            t._maxprice=100000
            t.sp()

            t.setmaxsap(5)
            t.sp()


        
