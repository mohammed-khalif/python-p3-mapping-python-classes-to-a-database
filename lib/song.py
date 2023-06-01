from config import CONN, CURSOR

class Song:
  
#    class attribute
#     name = "nimco"                        class attribute

    def __init__(self, name, album):
        #   //intances atrribute
        self.id = None                          
        self.name = name                    
        self.album = album

    # class method
    # never take a self it take cls
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """


        CURSOR.execute(sql)


    def save(self):
        sql = """
        INSERT INTO songs (name, album)
        VALUES (?,?)
        """
        
        CURSOR.execute(sql,(self.name, self.album))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):    
        song = Song(name, album)
        song.save()
        return song
    



















# print (Song.name)
# song1 = Song("nice", "nasheed")   
#                             #  intance
# print(song1.name)
# print(song1.album)
print(Song.create("ssooo", "music").__dict__)