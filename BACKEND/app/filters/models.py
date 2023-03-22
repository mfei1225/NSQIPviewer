# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Nsqip2018(models.Model):
    pufyear = models.IntegerField(blank=True, null=True)
    caseid = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    race_new = models.CharField(max_length=255, blank=True, null=True)
    ethnicity_hispanic = models.CharField(max_length=255, blank=True, null=True)
    prncptx = models.CharField(max_length=255, blank=True, null=True)
    cpt = models.IntegerField(blank=True, null=True)
    workrvu = models.FloatField(blank=True, null=True)
    inout = models.CharField(max_length=255, blank=True, null=True)
    transt = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    admyr = models.IntegerField(blank=True, null=True)
    operyr = models.IntegerField(blank=True, null=True)
    dischdest = models.CharField(max_length=255, blank=True, null=True)
    anesthes = models.CharField(max_length=255, blank=True, null=True)
    surgspec = models.CharField(max_length=255, blank=True, null=True)
    electsurg = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    diabetes = models.CharField(max_length=255, blank=True, null=True)
    smoke = models.CharField(max_length=255, blank=True, null=True)
    dyspnea = models.CharField(max_length=255, blank=True, null=True)
    fnstatus2 = models.CharField(max_length=255, blank=True, null=True)
    ventilat = models.CharField(max_length=255, blank=True, null=True)
    hxcopd = models.CharField(max_length=255, blank=True, null=True)
    ascites = models.CharField(max_length=255, blank=True, null=True)
    hxchf = models.CharField(max_length=255, blank=True, null=True)
    hypermed = models.CharField(max_length=255, blank=True, null=True)
    renafail = models.CharField(max_length=255, blank=True, null=True)
    dialysis = models.CharField(max_length=255, blank=True, null=True)
    discancr = models.CharField(max_length=255, blank=True, null=True)
    wndinf = models.CharField(max_length=255, blank=True, null=True)
    steroid = models.CharField(max_length=255, blank=True, null=True)
    wtloss = models.CharField(max_length=255, blank=True, null=True)
    bleeddis = models.CharField(max_length=255, blank=True, null=True)
    transfus = models.CharField(max_length=255, blank=True, null=True)
    prsepis = models.CharField(max_length=255, blank=True, null=True)
    dprna = models.IntegerField(blank=True, null=True)
    dprbun = models.IntegerField(blank=True, null=True)
    dprcreat = models.IntegerField(blank=True, null=True)
    dpralbum = models.IntegerField(blank=True, null=True)
    dprbili = models.IntegerField(blank=True, null=True)
    dprsgot = models.IntegerField(blank=True, null=True)
    dpralkph = models.IntegerField(blank=True, null=True)
    dprwbc = models.IntegerField(blank=True, null=True)
    dprhct = models.IntegerField(blank=True, null=True)
    dprplate = models.IntegerField(blank=True, null=True)
    dprptt = models.IntegerField(blank=True, null=True)
    dprpt = models.IntegerField(blank=True, null=True)
    dprinr = models.IntegerField(blank=True, null=True)
    prsodm = models.FloatField(blank=True, null=True)
    prbun = models.FloatField(blank=True, null=True)
    prcreat = models.FloatField(blank=True, null=True)
    pralbum = models.FloatField(blank=True, null=True)
    prbili = models.FloatField(blank=True, null=True)
    prsgot = models.FloatField(blank=True, null=True)
    pralkph = models.FloatField(blank=True, null=True)
    prwbc = models.FloatField(blank=True, null=True)
    prhct = models.FloatField(blank=True, null=True)
    prplate = models.FloatField(blank=True, null=True)
    prptt = models.FloatField(blank=True, null=True)
    prinr = models.FloatField(blank=True, null=True)
    prpt = models.IntegerField(blank=True, null=True)
    otherproc1 = models.CharField(max_length=255, blank=True, null=True)
    othercpt1 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu1 = models.FloatField(blank=True, null=True)
    otherproc2 = models.CharField(max_length=255, blank=True, null=True)
    othercpt2 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu2 = models.FloatField(blank=True, null=True)
    otherproc3 = models.CharField(max_length=255, blank=True, null=True)
    othercpt3 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu3 = models.FloatField(blank=True, null=True)
    otherproc4 = models.CharField(max_length=255, blank=True, null=True)
    othercpt4 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu4 = models.FloatField(blank=True, null=True)
    otherproc5 = models.CharField(max_length=255, blank=True, null=True)
    othercpt5 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu5 = models.FloatField(blank=True, null=True)
    otherproc6 = models.CharField(max_length=255, blank=True, null=True)
    othercpt6 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu6 = models.FloatField(blank=True, null=True)
    otherproc7 = models.CharField(max_length=255, blank=True, null=True)
    othercpt7 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu7 = models.FloatField(blank=True, null=True)
    otherproc8 = models.CharField(max_length=255, blank=True, null=True)
    othercpt8 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu8 = models.FloatField(blank=True, null=True)
    otherproc9 = models.CharField(max_length=255, blank=True, null=True)
    othercpt9 = models.CharField(max_length=255, blank=True, null=True)
    otherwrvu9 = models.FloatField(blank=True, null=True)
    otherproc10 = models.CharField(max_length=255, blank=True, null=True)
    othercpt10 = models.FloatField(blank=True, null=True)
    otherwrvu10 = models.FloatField(blank=True, null=True)
    concurr1 = models.CharField(max_length=255, blank=True, null=True)
    concpt1 = models.CharField(max_length=255, blank=True, null=True)
    conwrvu1 = models.FloatField(blank=True, null=True)
    concurr2 = models.CharField(max_length=255, blank=True, null=True)
    concpt2 = models.CharField(max_length=255, blank=True, null=True)
    conwrvu2 = models.FloatField(blank=True, null=True)
    concurr3 = models.CharField(max_length=255, blank=True, null=True)
    concpt3 = models.CharField(max_length=255, blank=True, null=True)
    conwrvu3 = models.FloatField(blank=True, null=True)
    concurr4 = models.CharField(max_length=255, blank=True, null=True)
    concpt4 = models.CharField(max_length=255, blank=True, null=True)
    conwrvu4 = models.FloatField(blank=True, null=True)
    concurr5 = models.CharField(max_length=255, blank=True, null=True)
    concpt5 = models.FloatField(blank=True, null=True)
    conwrvu5 = models.FloatField(blank=True, null=True)
    concurr6 = models.CharField(max_length=255, blank=True, null=True)
    concpt6 = models.CharField(max_length=255, blank=True, null=True)
    conwrvu6 = models.FloatField(blank=True, null=True)
    concurr7 = models.CharField(max_length=255, blank=True, null=True)
    concpt7 = models.FloatField(blank=True, null=True)
    conwrvu7 = models.FloatField(blank=True, null=True)
    concurr8 = models.CharField(max_length=255, blank=True, null=True)
    concpt8 = models.FloatField(blank=True, null=True)
    conwrvu8 = models.FloatField(blank=True, null=True)
    concurr9 = models.CharField(max_length=255, blank=True, null=True)
    concpt9 = models.FloatField(blank=True, null=True)
    conwrvu9 = models.FloatField(blank=True, null=True)
    concurr10 = models.CharField(max_length=255, blank=True, null=True)
    concpt10 = models.FloatField(blank=True, null=True)
    conwrvu10 = models.FloatField(blank=True, null=True)
    emergncy = models.CharField(max_length=255, blank=True, null=True)
    wndclas = models.CharField(max_length=255, blank=True, null=True)
    asaclas = models.CharField(max_length=255, blank=True, null=True)
    mortprob = models.FloatField(blank=True, null=True)
    morbprob = models.FloatField(blank=True, null=True)
    optime = models.IntegerField(blank=True, null=True)
    hdisdt = models.IntegerField(blank=True, null=True)
    yrdeath = models.IntegerField(blank=True, null=True)
    tothlos = models.IntegerField(blank=True, null=True)
    admqtr = models.IntegerField(blank=True, null=True)
    htooday = models.FloatField(blank=True, null=True)
    nsupinfec = models.IntegerField(blank=True, null=True)
    supinfec = models.CharField(max_length=255, blank=True, null=True)
    sssipatos = models.CharField(max_length=255, blank=True, null=True)
    dsupinfec = models.IntegerField(blank=True, null=True)
    nwndinfd = models.IntegerField(blank=True, null=True)
    wndinfd = models.CharField(max_length=255, blank=True, null=True)
    dssipatos = models.CharField(max_length=255, blank=True, null=True)
    dwndinfd = models.IntegerField(blank=True, null=True)
    norgspcssi = models.IntegerField(blank=True, null=True)
    orgspcssi = models.CharField(max_length=255, blank=True, null=True)
    ossipatos = models.CharField(max_length=255, blank=True, null=True)
    dorgspcssi = models.IntegerField(blank=True, null=True)
    ndehis = models.IntegerField(blank=True, null=True)
    dehis = models.CharField(max_length=255, blank=True, null=True)
    ddehis = models.IntegerField(blank=True, null=True)
    noupneumo = models.IntegerField(blank=True, null=True)
    oupneumo = models.CharField(max_length=255, blank=True, null=True)
    pnapatos = models.CharField(max_length=255, blank=True, null=True)
    doupneumo = models.IntegerField(blank=True, null=True)
    nreintub = models.IntegerField(blank=True, null=True)
    reintub = models.CharField(max_length=255, blank=True, null=True)
    dreintub = models.IntegerField(blank=True, null=True)
    npulembol = models.IntegerField(blank=True, null=True)
    pulembol = models.CharField(max_length=255, blank=True, null=True)
    dpulembol = models.IntegerField(blank=True, null=True)
    nfailwean = models.IntegerField(blank=True, null=True)
    failwean = models.CharField(max_length=255, blank=True, null=True)
    ventpatos = models.CharField(max_length=255, blank=True, null=True)
    dfailwean = models.IntegerField(blank=True, null=True)
    nrenainsf = models.IntegerField(blank=True, null=True)
    renainsf = models.CharField(max_length=255, blank=True, null=True)
    drenainsf = models.IntegerField(blank=True, null=True)
    noprenafl = models.IntegerField(blank=True, null=True)
    oprenafl = models.CharField(max_length=255, blank=True, null=True)
    doprenafl = models.IntegerField(blank=True, null=True)
    nurninfec = models.IntegerField(blank=True, null=True)
    urninfec = models.CharField(max_length=255, blank=True, null=True)
    utipatos = models.CharField(max_length=255, blank=True, null=True)
    durninfec = models.IntegerField(blank=True, null=True)
    ncnscva = models.IntegerField(blank=True, null=True)
    cnscva = models.CharField(max_length=255, blank=True, null=True)
    dcnscva = models.IntegerField(blank=True, null=True)
    ncdarrest = models.IntegerField(blank=True, null=True)
    cdarrest = models.CharField(max_length=255, blank=True, null=True)
    dcdarrest = models.IntegerField(blank=True, null=True)
    ncdmi = models.IntegerField(blank=True, null=True)
    cdmi = models.CharField(max_length=255, blank=True, null=True)
    dcdmi = models.IntegerField(blank=True, null=True)
    nothbleed = models.IntegerField(blank=True, null=True)
    othbleed = models.CharField(max_length=255, blank=True, null=True)
    dothbleed = models.IntegerField(blank=True, null=True)
    nothdvt = models.IntegerField(blank=True, null=True)
    othdvt = models.CharField(max_length=255, blank=True, null=True)
    dothdvt = models.IntegerField(blank=True, null=True)
    nothsysep = models.IntegerField(blank=True, null=True)
    othsysep = models.CharField(max_length=255, blank=True, null=True)
    sepsispatos = models.CharField(max_length=255, blank=True, null=True)
    dothsysep = models.IntegerField(blank=True, null=True)
    nothseshock = models.IntegerField(blank=True, null=True)
    othseshock = models.CharField(max_length=255, blank=True, null=True)
    sepshockpatos = models.CharField(max_length=255, blank=True, null=True)
    dothseshock = models.IntegerField(blank=True, null=True)
    podiag = models.FloatField(blank=True, null=True)
    podiagtx = models.FloatField(blank=True, null=True)
    podiag10 = models.CharField(max_length=255, blank=True, null=True)
    podiagtx10 = models.CharField(max_length=255, blank=True, null=True)
    returnor = models.CharField(max_length=255, blank=True, null=True)
    dopertod = models.IntegerField(blank=True, null=True)
    doptodis = models.IntegerField(blank=True, null=True)
    stillinhosp = models.CharField(max_length=255, blank=True, null=True)
    reoperation1 = models.CharField(max_length=255, blank=True, null=True)
    retorpodays = models.IntegerField(blank=True, null=True)
    reoporcpt1 = models.CharField(max_length=255, blank=True, null=True)
    retorrelated = models.CharField(max_length=255, blank=True, null=True)
    reoporicd91 = models.FloatField(blank=True, null=True)
    reopor1icd101 = models.CharField(max_length=255, blank=True, null=True)
    reoperation2 = models.CharField(max_length=255, blank=True, null=True)
    retor2podays = models.IntegerField(blank=True, null=True)
    reopor2cpt1 = models.CharField(max_length=255, blank=True, null=True)
    retor2related = models.CharField(max_length=255, blank=True, null=True)
    reopor2icd91 = models.FloatField(blank=True, null=True)
    reopor2icd101 = models.CharField(max_length=255, blank=True, null=True)
    reoperation3 = models.CharField(max_length=255, blank=True, null=True)
    readmission1 = models.CharField(max_length=255, blank=True, null=True)
    readmpodays1 = models.IntegerField(blank=True, null=True)
    unplannedreadmission1 = models.CharField(max_length=255, blank=True, null=True)
    readmrelated1 = models.CharField(max_length=255, blank=True, null=True)
    readmsuspreason1 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelsusp1 = models.CharField(max_length=255, blank=True, null=True)
    readmrelicd91 = models.FloatField(blank=True, null=True)
    readmrelicd101 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelicd91 = models.FloatField(blank=True, null=True)
    readmunrelicd101 = models.CharField(max_length=255, blank=True, null=True)
    readmission2 = models.CharField(max_length=255, blank=True, null=True)
    readmpodays2 = models.IntegerField(blank=True, null=True)
    unplannedreadmission2 = models.CharField(max_length=255, blank=True, null=True)
    readmrelated2 = models.CharField(max_length=255, blank=True, null=True)
    readmsuspreason2 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelsusp2 = models.FloatField(blank=True, null=True)
    readmrelicd92 = models.FloatField(blank=True, null=True)
    readmrelicd102 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelicd92 = models.FloatField(blank=True, null=True)
    readmunrelicd102 = models.FloatField(blank=True, null=True)
    readmission3 = models.CharField(max_length=255, blank=True, null=True)
    readmpodays3 = models.IntegerField(blank=True, null=True)
    unplannedreadmission3 = models.CharField(max_length=255, blank=True, null=True)
    readmrelated3 = models.CharField(max_length=255, blank=True, null=True)
    readmsuspreason3 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelsusp3 = models.FloatField(blank=True, null=True)
    readmrelicd93 = models.FloatField(blank=True, null=True)
    readmrelicd103 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelicd93 = models.FloatField(blank=True, null=True)
    readmunrelicd103 = models.FloatField(blank=True, null=True)
    readmission4 = models.CharField(max_length=255, blank=True, null=True)
    readmpodays4 = models.IntegerField(blank=True, null=True)
    unplannedreadmission4 = models.CharField(max_length=255, blank=True, null=True)
    readmrelated4 = models.CharField(max_length=255, blank=True, null=True)
    readmsuspreason4 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelsusp4 = models.FloatField(blank=True, null=True)
    readmrelicd94 = models.FloatField(blank=True, null=True)
    readmrelicd104 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelicd94 = models.FloatField(blank=True, null=True)
    readmunrelicd104 = models.FloatField(blank=True, null=True)
    readmission5 = models.CharField(max_length=255, blank=True, null=True)
    readmpodays5 = models.IntegerField(blank=True, null=True)
    unplannedreadmission5 = models.CharField(max_length=255, blank=True, null=True)
    readmrelated5 = models.CharField(max_length=255, blank=True, null=True)
    readmsuspreason5 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelsusp5 = models.FloatField(blank=True, null=True)
    readmrelicd95 = models.FloatField(blank=True, null=True)
    readmrelicd105 = models.CharField(max_length=255, blank=True, null=True)
    readmunrelicd95 = models.FloatField(blank=True, null=True)
    readmunrelicd105 = models.FloatField(blank=True, null=True)
    wound_closure = models.CharField(max_length=255, blank=True, null=True)
    podiag_other = models.FloatField(blank=True, null=True)
    podiag_other10 = models.CharField(max_length=255, blank=True, null=True)
    anesthes_other = models.CharField(max_length=255, blank=True, null=True)
    othcdiff = models.CharField(max_length=255, blank=True, null=True)
    nothcdiff = models.IntegerField(blank=True, null=True)
    dothcdiff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nsqip2018'
