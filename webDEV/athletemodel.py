import pickle
from athletelist import AthleteList
from athletelist import *

def put_to_store(file_list):
    all_athletes={}
    for each_file in file_list:
        ath=get_coach_data(each_file)
        all_athletes[ath.name]=ath
    try:
        with open ('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print "filed error (put and store):"+str(ioerr)

    return all_athletes

def get_to_store():
    all_athletes={}
    try:
        with open ('athletes.pickle','rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
        print "filed error (get and store):"+str(ioerr)
    return all_athletes
file_list=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
data=put_to_store(file_list)
print type(data)
