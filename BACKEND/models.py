# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Nsqip2008(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.CharField(db_column='ATTEND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.CharField(db_column='ETOH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.CharField(db_column='DNR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus1 = models.CharField(db_column='FNSTATUS1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.CharField(db_column='CPNEUMON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.CharField(db_column='ESOVAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.CharField(db_column='HXMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpci = models.CharField(db_column='PRVPCI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpcs = models.CharField(db_column='PRVPCS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxangina = models.CharField(db_column='HXANGINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.CharField(db_column='HXPVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restpain = models.CharField(db_column='RESTPAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.CharField(db_column='IMPSENS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coma = models.CharField(db_column='COMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hemi = models.CharField(db_column='HEMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxtia = models.CharField(db_column='HXTIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cva = models.CharField(db_column='CVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvano = models.CharField(db_column='CVANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumorcns = models.CharField(db_column='TUMORCNS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quad = models.CharField(db_column='QUAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.CharField(db_column='CHEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    radio = models.CharField(db_column='RADIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(db_column='Pregnancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proper30 = models.CharField(db_column='PrOper30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.TextField(db_column='OTHERCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.TextField(db_column='OTHERCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.TextField(db_column='OTHERCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.TextField(db_column='OTHERCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.TextField(db_column='CONCPT2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.TextField(db_column='CONCPT3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.TextField(db_column='CONCURR10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.CharField(db_column='OPNOTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.CharField(db_column='AIRTRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESurg', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SurgAne', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.CharField(db_column='TYPEINTOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODay', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MortProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MorbProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'NSQIP2008'


class Nsqip2009(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.CharField(db_column='ATTEND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.CharField(db_column='ETOH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.CharField(db_column='DNR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus1 = models.CharField(db_column='FNSTATUS1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.CharField(db_column='CPNEUMON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.CharField(db_column='ESOVAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.CharField(db_column='HXMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpci = models.CharField(db_column='PRVPCI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpcs = models.CharField(db_column='PRVPCS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxangina = models.CharField(db_column='HXANGINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.CharField(db_column='HXPVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restpain = models.CharField(db_column='RESTPAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.CharField(db_column='IMPSENS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coma = models.CharField(db_column='COMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hemi = models.CharField(db_column='HEMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxtia = models.CharField(db_column='HXTIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cva = models.CharField(db_column='CVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvano = models.CharField(db_column='CVANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumorcns = models.CharField(db_column='TUMORCNS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quad = models.CharField(db_column='QUAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.CharField(db_column='CHEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    radio = models.CharField(db_column='RADIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(db_column='Pregnancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proper30 = models.CharField(db_column='PrOper30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.TextField(db_column='OTHERCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.TextField(db_column='OTHERCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.TextField(db_column='CONCPT2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.TextField(db_column='CONCPT3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.TextField(db_column='CONCURR10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.IntegerField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase.
    opnote = models.CharField(db_column='OPNOTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.CharField(db_column='AIRTRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MortProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MorbProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANEsurg', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SurgAne', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.CharField(db_column='TYPEINTOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODAY', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODAY', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2009'


class Nsqip2010(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.CharField(db_column='ATTEND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.CharField(db_column='ETOH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.CharField(db_column='DNR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus1 = models.TextField(db_column='FNSTATUS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.CharField(db_column='CPNEUMON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.CharField(db_column='ESOVAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.CharField(db_column='HXMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpci = models.CharField(db_column='PRVPCI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpcs = models.CharField(db_column='PRVPCS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxangina = models.CharField(db_column='HXANGINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.CharField(db_column='HXPVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restpain = models.CharField(db_column='RESTPAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.CharField(db_column='IMPSENS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coma = models.CharField(db_column='COMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hemi = models.CharField(db_column='HEMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxtia = models.CharField(db_column='HXTIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cva = models.CharField(db_column='CVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvano = models.CharField(db_column='CVANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumorcns = models.CharField(db_column='TUMORCNS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quad = models.CharField(db_column='QUAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.CharField(db_column='CHEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    radio = models.CharField(db_column='RADIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(db_column='Pregnancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proper30 = models.CharField(db_column='PrOper30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.TextField(db_column='OTHERCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.TextField(db_column='OTHERCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.CharField(db_column='CONCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.CharField(db_column='CONCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.CharField(db_column='CONCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.TextField(db_column='OPNOTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.TextField(db_column='AIRTRA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MortProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MorbProb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESurg', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SurgAne', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.CharField(db_column='TYPEINTOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODAY', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODay', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2010'


class Nsqip2011(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.CharField(db_column='ATTEND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.CharField(db_column='ETOH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.CharField(db_column='DNR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus1 = models.TextField(db_column='FNSTATUS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.CharField(db_column='CPNEUMON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.CharField(db_column='ESOVAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.CharField(db_column='HXMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpci = models.CharField(db_column='PRVPCI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpcs = models.CharField(db_column='PRVPCS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxangina = models.CharField(db_column='HXANGINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.CharField(db_column='HXPVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restpain = models.CharField(db_column='RESTPAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.CharField(db_column='IMPSENS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coma = models.CharField(db_column='COMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hemi = models.CharField(db_column='HEMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxtia = models.CharField(db_column='HXTIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cva = models.CharField(db_column='CVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvano = models.CharField(db_column='CVANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumorcns = models.CharField(db_column='TUMORCNS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quad = models.CharField(db_column='QUAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.CharField(db_column='CHEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    radio = models.CharField(db_column='RADIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(db_column='Pregnancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proper30 = models.CharField(db_column='PrOper30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.CharField(db_column='CONCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.TextField(db_column='OPNOTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.TextField(db_column='AIRTRA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESURG', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SURGANE', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.CharField(db_column='TYPEINTOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODay', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission = models.CharField(db_column='READMISSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unplanreadmission = models.CharField(db_column='UNPLANREADMISSION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation = models.CharField(db_column='REOPERATION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2011'


class Nsqip2012(models.Model):
    caseid = models.IntegerField(db_column='CASEID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='ADMYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='ADMSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OPERYR', blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.CharField(db_column='ATTEND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.CharField(db_column='ETOH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.CharField(db_column='DNR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus1 = models.TextField(db_column='FNSTATUS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.CharField(db_column='CPNEUMON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.CharField(db_column='ESOVAR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.CharField(db_column='HXMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpci = models.CharField(db_column='PRVPCI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prvpcs = models.CharField(db_column='PRVPCS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxangina = models.CharField(db_column='HXANGINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.CharField(db_column='HXPVD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    restpain = models.CharField(db_column='RESTPAIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.CharField(db_column='IMPSENS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coma = models.CharField(db_column='COMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hemi = models.CharField(db_column='HEMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxtia = models.CharField(db_column='HXTIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cva = models.CharField(db_column='CVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvano = models.CharField(db_column='CVANO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumorcns = models.CharField(db_column='TUMORCNS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='PARA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quad = models.CharField(db_column='QUAD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.CharField(db_column='CHEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    radio = models.CharField(db_column='RADIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(db_column='PREGNANCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proper30 = models.CharField(db_column='PROPER30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.TextField(db_column='OPNOTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.TextField(db_column='AIRTRA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESURG', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SURGANE', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.CharField(db_column='TYPEINTOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='ADMQTR', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HTOODAY', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='STOODAY', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDTOHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.TextField(db_column='DOPERTOD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    doptodis = models.IntegerField(db_column='DOPTODIS', blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission = models.TextField(db_column='READMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unplanreadmission = models.TextField(db_column='UNPLANREADMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation = models.TextField(db_column='REOPERATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.CharField(db_column='REOPOR2ICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.CharField(db_column='READMRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.CharField(db_column='READMRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.TextField(db_column='READMRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'NSQIP2012'


class Nsqip2013(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.CharField(db_column='CPT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.TextField(db_column='ATTEND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.TextField(db_column='ETOH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.TextField(db_column='DNR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus1 = models.TextField(db_column='FNSTATUS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.TextField(db_column='CPNEUMON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.TextField(db_column='ESOVAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.TextField(db_column='HXMI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prvpci = models.TextField(db_column='PRVPCI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prvpcs = models.TextField(db_column='PRVPCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxangina = models.TextField(db_column='HXANGINA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.TextField(db_column='HXPVD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restpain = models.TextField(db_column='RESTPAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.TextField(db_column='IMPSENS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coma = models.TextField(db_column='COMA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hemi = models.TextField(db_column='HEMI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxtia = models.TextField(db_column='HXTIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cva = models.TextField(db_column='CVA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cvano = models.TextField(db_column='CVANO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tumorcns = models.TextField(db_column='TUMORCNS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    para = models.TextField(db_column='Para', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quad = models.TextField(db_column='QUAD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.TextField(db_column='CHEMO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    radio = models.TextField(db_column='RADIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.TextField(db_column='Pregnancy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proper30 = models.TextField(db_column='PrOper30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.IntegerField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.CharField(db_column='CONCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.CharField(db_column='CONCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.TextField(db_column='OPNOTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.TextField(db_column='AIRTRA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESURG', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SURGANE', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.TextField(db_column='TYPEINTOC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODay', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.CharField(db_column='CNSCOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.CharField(db_column='NEURODEF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.CharField(db_column='OTHGRAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission = models.TextField(db_column='READMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unplanreadmission = models.TextField(db_column='UNPLANREADMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation = models.TextField(db_column='REOPERATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.CharField(db_column='REOPOR2ICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.CharField(db_column='READMRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.CharField(db_column='READMUNRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.CharField(db_column='READMUNRELSUSP2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.CharField(db_column='READMRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.CharField(db_column='READMUNRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.CharField(db_column='READMUNRELSUSP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.CharField(db_column='READMRELICD93', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.CharField(db_column='READMUNRELSUSP4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.TextField(db_column='READMUNRELSUSP5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'NSQIP2013'


class Nsqip2014(models.Model):
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.IntegerField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    admsyr = models.IntegerField(db_column='AdmSYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attend = models.TextField(db_column='ATTEND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packs = models.IntegerField(db_column='PACKS', blank=True, null=True)  # Field name made lowercase.
    etoh = models.TextField(db_column='ETOH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnr = models.TextField(db_column='DNR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus1 = models.TextField(db_column='FNSTATUS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpneumon = models.TextField(db_column='CPNEUMON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esovar = models.TextField(db_column='ESOVAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxmi = models.TextField(db_column='HXMI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prvpci = models.TextField(db_column='PRVPCI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prvpcs = models.TextField(db_column='PRVPCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxangina = models.TextField(db_column='HXANGINA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxpvd = models.TextField(db_column='HXPVD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restpain = models.TextField(db_column='RESTPAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impsens = models.TextField(db_column='IMPSENS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coma = models.TextField(db_column='COMA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hemi = models.TextField(db_column='HEMI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hxtia = models.TextField(db_column='HXTIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cva = models.TextField(db_column='CVA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cvano = models.TextField(db_column='CVANO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tumorcns = models.TextField(db_column='TUMORCNS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    para = models.TextField(db_column='Para', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quad = models.TextField(db_column='QUAD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chemo = models.TextField(db_column='CHEMO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    radio = models.TextField(db_column='RADIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.TextField(db_column='Pregnancy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proper30 = models.TextField(db_column='PrOper30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opnote = models.TextField(db_column='OPNOTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pgy = models.IntegerField(db_column='PGY', blank=True, null=True)  # Field name made lowercase.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtra = models.TextField(db_column='AIRTRA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mallamp = models.IntegerField(db_column='MALLAMP', blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rbc = models.IntegerField(db_column='RBC', blank=True, null=True)  # Field name made lowercase.
    anesurg = models.IntegerField(db_column='ANESURG', blank=True, null=True)  # Field name made lowercase.
    surgane = models.IntegerField(db_column='SURGANE', blank=True, null=True)  # Field name made lowercase.
    dpatrm = models.IntegerField(db_column='DPATRM', blank=True, null=True)  # Field name made lowercase.
    anetime = models.IntegerField(db_column='ANETIME', blank=True, null=True)  # Field name made lowercase.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    typeintoc = models.TextField(db_column='TYPEINTOC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sdisdt = models.IntegerField(db_column='SDISDT', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase.
    stooday = models.IntegerField(db_column='StoODay', blank=True, null=True)  # Field name made lowercase.
    totslos = models.IntegerField(db_column='TOTSLOS', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncnscoma = models.IntegerField(db_column='NCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    cnscoma = models.TextField(db_column='CNSCOMA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dcnscoma = models.IntegerField(db_column='DCNSCOMA', blank=True, null=True)  # Field name made lowercase.
    nneurodef = models.IntegerField(db_column='NNEURODEF', blank=True, null=True)  # Field name made lowercase.
    neurodef = models.TextField(db_column='NEURODEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dneurodef = models.IntegerField(db_column='DNEURODEF', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothgrafl = models.IntegerField(db_column='NOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    othgrafl = models.TextField(db_column='OTHGRAFL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dothgrafl = models.IntegerField(db_column='DOTHGRAFL', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag10 = models.CharField(db_column='PODIAG10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx10 = models.CharField(db_column='PODIAGTX10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsdtohd = models.IntegerField(db_column='DSDtoHD', blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission = models.TextField(db_column='READMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unplanreadmission = models.TextField(db_column='UNPLANREADMISSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation = models.TextField(db_column='REOPERATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor1icd101 = models.CharField(db_column='REOPOR1ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.CharField(db_column='REOPOR2ICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd101 = models.TextField(db_column='REOPOR2ICD101', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.CharField(db_column='READMRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd101 = models.CharField(db_column='READMRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.CharField(db_column='READMUNRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd101 = models.CharField(db_column='READMUNRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.CharField(db_column='READMUNRELSUSP2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.CharField(db_column='READMRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd102 = models.CharField(db_column='READMRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.CharField(db_column='READMUNRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd102 = models.CharField(db_column='READMUNRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.CharField(db_column='READMUNRELSUSP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.CharField(db_column='READMRELICD93', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd103 = models.CharField(db_column='READMRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd103 = models.TextField(db_column='READMUNRELICD103', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.CharField(db_column='READMUNRELSUSP4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.CharField(db_column='READMRELICD94', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd104 = models.TextField(db_column='READMRELICD104', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd104 = models.TextField(db_column='READMUNRELICD104', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.TextField(db_column='READMUNRELSUSP5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd95 = models.CharField(db_column='READMRELICD95', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd105 = models.TextField(db_column='READMRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd105 = models.TextField(db_column='READMUNRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wound_closure = models.CharField(db_column='WOUND_CLOSURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other = models.CharField(db_column='PODIAG_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other10 = models.CharField(db_column='PODIAG_OTHER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes_other = models.CharField(db_column='ANESTHES_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2014'


class Nsqip2015(models.Model):
    pufyear = models.IntegerField(db_column='PUFYEAR', blank=True, null=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.IntegerField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.TextField(db_column='CONCPT3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.TextField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.TextField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.TextField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag10 = models.CharField(db_column='PODIAG10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx10 = models.CharField(db_column='PODIAGTX10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor1icd101 = models.CharField(db_column='REOPOR1ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.CharField(db_column='REOPOR2ICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd101 = models.CharField(db_column='REOPOR2ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.CharField(db_column='READMRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd101 = models.CharField(db_column='READMRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.CharField(db_column='READMUNRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd101 = models.CharField(db_column='READMUNRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.CharField(db_column='READMUNRELSUSP2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.CharField(db_column='READMRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd102 = models.CharField(db_column='READMRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.CharField(db_column='READMUNRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd102 = models.CharField(db_column='READMUNRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.CharField(db_column='READMUNRELSUSP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.TextField(db_column='READMRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd103 = models.CharField(db_column='READMRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd103 = models.CharField(db_column='READMUNRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.CharField(db_column='READMUNRELSUSP4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd104 = models.CharField(db_column='READMRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd104 = models.CharField(db_column='READMUNRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.CharField(db_column='READMUNRELSUSP5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd105 = models.TextField(db_column='READMRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd105 = models.CharField(db_column='READMUNRELICD105', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wound_closure = models.CharField(db_column='WOUND_CLOSURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other = models.CharField(db_column='PODIAG_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other10 = models.CharField(db_column='PODIAG_OTHER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes_other = models.CharField(db_column='ANESTHES_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othcdiff = models.CharField(db_column='OTHCDIFF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nothcdiff = models.IntegerField(db_column='NOTHCDIFF', blank=True, null=True)  # Field name made lowercase.
    dothcdiff = models.IntegerField(db_column='DOTHCDIFF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2015'


class Nsqip2016(models.Model):
    pufyear = models.IntegerField(db_column='PUFYEAR', blank=True, null=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.IntegerField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.TextField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.IntegerField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.TextField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.TextField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.CharField(db_column='PODIAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx = models.CharField(db_column='PODIAGTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag10 = models.CharField(db_column='PODIAG10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx10 = models.CharField(db_column='PODIAGTX10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor1icd101 = models.CharField(db_column='REOPOR1ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.TextField(db_column='REOPOR2CPT1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.TextField(db_column='REOPOR2ICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reopor2icd101 = models.CharField(db_column='REOPOR2ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.CharField(db_column='READMRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd101 = models.CharField(db_column='READMRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.CharField(db_column='READMUNRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd101 = models.CharField(db_column='READMUNRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.CharField(db_column='READMUNRELSUSP2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.CharField(db_column='READMRELICD92', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd102 = models.CharField(db_column='READMRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.TextField(db_column='READMUNRELICD92', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd102 = models.CharField(db_column='READMUNRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.CharField(db_column='READMUNRELSUSP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.TextField(db_column='READMRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd103 = models.CharField(db_column='READMRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd103 = models.CharField(db_column='READMUNRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.CharField(db_column='READMUNRELSUSP4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd104 = models.CharField(db_column='READMRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd104 = models.CharField(db_column='READMUNRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.TextField(db_column='READMUNRELSUSP5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd105 = models.CharField(db_column='READMRELICD105', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd105 = models.TextField(db_column='READMUNRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wound_closure = models.CharField(db_column='WOUND_CLOSURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other = models.CharField(db_column='PODIAG_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other10 = models.CharField(db_column='PODIAG_OTHER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes_other = models.CharField(db_column='ANESTHES_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othcdiff = models.CharField(db_column='OTHCDIFF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nothcdiff = models.IntegerField(db_column='NOTHCDIFF', blank=True, null=True)  # Field name made lowercase.
    dothcdiff = models.IntegerField(db_column='DOTHCDIFF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2016'


class Nsqip2017(models.Model):
    pufyear = models.IntegerField(db_column='PUFYEAR', blank=True, null=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.IntegerField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.IntegerField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.CharField(db_column='OTHERCPT10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.TextField(db_column='CONCPT4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.CharField(db_column='CONCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.TextField(db_column='CONCPT6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.TextField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.TextField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.TextField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.TextField(db_column='PODIAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    podiagtx = models.TextField(db_column='PODIAGTX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    podiag10 = models.CharField(db_column='PODIAG10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx10 = models.CharField(db_column='PODIAGTX10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.CharField(db_column='REOPORICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor1icd101 = models.CharField(db_column='REOPOR1ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.TextField(db_column='REOPOR2ICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reopor2icd101 = models.CharField(db_column='REOPOR2ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.TextField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.TextField(db_column='READMRELICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd101 = models.CharField(db_column='READMRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.CharField(db_column='READMUNRELICD91', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd101 = models.CharField(db_column='READMUNRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.CharField(db_column='READMUNRELSUSP2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd92 = models.TextField(db_column='READMRELICD92', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd102 = models.CharField(db_column='READMRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.TextField(db_column='READMUNRELICD92', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd102 = models.CharField(db_column='READMUNRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.CharField(db_column='READMUNRELSUSP3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd93 = models.TextField(db_column='READMRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd103 = models.CharField(db_column='READMRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd103 = models.CharField(db_column='READMUNRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.CharField(db_column='READMUNRELSUSP4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd104 = models.CharField(db_column='READMRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd104 = models.CharField(db_column='READMUNRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.TextField(db_column='READMUNRELSUSP5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd105 = models.CharField(db_column='READMRELICD105', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd105 = models.TextField(db_column='READMUNRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wound_closure = models.CharField(db_column='WOUND_CLOSURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other = models.CharField(db_column='PODIAG_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other10 = models.CharField(db_column='PODIAG_OTHER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes_other = models.CharField(db_column='ANESTHES_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othcdiff = models.CharField(db_column='OTHCDIFF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nothcdiff = models.IntegerField(db_column='NOTHCDIFF', blank=True, null=True)  # Field name made lowercase.
    dothcdiff = models.IntegerField(db_column='DOTHCDIFF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2017'


class Nsqip2018(models.Model):
    pufyear = models.IntegerField(db_column='PUFYEAR', blank=True, null=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race_new = models.CharField(db_column='RACE_NEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity_hispanic = models.CharField(db_column='ETHNICITY_HISPANIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prncptx = models.CharField(db_column='PRNCPTX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpt = models.IntegerField(db_column='CPT', blank=True, null=True)  # Field name made lowercase.
    workrvu = models.TextField(db_column='WORKRVU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inout = models.CharField(db_column='INOUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transt = models.CharField(db_column='TRANST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admyr = models.IntegerField(db_column='AdmYR', blank=True, null=True)  # Field name made lowercase.
    operyr = models.IntegerField(db_column='OperYR', blank=True, null=True)  # Field name made lowercase.
    dischdest = models.CharField(db_column='DISCHDEST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes = models.CharField(db_column='ANESTHES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgspec = models.CharField(db_column='SURGSPEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electsurg = models.CharField(db_column='ELECTSURG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.CharField(db_column='DIABETES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dyspnea = models.CharField(db_column='DYSPNEA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fnstatus2 = models.CharField(db_column='FNSTATUS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventilat = models.CharField(db_column='VENTILAT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxcopd = models.CharField(db_column='HXCOPD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ascites = models.CharField(db_column='ASCITES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hxchf = models.CharField(db_column='HXCHF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hypermed = models.CharField(db_column='HYPERMED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    renafail = models.CharField(db_column='RENAFAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dialysis = models.CharField(db_column='DIALYSIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discancr = models.CharField(db_column='DISCANCR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndinf = models.CharField(db_column='WNDINF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    steroid = models.CharField(db_column='STEROID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wtloss = models.CharField(db_column='WTLOSS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bleeddis = models.CharField(db_column='BLEEDDIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfus = models.CharField(db_column='TRANSFUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prsepis = models.CharField(db_column='PRSEPIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dprna = models.IntegerField(db_column='DPRNA', blank=True, null=True)  # Field name made lowercase.
    dprbun = models.IntegerField(db_column='DPRBUN', blank=True, null=True)  # Field name made lowercase.
    dprcreat = models.IntegerField(db_column='DPRCREAT', blank=True, null=True)  # Field name made lowercase.
    dpralbum = models.IntegerField(db_column='DPRALBUM', blank=True, null=True)  # Field name made lowercase.
    dprbili = models.IntegerField(db_column='DPRBILI', blank=True, null=True)  # Field name made lowercase.
    dprsgot = models.IntegerField(db_column='DPRSGOT', blank=True, null=True)  # Field name made lowercase.
    dpralkph = models.IntegerField(db_column='DPRALKPH', blank=True, null=True)  # Field name made lowercase.
    dprwbc = models.IntegerField(db_column='DPRWBC', blank=True, null=True)  # Field name made lowercase.
    dprhct = models.IntegerField(db_column='DPRHCT', blank=True, null=True)  # Field name made lowercase.
    dprplate = models.IntegerField(db_column='DPRPLATE', blank=True, null=True)  # Field name made lowercase.
    dprptt = models.IntegerField(db_column='DPRPTT', blank=True, null=True)  # Field name made lowercase.
    dprpt = models.IntegerField(db_column='DPRPT', blank=True, null=True)  # Field name made lowercase.
    dprinr = models.IntegerField(db_column='DPRINR', blank=True, null=True)  # Field name made lowercase.
    prsodm = models.TextField(db_column='PRSODM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbun = models.TextField(db_column='PRBUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prcreat = models.TextField(db_column='PRCREAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralbum = models.TextField(db_column='PRALBUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prbili = models.TextField(db_column='PRBILI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prsgot = models.TextField(db_column='PRSGOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pralkph = models.TextField(db_column='PRALKPH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prwbc = models.TextField(db_column='PRWBC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prhct = models.TextField(db_column='PRHCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prplate = models.TextField(db_column='PRPLATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prptt = models.TextField(db_column='PRPTT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prinr = models.TextField(db_column='PRINR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prpt = models.IntegerField(db_column='PRPT', blank=True, null=True)  # Field name made lowercase.
    otherproc1 = models.CharField(db_column='OTHERPROC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt1 = models.CharField(db_column='OTHERCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu1 = models.TextField(db_column='OTHERWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc2 = models.CharField(db_column='OTHERPROC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt2 = models.CharField(db_column='OTHERCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu2 = models.TextField(db_column='OTHERWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc3 = models.CharField(db_column='OTHERPROC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt3 = models.CharField(db_column='OTHERCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu3 = models.TextField(db_column='OTHERWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc4 = models.CharField(db_column='OTHERPROC4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt4 = models.CharField(db_column='OTHERCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu4 = models.TextField(db_column='OTHERWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc5 = models.CharField(db_column='OTHERPROC5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt5 = models.CharField(db_column='OTHERCPT5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu5 = models.TextField(db_column='OTHERWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc6 = models.CharField(db_column='OTHERPROC6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt6 = models.CharField(db_column='OTHERCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu6 = models.TextField(db_column='OTHERWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc7 = models.CharField(db_column='OTHERPROC7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt7 = models.CharField(db_column='OTHERCPT7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu7 = models.TextField(db_column='OTHERWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc8 = models.CharField(db_column='OTHERPROC8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt8 = models.CharField(db_column='OTHERCPT8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu8 = models.TextField(db_column='OTHERWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc9 = models.CharField(db_column='OTHERPROC9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt9 = models.CharField(db_column='OTHERCPT9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherwrvu9 = models.TextField(db_column='OTHERWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherproc10 = models.CharField(db_column='OTHERPROC10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercpt10 = models.TextField(db_column='OTHERCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherwrvu10 = models.TextField(db_column='OTHERWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr1 = models.CharField(db_column='CONCURR1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt1 = models.CharField(db_column='CONCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu1 = models.TextField(db_column='CONWRVU1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr2 = models.CharField(db_column='CONCURR2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt2 = models.CharField(db_column='CONCPT2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu2 = models.TextField(db_column='CONWRVU2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr3 = models.CharField(db_column='CONCURR3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt3 = models.CharField(db_column='CONCPT3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu3 = models.TextField(db_column='CONWRVU3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr4 = models.CharField(db_column='CONCURR4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt4 = models.CharField(db_column='CONCPT4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu4 = models.TextField(db_column='CONWRVU4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr5 = models.CharField(db_column='CONCURR5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt5 = models.TextField(db_column='CONCPT5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu5 = models.TextField(db_column='CONWRVU5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr6 = models.CharField(db_column='CONCURR6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt6 = models.CharField(db_column='CONCPT6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conwrvu6 = models.TextField(db_column='CONWRVU6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr7 = models.CharField(db_column='CONCURR7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt7 = models.TextField(db_column='CONCPT7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu7 = models.TextField(db_column='CONWRVU7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr8 = models.CharField(db_column='CONCURR8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt8 = models.TextField(db_column='CONCPT8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu8 = models.TextField(db_column='CONWRVU8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr9 = models.CharField(db_column='CONCURR9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt9 = models.TextField(db_column='CONCPT9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu9 = models.TextField(db_column='CONWRVU9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    concurr10 = models.CharField(db_column='CONCURR10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concpt10 = models.TextField(db_column='CONCPT10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conwrvu10 = models.TextField(db_column='CONWRVU10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emergncy = models.CharField(db_column='EMERGNCY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wndclas = models.CharField(db_column='WNDCLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asaclas = models.CharField(db_column='ASACLAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mortprob = models.TextField(db_column='MORTPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    morbprob = models.TextField(db_column='MORBPROB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.IntegerField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase.
    hdisdt = models.IntegerField(db_column='HDISDT', blank=True, null=True)  # Field name made lowercase.
    yrdeath = models.IntegerField(db_column='YRDEATH', blank=True, null=True)  # Field name made lowercase.
    tothlos = models.IntegerField(db_column='TOTHLOS', blank=True, null=True)  # Field name made lowercase.
    admqtr = models.IntegerField(db_column='AdmQtr', blank=True, null=True)  # Field name made lowercase.
    htooday = models.TextField(db_column='HtoODay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nsupinfec = models.IntegerField(db_column='NSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    supinfec = models.CharField(db_column='SUPINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sssipatos = models.CharField(db_column='SSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsupinfec = models.IntegerField(db_column='DSUPINFEC', blank=True, null=True)  # Field name made lowercase.
    nwndinfd = models.IntegerField(db_column='NWNDINFD', blank=True, null=True)  # Field name made lowercase.
    wndinfd = models.CharField(db_column='WNDINFD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dssipatos = models.CharField(db_column='DSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwndinfd = models.IntegerField(db_column='DWNDINFD', blank=True, null=True)  # Field name made lowercase.
    norgspcssi = models.IntegerField(db_column='NORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    orgspcssi = models.CharField(db_column='ORGSPCSSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ossipatos = models.CharField(db_column='OSSIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dorgspcssi = models.IntegerField(db_column='DORGSPCSSI', blank=True, null=True)  # Field name made lowercase.
    ndehis = models.IntegerField(db_column='NDEHIS', blank=True, null=True)  # Field name made lowercase.
    dehis = models.CharField(db_column='DEHIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddehis = models.IntegerField(db_column='DDEHIS', blank=True, null=True)  # Field name made lowercase.
    noupneumo = models.IntegerField(db_column='NOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    oupneumo = models.CharField(db_column='OUPNEUMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pnapatos = models.CharField(db_column='PNAPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doupneumo = models.IntegerField(db_column='DOUPNEUMO', blank=True, null=True)  # Field name made lowercase.
    nreintub = models.IntegerField(db_column='NREINTUB', blank=True, null=True)  # Field name made lowercase.
    reintub = models.CharField(db_column='REINTUB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dreintub = models.IntegerField(db_column='DREINTUB', blank=True, null=True)  # Field name made lowercase.
    npulembol = models.IntegerField(db_column='NPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    pulembol = models.CharField(db_column='PULEMBOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dpulembol = models.IntegerField(db_column='DPULEMBOL', blank=True, null=True)  # Field name made lowercase.
    nfailwean = models.IntegerField(db_column='NFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    failwean = models.CharField(db_column='FAILWEAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ventpatos = models.CharField(db_column='VENTPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dfailwean = models.IntegerField(db_column='DFAILWEAN', blank=True, null=True)  # Field name made lowercase.
    nrenainsf = models.IntegerField(db_column='NRENAINSF', blank=True, null=True)  # Field name made lowercase.
    renainsf = models.CharField(db_column='RENAINSF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drenainsf = models.IntegerField(db_column='DRENAINSF', blank=True, null=True)  # Field name made lowercase.
    noprenafl = models.IntegerField(db_column='NOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    oprenafl = models.CharField(db_column='OPRENAFL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doprenafl = models.IntegerField(db_column='DOPRENAFL', blank=True, null=True)  # Field name made lowercase.
    nurninfec = models.IntegerField(db_column='NURNINFEC', blank=True, null=True)  # Field name made lowercase.
    urninfec = models.CharField(db_column='URNINFEC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utipatos = models.CharField(db_column='UTIPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durninfec = models.IntegerField(db_column='DURNINFEC', blank=True, null=True)  # Field name made lowercase.
    ncnscva = models.IntegerField(db_column='NCNSCVA', blank=True, null=True)  # Field name made lowercase.
    cnscva = models.CharField(db_column='CNSCVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcnscva = models.IntegerField(db_column='DCNSCVA', blank=True, null=True)  # Field name made lowercase.
    ncdarrest = models.IntegerField(db_column='NCDARREST', blank=True, null=True)  # Field name made lowercase.
    cdarrest = models.CharField(db_column='CDARREST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdarrest = models.IntegerField(db_column='DCDARREST', blank=True, null=True)  # Field name made lowercase.
    ncdmi = models.IntegerField(db_column='NCDMI', blank=True, null=True)  # Field name made lowercase.
    cdmi = models.CharField(db_column='CDMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dcdmi = models.IntegerField(db_column='DCDMI', blank=True, null=True)  # Field name made lowercase.
    nothbleed = models.IntegerField(db_column='NOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    othbleed = models.CharField(db_column='OTHBLEED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothbleed = models.IntegerField(db_column='DOTHBLEED', blank=True, null=True)  # Field name made lowercase.
    nothdvt = models.IntegerField(db_column='NOTHDVT', blank=True, null=True)  # Field name made lowercase.
    othdvt = models.CharField(db_column='OTHDVT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothdvt = models.IntegerField(db_column='DOTHDVT', blank=True, null=True)  # Field name made lowercase.
    nothsysep = models.IntegerField(db_column='NOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    othsysep = models.CharField(db_column='OTHSYSEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepsispatos = models.CharField(db_column='SEPSISPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothsysep = models.IntegerField(db_column='DOTHSYSEP', blank=True, null=True)  # Field name made lowercase.
    nothseshock = models.IntegerField(db_column='NOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    othseshock = models.CharField(db_column='OTHSESHOCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sepshockpatos = models.CharField(db_column='SEPSHOCKPATOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dothseshock = models.IntegerField(db_column='DOTHSESHOCK', blank=True, null=True)  # Field name made lowercase.
    podiag = models.TextField(db_column='PODIAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    podiagtx = models.TextField(db_column='PODIAGTX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    podiag10 = models.CharField(db_column='PODIAG10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiagtx10 = models.CharField(db_column='PODIAGTX10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    returnor = models.CharField(db_column='RETURNOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dopertod = models.IntegerField(db_column='DOpertoD', blank=True, null=True)  # Field name made lowercase.
    doptodis = models.IntegerField(db_column='DOptoDis', blank=True, null=True)  # Field name made lowercase.
    stillinhosp = models.CharField(db_column='STILLINHOSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation1 = models.CharField(db_column='REOPERATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorpodays = models.IntegerField(db_column='RETORPODAYS', blank=True, null=True)  # Field name made lowercase.
    reoporcpt1 = models.CharField(db_column='REOPORCPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retorrelated = models.CharField(db_column='RETORRELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoporicd91 = models.TextField(db_column='REOPORICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reopor1icd101 = models.CharField(db_column='REOPOR1ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation2 = models.CharField(db_column='REOPERATION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2podays = models.IntegerField(db_column='RETOR2PODAYS', blank=True, null=True)  # Field name made lowercase.
    reopor2cpt1 = models.CharField(db_column='REOPOR2CPT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retor2related = models.CharField(db_column='RETOR2RELATED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reopor2icd91 = models.TextField(db_column='REOPOR2ICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reopor2icd101 = models.CharField(db_column='REOPOR2ICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reoperation3 = models.CharField(db_column='REOPERATION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission1 = models.CharField(db_column='READMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays1 = models.IntegerField(db_column='READMPODAYS1', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission1 = models.CharField(db_column='UNPLANNEDREADMISSION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated1 = models.CharField(db_column='READMRELATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason1 = models.CharField(db_column='READMSUSPREASON1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp1 = models.CharField(db_column='READMUNRELSUSP1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelicd91 = models.TextField(db_column='READMRELICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd101 = models.CharField(db_column='READMRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd91 = models.TextField(db_column='READMUNRELICD91', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd101 = models.CharField(db_column='READMUNRELICD101', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmission2 = models.CharField(db_column='READMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays2 = models.IntegerField(db_column='READMPODAYS2', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission2 = models.CharField(db_column='UNPLANNEDREADMISSION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated2 = models.CharField(db_column='READMRELATED2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason2 = models.CharField(db_column='READMSUSPREASON2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp2 = models.TextField(db_column='READMUNRELSUSP2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd92 = models.TextField(db_column='READMRELICD92', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd102 = models.CharField(db_column='READMRELICD102', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd92 = models.TextField(db_column='READMUNRELICD92', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd102 = models.TextField(db_column='READMUNRELICD102', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission3 = models.CharField(db_column='READMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays3 = models.IntegerField(db_column='READMPODAYS3', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission3 = models.CharField(db_column='UNPLANNEDREADMISSION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated3 = models.CharField(db_column='READMRELATED3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason3 = models.CharField(db_column='READMSUSPREASON3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp3 = models.TextField(db_column='READMUNRELSUSP3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd93 = models.TextField(db_column='READMRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd103 = models.CharField(db_column='READMRELICD103', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd93 = models.TextField(db_column='READMUNRELICD93', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd103 = models.TextField(db_column='READMUNRELICD103', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission4 = models.CharField(db_column='READMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays4 = models.IntegerField(db_column='READMPODAYS4', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission4 = models.CharField(db_column='UNPLANNEDREADMISSION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated4 = models.CharField(db_column='READMRELATED4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason4 = models.CharField(db_column='READMSUSPREASON4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp4 = models.TextField(db_column='READMUNRELSUSP4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd94 = models.TextField(db_column='READMRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd104 = models.CharField(db_column='READMRELICD104', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd94 = models.TextField(db_column='READMUNRELICD94', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd104 = models.TextField(db_column='READMUNRELICD104', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmission5 = models.CharField(db_column='READMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmpodays5 = models.IntegerField(db_column='READMPODAYS5', blank=True, null=True)  # Field name made lowercase.
    unplannedreadmission5 = models.CharField(db_column='UNPLANNEDREADMISSION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmrelated5 = models.CharField(db_column='READMRELATED5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmsuspreason5 = models.CharField(db_column='READMSUSPREASON5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelsusp5 = models.TextField(db_column='READMUNRELSUSP5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd95 = models.TextField(db_column='READMRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmrelicd105 = models.CharField(db_column='READMRELICD105', max_length=255, blank=True, null=True)  # Field name made lowercase.
    readmunrelicd95 = models.TextField(db_column='READMUNRELICD95', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    readmunrelicd105 = models.TextField(db_column='READMUNRELICD105', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wound_closure = models.CharField(db_column='WOUND_CLOSURE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    podiag_other = models.TextField(db_column='PODIAG_OTHER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    podiag_other10 = models.CharField(db_column='PODIAG_OTHER10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anesthes_other = models.CharField(db_column='ANESTHES_OTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othcdiff = models.CharField(db_column='OTHCDIFF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nothcdiff = models.IntegerField(db_column='NOTHCDIFF', blank=True, null=True)  # Field name made lowercase.
    dothcdiff = models.IntegerField(db_column='DOTHCDIFF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP2018'


class NsqipMeta(models.Model):
    name = models.TextField(db_column='Name', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NSQIP_META'
