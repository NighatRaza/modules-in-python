def make_album(artist_name,album_title,num_tracks=None):
    """ """
    music_album = {}
    music_album['artist']=artist_name
    music_album['album']=album_title
    if num_tracks:
        music_album['tracks'] = num_tracks
    
    return music_album


# made a new dict and save all the content (profile)

def build_profile(first,last,**user_info):
    profile={}
    profile['first name']=first
    profile['last name'] = last
    for key,val in user_info.items():
        profile[key]=val
    return profile


students = ['Asad','Aqsa','Danish','Fahad','Kiran']

def promoteStudent(list_of_st):
    promotedSt = []
    for st in list_of_st:
        promotedSt.append(st)
    print(promotedSt)
    print(list_of_st)

