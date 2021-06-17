class Settings:

    def __init__(self):

        #APP CONF
        self.title = "Palembang Hamster App"


        #WINDOW CONF
        base = 50
        ratio = (16, 9)
        self.width = base*ratio[0]
        self.height = base*ratio[1]
        self.side = self.width*self.height
        self.screen = f"{self.width}x{self.height}+500+500"


        #IMG CONF
        self.logo = "img/logo.jpg"

        #DUMMY DATA CONTACTS

        self.contacts = [
            {
                "1" : {
                    "product" : "Bathtub Besar",
                    "capital" : "14.600",
                    "selles_price" : "16.000",
                    "net_profit" : "1.400"
 
                }
            },
            {
                "2" : {
                    "product" : "Botol Minum Dot",
                    "capital" : "9.000",
                    "selles_price" : "10.000",
                    "net_profit" : "1.000"
 
                }
            },
            {
                "3" : {
                    "product" : "Botol Navo",
                    "capital" : "9.000",
                    "selles_price" : "10.000",
                    "net_profit" : "1.000"
 
                }
            },
            {
                "4" : {
                    "product" : "Fish oil 25 Butir",
                    "capital" : "14.200",
                    "selles_price" : "18.000",
                    "net_profit" : "3.800"
 
                }
            },
            {
                "5" : {
                    "product" : "Gigitan Stick Kayu",
                    "capital" : "12.000",
                    "selles_price" : "15.000",
                    "net_profit" : "3.000"
 
                }
            },
            {
                "6" : {
                    "product" : "Hamsfood",
                    "capital" : "4.100",
                    "selles_price" : "5.000",
                    "net_profit" : "900"
 
                }
            },
            {
                "7" : {
                    "product" : "Hamster House",
                    "capital" : "8.600",
                    "selles_price" : "10.000",
                    "net_profit" : "2.400"
 
                }
            },
            {
                "8" : {
                    "product" : "Hamsvit",
                    "capital" : "11.000",
                    "selles_price" : "14.000",
                    "net_profit" : "3.000"
 
                }
            },
            {
                "9" : {
                    "product" : "Jogging Ball",
                    "capital" : "20.500",
                    "selles_price" : "22.000",
                    "net_profit" : "1.500"
 
                }
            },
            {
                "10" : {
                    "product" : "Mixfood 200gr",
                    "capital" : "20.500",
                    "selles_price" : "22.000",
                    "net_profit" : "1.500"
 
                }
            },
            {
                "11" : {
                    "product" : "Niteangel Moss",
                    "capital" : "16.000",
                    "selles_price" : "18.000",
                    "net_profit" : "2.000"
 
                }
            },
            {
                "12" : {
                    "product" : "Original Nex 250gr",
                    "capital" : "16.200",
                    "selles_price" : "18.000",
                    "net_profit" : "1.800"
 
                }
            },
            {
                "13" : {
                    "product" : "Pasir Mandi Jolly",
                    "capital" : "15.300",
                    "selles_price" : "18.000",
                    "net_profit" : "2.700"
 
                }
            },
            {
                "14" : {
                    "product" : "Pasir Mandi Sanbbi",
                    "capital" : "13.800",
                    "selles_price" : "15.000",
                    "net_profit" : "1.200"
 
                }
            },
            {
                "15" : {
                    "product" : "Pasir Mandi Sweet",
                    "capital" : "10.000",
                    "selles_price" : "12.000",
                    "net_profit" : "2.000"
 
                }
            },
            {
                "16" : {
                    "product" : "Pasir Zeolit No.3",
                    "capital" : "26.600",
                    "selles_price" : "28.000",
                    "net_profit" : "1.400"
 
                }
            },
            {
                "17" : {
                    "product" : "Plate Tempat Makan",
                    "capital" : "14.000",
                    "selles_price" : "20.000",
                    "net_profit" : "6.000"
 
                }
            },
            {
                "18" : {
                    "product" : "Roda Putar Besar",
                    "capital" : "2.000",
                    "selles_price" : "8.000",
                    "net_profit" : "6.000"
 
                }
            },
            {
                "19" : {
                    "product" : "Roda Putar Tipe B",
                    "capital" : "17.000",
                    "selles_price" : "25.000",
                    "net_profit" : "8.000"
 
                }
            },
            {
                "20" : {
                    "product" : "Rolled Oat",
                    "capital" : "9.000",
                    "selles_price" : "15.000",
                    "net_profit" : "6.000"
 
                }
            },
            {
                "21" : {
                    "product" : "Rumah Mainan",
                    "capital" : "13.000",
                    "selles_price" : "20.000",
                    "net_profit" : "7.000"
 
                }
            },
            {
                "22" : {
                    "product" : "Sauna Rocket",
                    "capital" : "16.000",
                    "selles_price" : "20.000",
                    "net_profit" : "4.000"
 
                }
            },
            {
                "23" : {
                    "product" : "Serbuk Kayu Impor ",
                    "capital" : "21.900",
                    "selles_price" : "23.000",
                    "net_profit" : "1.100"
 
                }
            },
            {
                "24" : {
                    "product" : "Tempat Makan Akrilik",
                    "capital" : "6.400",
                    "selles_price" : "11.000",
                    "net_profit" : "4.600"
 
                }
            },
            {
                "25" : {
                    "product" : "Tempelan Karet",
                    "capital" : "17.000",
                    "selles_price" : "19.000",
                    "net_profit" : "2.000"
 
                }
            },
            {
                "26" : {
                    "product" : "Terowongan X",
                    "capital" : "13.000",
                    "selles_price" : "16.000",
                    "net_profit" : "3.000"
 
                }
            }
 
        ]