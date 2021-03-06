# const.py
# AUTOMATICALLY GENERATED - do not edit

DAAP_ITEMKIND_AUDIO = 2

DAAP_MEDIAKIND_TV = 64
DAAP_MEDIAKIND_MOVIE = 32
DAAP_MEDIAKIND_AUDIO = 1
DAAP_MEDIAKIND_VIDEO = 2

DAAP_SONGDATAKIND_STREAM = 1
DAAP_SONGDATAKIND_FILE = 0

DMAP_TYPE_BYTE = 0x1
DMAP_TYPE_UBYTE = 0x2
DMAP_TYPE_SHORT = 0x3
DMAP_TYPE_USHORT = 0x4
DMAP_TYPE_INT = 0x5
DMAP_TYPE_UINT = 0x6
DMAP_TYPE_LONG = 0x7
DMAP_TYPE_ULONG = 0x8
DMAP_TYPE_STRING = 0x9
DMAP_TYPE_DATE = 0xa
DMAP_TYPE_VERSION = 0xb
DMAP_TYPE_LIST = 0xc

dmap_consts = {
    "abal": ("daap.browsealbumlisting", DMAP_TYPE_LIST),
    "abar": ("daap.browseartistlisting", DMAP_TYPE_LIST),
    "abcp": ("daap.browsecomposerlisting", DMAP_TYPE_LIST),
    "abgn": ("daap.browsegenrelisting", DMAP_TYPE_LIST),
    "abpl": ("daap.baseplaylist", DMAP_TYPE_UBYTE),
    "abro": ("daap.databasebrowse", DMAP_TYPE_LIST),
    "adbs": ("daap.databasesongs", DMAP_TYPE_LIST),
#   "aeAD": ("com.apple.itunes.adam-ids-array", DMAP_TYPE_LIST),
    "aeAI": ("com.apple.itunes.itms-artistid", DMAP_TYPE_UINT),
    "aeCI": ("com.apple.itunes.itms-composerid", DMAP_TYPE_UINT),
#   "aeCR": ("com.apple.itunes.content-rating", DMAP_TYPE_STRING),
#   "aeDP": ("com.apple.itunes.drm-platform-id", DMAP_TYPE_UINT),
#   "aeDR": ("com.apple.itunes.drm-user-id", DMAP_TYPE_ULONG),
#   "aeDV": ("com.apple.itunes.drm-versions", DMAP_TYPE_UINT),
    "aeEN": ("com.apple.itunes.episode-num-str", DMAP_TYPE_STRING),
    "aeES": ("com.apple.itunes.episode-sort", DMAP_TYPE_UINT),
#   "aeGD": ("com.apple.itunes.gapless-enc-dr", DMAP_TYPE_UINT),
#   "aeGE": ("com.apple.itunes.gapless-enc-del", DMAP_TYPE_UINT),
#   "aeGH": ("com.apple.itunes.gapless-heur", DMAP_TYPE_UINT),
    "aeGI": ("com.apple.itunes.itms-genreid", DMAP_TYPE_UINT),
#   "aeGR": ("com.apple.itunes.gapless-resy", DMAP_TYPE_ULONG),
#   "aeGU": ("com.apple.itunes.gapless-dur", DMAP_TYPE_ULONG),
#   "aeHD": ("com.apple.itunes.is-hd-video", DMAP_TYPE_UBYTE),
    "aeHV": ("com.apple.itunes.has-video", DMAP_TYPE_UBYTE),
#   "aeK1": ("com.apple.itunes.drm-key1-id", DMAP_TYPE_ULONG),
#   "aeK2": ("com.apple.itunes.drm-key2-id", DMAP_TYPE_ULONG),
    "aeMk": ("com.apple.itunes.extended-media-kind", DMAP_TYPE_UINT),
    "aeMK": ("com.apple.itunes.mediakind", DMAP_TYPE_UBYTE),
#   "aeND": ("com.apple.itunes.non-drm-user-id", DMAP_TYPE_ULONG),
    "aeNN": ("com.apple.itunes.network-name", DMAP_TYPE_STRING),
    "aeNV": ("com.apple.itunes.norm-volume", DMAP_TYPE_UINT),
    "aePC": ("com.apple.itunes.is-podcast", DMAP_TYPE_UBYTE),
    "aePI": ("com.apple.itunes.itms-playlistid", DMAP_TYPE_UINT),
    "aePP": ("com.apple.itunes.is-podcast-playlist", DMAP_TYPE_UBYTE),
    "aePS": ("com.apple.itunes.special-playlist", DMAP_TYPE_UBYTE),
#   "aeSE": ("com.apple.itunes.store-pers-id", DMAP_TYPE_ULONG),
    "aeSF": ("com.apple.itunes.itms-storefrontid", DMAP_TYPE_UINT),
#   "aeSG": ("com.apple.itunes.saved-genius", DMAP_TYPE_UBYTE),
    "aeSI": ("com.apple.itunes.itms-songid", DMAP_TYPE_UINT),
    "aeSN": ("com.apple.itunes.series-name", DMAP_TYPE_STRING),
    "aeSP": ("com.apple.itunes.smart-playlist", DMAP_TYPE_UBYTE),
    "aeSU": ("com.apple.itunes.season-num", DMAP_TYPE_UINT),
    "aeSV": ("com.apple.itunes.music-sharing-version", DMAP_TYPE_UINT),
#   "aeXD": ("com.apple.itunes.xid", DMAP_TYPE_STRING),
    "agrp": ("daap.songgrouping", DMAP_TYPE_STRING),
    "aply": ("daap.databaseplaylists", DMAP_TYPE_LIST),
    "aprm": ("daap.playlistrepeatmode", DMAP_TYPE_UBYTE),
    "apro": ("daap.protocolversion", DMAP_TYPE_VERSION),
    "apsm": ("daap.playlistshufflemode", DMAP_TYPE_UBYTE),
    "apso": ("daap.playlistsongs", DMAP_TYPE_LIST),
    "arif": ("daap.resolveinfo", DMAP_TYPE_LIST),
    "arsv": ("daap.resolve", DMAP_TYPE_LIST),
    "asaa": ("daap.songalbumartist", DMAP_TYPE_STRING),
    "asai": ("daap.songalbumid", DMAP_TYPE_ULONG),
    "asal": ("daap.songalbum", DMAP_TYPE_STRING),
    "asar": ("daap.songartist", DMAP_TYPE_STRING),
#   "asbk": ("daap.bookmarkable", DMAP_TYPE_UBYTE),
#   "asbo": ("daap.songbookmark", DMAP_TYPE_UINT),
    "asbr": ("daap.songbitrate", DMAP_TYPE_USHORT),
    "asbt": ("daap.songbeatsperminute", DMAP_TYPE_USHORT),
    "ascd": ("daap.songcodectype", DMAP_TYPE_UINT),
    "ascm": ("daap.songcomment", DMAP_TYPE_STRING),
    "ascn": ("daap.songcontentdescription", DMAP_TYPE_STRING),
    "asco": ("daap.songcompilation", DMAP_TYPE_UBYTE),
    "ascp": ("daap.songcomposer", DMAP_TYPE_STRING),
    "ascr": ("daap.songcontentrating", DMAP_TYPE_UBYTE),
    "ascs": ("daap.songcodecsubtype", DMAP_TYPE_UINT),
    "asct": ("daap.songcategory", DMAP_TYPE_STRING),
    "asda": ("daap.songdateadded", DMAP_TYPE_DATE),
    "asdb": ("daap.songdisabled", DMAP_TYPE_UBYTE),
    "asdc": ("daap.songdisccount", DMAP_TYPE_USHORT),
    "asdk": ("daap.songdatakind", DMAP_TYPE_UBYTE),
    "asdm": ("daap.songdatemodified", DMAP_TYPE_DATE),
    "asdn": ("daap.songdiscnumber", DMAP_TYPE_USHORT),
#   "asdp": ("daap.songdatepurchased", DMAP_TYPE_DATE),
#   "asdr": ("daap.songdatereleased", DMAP_TYPE_DATE),
    "asdt": ("daap.songdescription", DMAP_TYPE_STRING),
#   "ased": ("daap.songextradata", DMAP_TYPE_USHORT),
    "aseq": ("daap.songeqpreset", DMAP_TYPE_STRING),
    "asfm": ("daap.songformat", DMAP_TYPE_STRING),
    "asgn": ("daap.songgenre", DMAP_TYPE_STRING),
#   "asgp": ("daap.songgapless", DMAP_TYPE_UBYTE),
#   "ashp": ("daap.songhasbeenplayed", DMAP_TYPE_UBYTE),
    "asky": ("daap.songkeywords", DMAP_TYPE_STRING),
    "aslc": ("daap.songlongcontentdescription", DMAP_TYPE_STRING),
#   "asls": ("daap.songlongsize", DMAP_TYPE_ULONG),
#   "aspu": ("daap.songpodcasturl", DMAP_TYPE_STRING),
    "asrv": ("daap.songrelativevolume", DMAP_TYPE_BYTE),
#   "assa": ("daap.sortartist", DMAP_TYPE_STRING),
#   "assc": ("daap.sortcomposer", DMAP_TYPE_STRING),
#   "assl": ("daap.sortalbumartist", DMAP_TYPE_STRING),
#   "assn": ("daap.sortname", DMAP_TYPE_STRING),
    "assp": ("daap.songstoptime", DMAP_TYPE_UINT),
    "assr": ("daap.songsamplerate", DMAP_TYPE_UINT),
#   "asss": ("daap.sortseriesname", DMAP_TYPE_STRING),
    "asst": ("daap.songstarttime", DMAP_TYPE_UINT),
#   "assu": ("daap.sortalbum", DMAP_TYPE_STRING),
    "assz": ("daap.songsize", DMAP_TYPE_UINT),
    "astc": ("daap.songtrackcount", DMAP_TYPE_USHORT),
    "astm": ("daap.songtime", DMAP_TYPE_UINT),
    "astn": ("daap.songtracknumber", DMAP_TYPE_USHORT),
    "asul": ("daap.songdataurl", DMAP_TYPE_STRING),
    "asur": ("daap.songuserrating", DMAP_TYPE_UBYTE),
    "asyr": ("daap.songyear", DMAP_TYPE_USHORT),
#   "ated": ("daap.supportsextradata", DMAP_TYPE_USHORT),
    "avdb": ("daap.serverdatabases", DMAP_TYPE_LIST),
#   "ceJC": ("com.apple.itunes.jukebox-client-vote", DMAP_TYPE_BYTE),
#   "ceJI": ("com.apple.itunes.jukebox-current", DMAP_TYPE_UINT),
#   "ceJS": ("com.apple.itunes.jukebox-score", DMAP_TYPE_SHORT),
#   "ceJV": ("com.apple.itunes.jukebox-vote", DMAP_TYPE_UINT),
    "mbcl": ("dmap.bag", DMAP_TYPE_LIST),
    "mccr": ("dmap.contentcodesresponse", DMAP_TYPE_LIST),
    "mcna": ("dmap.contentcodesname", DMAP_TYPE_STRING),
    "mcnm": ("dmap.contentcodesnumber", DMAP_TYPE_STRING),
    "mcon": ("dmap.container", DMAP_TYPE_LIST),
    "mctc": ("dmap.containercount", DMAP_TYPE_UINT),
    "mcti": ("dmap.containeritemid", DMAP_TYPE_UINT),
    "mcty": ("dmap.contentcodestype", DMAP_TYPE_USHORT),
    "mdcl": ("dmap.dictionary", DMAP_TYPE_LIST),
#   "meds": ("dmap.editcommandssupported", DMAP_TYPE_UINT),
    "miid": ("dmap.itemid", DMAP_TYPE_UINT),
    "mikd": ("dmap.itemkind", DMAP_TYPE_UBYTE),
    "mimc": ("dmap.itemcount", DMAP_TYPE_UINT),
    "minm": ("dmap.itemname", DMAP_TYPE_STRING),
    "mlcl": ("dmap.listing", DMAP_TYPE_LIST),
    "mlid": ("dmap.sessionid", DMAP_TYPE_UINT),
    "mlit": ("dmap.listingitem", DMAP_TYPE_LIST),
    "mlog": ("dmap.loginresponse", DMAP_TYPE_LIST),
    "mpco": ("dmap.parentcontainerid", DMAP_TYPE_UINT),
    "mper": ("dmap.persistentid", DMAP_TYPE_ULONG),
    "mpro": ("dmap.protocolversion", DMAP_TYPE_VERSION),
    "mrco": ("dmap.returnedcount", DMAP_TYPE_UINT),
    "msal": ("dmap.supportsautologout", DMAP_TYPE_UBYTE),
    "msas": ("dmap.authenticationschemes", DMAP_TYPE_UINT),
    "msau": ("dmap.authenticationmethod", DMAP_TYPE_UBYTE),
    "msbr": ("dmap.supportsbrowse", DMAP_TYPE_UBYTE),
    "msdc": ("dmap.databasescount", DMAP_TYPE_UINT),
    "mshl": ("dmap.sortingheaderlisting", DMAP_TYPE_UINT),
    "mshc": ("dmap.sortingheaderchar", DMAP_TYPE_SHORT),
    "mshi": ("dmap.sortingheaderindex", DMAP_TYPE_UINT),
    "mshn": ("dmap.sortingheadernumber", DMAP_TYPE_UINT),
    "msex": ("dmap.supportsextensions", DMAP_TYPE_UBYTE),
    "msix": ("dmap.supportsindex", DMAP_TYPE_UBYTE),
    "mslr": ("dmap.loginrequired", DMAP_TYPE_UBYTE),
    "mspi": ("dmap.supportspersistentids", DMAP_TYPE_UBYTE),
    "msqy": ("dmap.supportsquery", DMAP_TYPE_UBYTE),
    "msrs": ("dmap.supportsresolve", DMAP_TYPE_UBYTE),
    "msrv": ("dmap.serverinforesponse", DMAP_TYPE_LIST),
#   "mstc": ("dmap.utctime", DMAP_TYPE_DATE),
    "mstm": ("dmap.timeoutinterval", DMAP_TYPE_UINT),
#   "msto": ("dmap.utcoffset", DMAP_TYPE_INT),
    "msts": ("dmap.statusstring", DMAP_TYPE_STRING),
    "mstt": ("dmap.status", DMAP_TYPE_UINT),
    "msup": ("dmap.supportsupdate", DMAP_TYPE_UBYTE),
    "mtco": ("dmap.specifiedtotalcount", DMAP_TYPE_UINT),
    "mudl": ("dmap.deletedidlisting", DMAP_TYPE_LIST),
    "mupd": ("dmap.updateresponse", DMAP_TYPE_LIST),
    "musr": ("dmap.serverrevision", DMAP_TYPE_UINT),
    "muty": ("dmap.updatetype", DMAP_TYPE_UBYTE),
}

dmap_consts_rmap = {
    "daap.browsealbumlisting": "abal",
    "daap.browseartistlisting": "abar",
    "daap.browsecomposerlisting": "abcp",
    "daap.browsegenrelisting": "abgn",
    "daap.baseplaylist": "abpl",
    "daap.databasebrowse": "abro",
    "daap.databasesongs": "adbs",
#   "com.apple.itunes.adam-ids-array": "aeAD",
    "com.apple.itunes.itms-artistid": "aeAI",
    "com.apple.itunes.itms-composerid": "aeCI",
#   "com.apple.itunes.content-rating": "aeCR",
#   "com.apple.itunes.drm-platform-id": "aeDP",
#   "com.apple.itunes.drm-user-id": "aeDR",
#   "com.apple.itunes.drm-versions": "aeDV",
    "com.apple.itunes.episode-num-str": "aeEN",
    "com.apple.itunes.episode-sort": "aeES",
#   "com.apple.itunes.gapless-enc-dr": "aeGD",
#   "com.apple.itunes.gapless-enc-del": "aeGE",
#   "com.apple.itunes.gapless-heur": "aeGH",
    "com.apple.itunes.itms-genreid": "aeGI",
#   "com.apple.itunes.gapless-resy": "aeGR",
#   "com.apple.itunes.gapless-dur": "aeGU",
#   "com.apple.itunes.is-hd-video": "aeHD",
    "com.apple.itunes.has-video": "aeHV",
#   "com.apple.itunes.drm-key1-id": "aeK1",
#   "com.apple.itunes.drm-key2-id": "aeK2",
    "com.apple.itunes.extended-media-kind": "aeMk",
    "com.apple.itunes.mediakind": "aeMK",
#   "com.apple.itunes.non-drm-user-id": "aeND",
    "com.apple.itunes.network-name": "aeNN",
    "com.apple.itunes.norm-volume": "aeNV",
    "com.apple.itunes.is-podcast": "aePC",
    "com.apple.itunes.itms-playlistid": "aePI",
    "com.apple.itunes.is-podcast-playlist": "aePP",
    "com.apple.itunes.special-playlist": "aePS",
#   "com.apple.itunes.store-pers-id": "aeSE",
    "com.apple.itunes.itms-storefrontid": "aeSF",
#   "com.apple.itunes.saved-genius": "aeSG",
    "com.apple.itunes.itms-songid": "aeSI",
    "com.apple.itunes.series-name": "aeSN",
    "com.apple.itunes.smart-playlist": "aeSP",
    "com.apple.itunes.season-num": "aeSU",
    "com.apple.itunes.music-sharing-version": "aeSV",
#   "com.apple.itunes.xid": "aeXD",
    "daap.songgrouping": "agrp",
    "daap.databaseplaylists": "aply",
    "daap.playlistrepeatmode": "aprm",
    "daap.protocolversion": "apro",
    "daap.playlistshufflemode": "apsm",
    "daap.playlistsongs": "apso",
    "daap.resolveinfo": "arif",
    "daap.resolve": "arsv",
    "daap.songalbumartist": "asaa",
    "daap.songalbumid": "asai",
    "daap.songalbum": "asal",
    "daap.songartist": "asar",
#   "daap.bookmarkable": "asbk",
#   "daap.songbookmark": "asbo",
    "daap.songbitrate": "asbr",
    "daap.songbeatsperminute": "asbt",
    "daap.songcodectype": "ascd",
    "daap.songcomment": "ascm",
    "daap.songcontentdescription": "ascn",
    "daap.songcompilation": "asco",
    "daap.songcomposer": "ascp",
    "daap.songcontentrating": "ascr",
    "daap.songcodecsubtype": "ascs",
    "daap.songcategory": "asct",
    "daap.songdateadded": "asda",
    "daap.songdisabled": "asdb",
    "daap.songdisccount": "asdc",
    "daap.songdatakind": "asdk",
    "daap.songdatemodified": "asdm",
    "daap.songdiscnumber": "asdn",
#   "daap.songdatepurchased": "asdp",
#   "daap.songdatereleased": "asdr",
    "daap.songdescription": "asdt",
#   "daap.songextradata": "ased",
    "daap.songeqpreset": "aseq",
    "daap.songformat": "asfm",
    "daap.songgenre": "asgn",
#   "daap.songgapless": "asgp",
#   "daap.songhasbeenplayed": "ashp",
    "daap.songkeywords": "asky",
    "daap.songlongcontentdescription": "aslc",
#   "daap.songlongsize": "asls",
#   "daap.songpodcasturl": "aspu",
    "daap.songrelativevolume": "asrv",
#   "daap.sortartist": "assa",
#   "daap.sortcomposer": "assc",
#   "daap.sortalbumartist": "assl",
#   "daap.sortname": "assn",
    "daap.songstoptime": "assp",
    "daap.songsamplerate": "assr",
#   "daap.sortseriesname": "asss",
    "daap.songstarttime": "asst",
#   "daap.sortalbum": "assu",
    "daap.songsize": "assz",
    "daap.songtrackcount": "astc",
    "daap.songtime": "astm",
    "daap.songtracknumber": "astn",
    "daap.songdataurl": "asul",
    "daap.songuserrating": "asur",
    "daap.songyear": "asyr",
#   "daap.supportsextradata": "ated",
    "daap.serverdatabases": "avdb",
#   "com.apple.itunes.jukebox-client-vote": "ceJC",
#   "com.apple.itunes.jukebox-current": "ceJI",
#   "com.apple.itunes.jukebox-score": "ceJS",
#   "com.apple.itunes.jukebox-vote": "ceJV",
    "dmap.bag": "mbcl",
    "dmap.contentcodesresponse": "mccr",
    "dmap.contentcodesname": "mcna",
    "dmap.contentcodesnumber": "mcnm",
    "dmap.container": "mcon",
    "dmap.containercount": "mctc",
    "dmap.containeritemid": "mcti",
    "dmap.contentcodestype": "mcty",
    "dmap.dictionary": "mdcl",
#   "dmap.editcommandssupported": "meds",
    "dmap.itemid": "miid",
    "dmap.itemkind": "mikd",
    "dmap.itemcount": "mimc",
    "dmap.itemname": "minm",
    "dmap.listing": "mlcl",
    "dmap.sessionid": "mlid",
    "dmap.listingitem": "mlit",
    "dmap.loginresponse": "mlog",
    "dmap.parentcontainerid": "mpco",
    "dmap.persistentid": "mper",
    "dmap.protocolversion": "mpro",
    "dmap.returnedcount": "mrco",
    "dmap.supportsautologout": "msal",
    "dmap.authenticationschemes": "msas",
    "dmap.authenticationmethod": "msau",
    "dmap.supportsbrowse": "msbr",
    "dmap.databasescount": "msdc",
    "dmap.sortingheaderlisting": "mshl",
    "dmap.sortingheaderchar": "mshc",
    "dmap.sortingheaderindex": "mshi",
    "dmap.sortingheadernumber": "mshn",
    "dmap.supportsextensions": "msex",
    "dmap.supportsindex": "msix",
    "dmap.loginrequired": "mslr",
    "dmap.supportspersistentids": "mspi",
    "dmap.supportsquery": "msqy",
    "dmap.supportsresolve": "msrs",
    "dmap.serverinforesponse": "msrv",
#   "dmap.utctime": "mstc",
    "dmap.timeoutinterval": "mstm",
#   "dmap.utcoffset": "msto",
    "dmap.statusstring": "msts",
    "dmap.status": "mstt",
    "dmap.supportsupdate": "msup",
    "dmap.specifiedtotalcount": "mtco",
    "dmap.deletedidlisting": "mudl",
    "dmap.updateresponse": "mupd",
    "dmap.serverrevision": "musr",
    "dmap.updatetype": "muty",
}
