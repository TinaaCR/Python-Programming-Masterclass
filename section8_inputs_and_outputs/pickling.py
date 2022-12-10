import pickle

# imelda = ('More mayhem',
#           'Imedla May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Pysyco'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town waltz')))

# with open("Imelda.pickle", "rb") as imelda_picked:
#     imelda2 = pickle.load(imelda_picked)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

# imelda = ('More mayhem',
#           'Imedla May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Pysyco'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town waltz')))
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("Imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=0)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=0)
#     pickle.dump(2998302, pickle_file, protocol=0)
#
# with open("Imelda.pickle", "rb") as imelda_picked:
#     imelda2 = pickle.load(imelda_picked)
#     even_list = pickle.load(imelda_picked)
#     odd_list = pickle.load(imelda_picked)
#     x = pickle.load(imelda_picked)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
#
# print('=' * 40)
#
# for i in even_list:
#     print(i)
#
# print('=' * 40)
#
# for i in odd_list:
#     print(i)
#
# print('=' * 40)
#
# print(x)

pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")    # denne gjør at filen slettes