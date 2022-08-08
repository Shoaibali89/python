class bill:
    def __init__(self,customername,units,month):
        self.cname=customername
        self.units=units
        self.month=month
        fa=15
        mc=10
    def amt(self):
        if(self.units<25):
            fa=15
            mc=10
            mvca1=self.units*0.29
            sum1=(self.units*4.89)+mvca1+fa+mc
            state1=(f"the total amt of{self.cname} is {sum1} for {self.month}")
            print(state1)
        elif(self.units>25 and self.units<=60):
            fa=15
            mc=10
            mvca2=self.units*0.29
            sum2=(25*4.89)+(self.units-25)*5.40+fa+mc+mvca2
            state2=(f"the total amt of{self.cname} is {sum2} for {self.month}")
            print(state2)
        elif(self.units>60 and self.units<=100):
            fa=15
            mc=10
            mvca3=self.units*0.29
            sum3=(25*4.89)+35*5.40+(self.units-60)*6.41+fa+mc+mvca3
            state3=(f"the total amt of{self.cname} is {sum3} for {self.month}")
            print(state3)
        elif(self.units>100 and self.units<=150):
            fa=15
            mc=10
            mvca4=self.units*0.29
            sum4=(25*4.89)+35*5.40+40*6.41+(self.units-100)*7.16+fa+mc+mvca4
            state4=(f"the total amt of{self.cname} is {sum4} for {self.month}")
            print(state4)
        elif(self.units>150 and self.units<=300):
            fa=15
            mc=10
            mvca5=self.units*0.29
            sum5=(25*4.89)+35*5.40+40*6.41+50*7.16(self.units-150)*7.33+fa+mc+mvca5
            state5=(f"the total amt of{self.cname} is {sum5} for {self.month}")
            print(state5)
        elif(self.units>300):
            fa=15
            mc=10
            mvca6=self.units*0.29
            sum6=(25*4.89)+35*5.40+40*6.41+50*7.16+150*7.33(self.units-300)*8.92+fa+mc+mvca6
            state6=(f"the total amt of{self.cname} is {sum6} for {self.month}")
            print(state6)
