#_*_ coding:utf-8 _*_
import MySQLdb

class algoritma():
 #   def __init__(self,k,b,y,c):
  #      self.kilo = k
   #     self.boy = b
    #    self.yas = y
     #   self.cinsiyet = c
    def init(self,k,b,y,c):
        self.kilo = k
        self.boy = b
        self.yas = y
        self.cinsiyet = c
    def database(self):
        #bu fonksiyon ile veritabanına bağlantı işlemlerini yapıyoruz
        # db = self.database()  i kullanarak 5 satırlık kodu her veritabanıyla ilgili bir fonksiyon yazarken kullanmamıza gerek yok
        host = "sql11.freemysqlhosting.net"
        user = "sql11162905"
        pasw = "DNfiw53yq3"
        database = "sql11162905"
        # Open database connection
        return MySQLdb.connect(host, user, pasw, database)
    def dataselect(self):
        #host = "localhost"
        # user = "root"
        # pasw = ""
        # database = "tez"
        # Open database connection
        ##db = MySQLdb.connect(host, user, pasw, database)
        db = self.database()
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * from besinler")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        return data
    def BMR(self):
        if(self.cinsiyet == 'e'):
            self.bmr = 88.362+(13.397*self.kilo)+(4.799*self.boy)-(5.677*self.yas)
            return self.bmr
        if(self.cinsiyet == 'k'):
            self.bmr = 447.593 + (9.247 * self.kilo) + (3.098 * self.boy) - (4.330 * self.yas)
            return self.bmr
    def EER(self,egSeviyesi):
        if(egSeviyesi==1):
            eer=(self.BMR()*1.2)+1
            return eer
        if(egSeviyesi==2):
            eer=(self.BMR()*1.375)+1
            return eer
        if(egSeviyesi==3):
            eer=(self.BMR()*1.55)+1
            return eer
        if (egSeviyesi == 4):
            eer = (self.BMR() * 1.9) + 1
            return eer
    def BesinEkle(self,BesinAdi,Kalori):
        #host = "localhost"
        # user = "root"
        # pasw = ""
        # database = "tez"
        # db = MySQLdb.connect(host, user, pasw, database)
        db=self.database()
        cursor = db.cursor()
        sql="""INSERT INTO besinler(BesinAdi,Kalori)
        VALUES('%s','%s')""" % \
            (BesinAdi,Kalori)
        cursor.execute(sql)
        return db.commit()
    def Listele(self):
        #a = algoritma(29,170,71,'k')
        a = algoritma()
        k = a.dataselect()

        for row in k:
            fname = row[0]
            lname = row[1]
            age = row[2]

            # Now print fetched result
            print "id=%s,Adi=%s,Kalorisi=%s" % \
                  (fname, lname, age)
    def Besin_gir(self):
        n=input("Kaç besin gireceksiniz ?")
        while n>0:
            besin=raw_input("Besin adını giriniz :")
            kalori=input("Kalori miktarını giriniz:")
            algoritma.BesinEkle(besin,kalori)
            n-=1
        print "Besinler Eklendi."


#b = algoritma(29, 170, 71, 'k')
#d=b.Besin_gir()
#g=b.Listele()


