# -*- coding: utf-8 -*
# __author__ = 'wangdiyi'
import numpy as np
from math import *
from alldata import dataset
from schoolname import affiliationName

affiliationIDs =set(['0003B055',
 '0005FC5A',
 '000CF342',
 '0011114D',
 '0011EAC4',
 '0014A048',
 '001C3B8F',
 '00243975',
 '0027E0B8',
 '002932B0',
 '003BDEE2',
 '003E7116',
 '00433890',
 '0045D019',
 '0045D9F6',
 '00493E54',
 '004B1FBC',
 '004CA7A3',
 '004E3300',
 '005237C4',
 '0056B275',
 '006329B3',
 '006952C5',
 '00725F06',
 '0073ECCC',
 '00784876',
 '007B4591',
 '007B68B5',
 '007D2F41',
 '008ED3A6',
 '0092C1B8',
 '00962EEC',
 '009779A9',
 '009F903A',
 '00A3C9C2',
 '00A52A7E',
 '00A87317',
 '00BBEBAA',
 '00BC8D07',
 '00BDF5D6',
 '00C50601',
 '00C86936',
 '00CC80B3',
 '00CD8766',
 '00CE2969',
 '00D40E2B',
 '00D4F325',
 '00D956B2',
 '00E5C27A',
 '00EE209B',
 '00F1EE39',
 '00F8422C',
 '00F87E5D',
 '00F94921',
 '00F9B76E',
 '00FA1C18',
 '00FB0CDD',
 '00FD6FCE',
 '00FF56A8',
 '0108016A',
 '0108DAB7',
 '01109E6D',
 '01124466',
 '0112E226',
 '01198E98',
 '0126039E',
 '012BCF09',
 '012C9CDF',
 '012E6F4E',
 '012F592B',
 '01328BF3',
 '0134B592',
 '0139FCD5',
 '013A0DA1',
 '01438A3B',
 '01444027',
 '01461554',
 '0147F037',
 '0154426A',
 '0159FE4E',
 '015B46C7',
 '016FC32A',
 '01710C78',
 '01739E09',
 '01776B6C',
 '017889A7',
 '017C99DB',
 '017F2ECE',
 '018A6121',
 '018E2322',
 '0190EC9A',
 '01A17328',
 '01A842AA',
 '01A8C383',
 '01AE4F56',
 '01AFAF1B',
 '01B2BC70',
 '01C3C549',
 '01C5C92C',
 '01C641C3',
 '01D5887E',
 '01DF6D2D',
 '01E0D8CE',
 '01E46A0B',
 '01E93C2F',
 '01EE4B98',
 '01F164D0',
 '01F1D439',
 '01F6ADD2',
 '01F71AD0',
 '01FACAD8',
 '01FB725A',
 '01FE29EA',
 '02066FCD',
 '0216C308',
 '021B9D77',
 '021CC5D8',
 '0228E4F2',
 '02290965',
 '0229448F',
 '022B685F',
 '022F9467',
 '023B9EF3',
 '0240B99C',
 '025139D2',
 '02585490',
 '0259891E',
 '025B9122',
 '025D2C19',
 '025F5CB1',
 '0262EA12',
 '02642F55',
 '026778A2',
 '0267A61E',
 '027426D0',
 '028E8644',
 '028F2298',
 '0294EAD4',
 '02965656',
 '0296D744',
 '02AA1FA9',
 '02AD1047',
 '02AD820C',
 '02B09E25',
 '02B1C5D7',
 '02B49FCD',
 '02B554FC',
 '02B911E0',
 '02BCD1A8',
 '02C7065C',
 '02D4CE98',
 '02D4EDF8',
 '02D66721',
 '02D828C1',
 '02D9A7F2',
 '02DB0F2D',
 '02E90378',
 '03006309',
 '03099350',
 '0312B01D',
 '031AFA6D',
 '031C31BE',
 '031EE95E',
 '03376F29',
 '03496C27',
 '0349EE07',
 '034F3208',
 '0352694C',
 '03528CBA',
 '0352F953',
 '035786DA',
 '035F81F4',
 '03672BD5',
 '0368D319',
 '0368E8BE',
 '037D28F2',
 '03839B48',
 '03839CF8',
 '0388650E',
 '0389C918',
 '038AE3AA',
 '038CB6F6',
 '039459BF',
 '03959311',
 '0395F208',
 '039DB9B6',
 '03A194FC',
 '03A8769C',
 '03AC92A1',
 '03B6E7B2',
 '03B817A9',
 '03BF901A',
 '03C0079C',
 '03C2CC97',
 '03C3607B',
 '03C436D1',
 '03CAFC05',
 '03D00B37',
 '03D09CA7',
 '03E298B8',
 '03EB6D7F',
 '03FA8F1E',
 '03FC3F40',
 '03FC4F79',
 '03FCE859',
 '03FD8454',
 '040F37A8',
 '0412EAF6',
 '0413757D',
 '041B3329',
 '041C3083',
 '04281A41',
 '0437D79B',
 '043A55FE',
 '043B1E1B',
 '043F7F1E',
 '04496BAA',
 '044C0559',
 '045716B5',
 '04592826',
 '045C11B3',
 '045D3373',
 '04634070',
 '046C3B83',
 '0474BFAF',
 '0474FB72',
 '04756336',
 '0477FFD3',
 '0478D4F8',
 '0486EC92',
 '0489A984',
 '0489F1AC',
 '048AB435',
 '04905D15',
 '04946B1E',
 '049573B2',
 '04AEE5C7',
 '04AF010A',
 '04AF492D',
 '04B01E55',
 '04B5445A',
 '04BE3F72',
 '04BEE6D7',
 '04C30B43',
 '04C3CCF3',
 '04C3E428',
 '04D98949',
 '04EAD036',
 '04F0A8A0',
 '04F1BEA5',
 '04F2C66A',
 '04F353DF',
 '04F99C7A',
 '04FB01B8',
 '04FD6759',
 '0501E2EA',
 '0502A721',
 '050513B0',
 '0507BBD7',
 '050BB43F',
 '0527EA39',
 '05282E0D',
 '052BF631',
 '052F5108',
 '0532D181',
 '0535FE32',
 '05364FE4',
 '0538AC16',
 '05397CB8',
 '053FB310',
 '054B33A5',
 '0555D86A',
 '055B394D',
 '05669A68',
 '056D3FC6',
 '056EA0E2',
 '056FA77A',
 '05776AD7',
 '0578DF46',
 '0581F5D5',
 '0582A04E',
 '059DE5E4',
 '05A21A71',
 '05A3DA1F',
 '05A55A03',
 '05B090CE',
 '05B3DFF1',
 '05B9651E',
 '05BDC90E',
 '05C31D4B',
 '05C86094',
 '05DAB8C0',
 '05DBB954',
 '05DBF710',
 '05DCD65A',
 '05E1B1D9',
 '05E2161B',
 '05E74909',
 '05E79D01',
 '05EDB3A0',
 '05EEE4E0',
 '05EFFB90',
 '05F5F76A',
 '05F6E42A',
 '06041575',
 '06167391',
 '0616AB9C',
 '0617689C',
 '06194FDE',
 '0619822C',
 '061A19CA',
 '061BA55B',
 '061C6C3B',
 '0626251D',
 '062BC2E4',
 '062D596B',
 '06444F84',
 '0653F611',
 '06601420',
 '0661DECB',
 '066A71BC',
 '066AF386',
 '066F2C46',
 '067461C8',
 '06771A5A',
 '0679E020',
 '067C4210',
 '068A7232',
 '068E815A',
 '06918666',
 '06943C23',
 '0699B629',
 '069BF47D',
 '069DA7A7',
 '069F11AE',
 '06ACAD91',
 '06C2C7BC',
 '06CB2E98',
 '06CBC4BA',
 '06CBEAA9',
 '06CCE1C6',
 '06CD3667',
 '06CF160C',
 '06D18AFD',
 '06D27A8D',
 '06D35AFB',
 '06D39D72',
 '06D835C2',
 '06DA7DC2',
 '06DE3FEB',
 '06E63D20',
 '06EB0D45',
 '06F892B4',
 '0708D687',
 '070A58AF',
 '070A9F1F',
 '070DD5D4',
 '070DD774',
 '070DED1B',
 '07103214',
 '071126B7',
 '07162905',
 '072620B4',
 '0733A746',
 '073B94B1',
 '07427AD9',
 '0742D5C5',
 '0743CD5B',
 '074491E2',
 '07454816',
 '0749A315',
 '074ADC51',
 '074B3001',
 '074BDB0A',
 '07511464',
 '0754B26A',
 '0757A922',
 '075ABF1F',
 '0762929E',
 '0764F090',
 '07679147',
 '07681456',
 '077DD57B',
 '077EC9E4',
 '07802943',
 '0782737C',
 '07862589',
 '07874D3C',
 '0787E01C',
 '078981CC',
 '078A8AE9',
 '07930A8B',
 '07A75F52',
 '07B10DCB',
 '07B6A2A8',
 '07B99BFA',
 '07B9F6F5',
 '07BAB9E7',
 '07BC3356',
 '07BDC4B0',
 '07C34834',
 '07CA5884',
 '07CB626B',
 '07D2B6B9',
 '07DA0A1C',
 '07DEF9D7',
 '07F5B6CA',
 '07F892EC',
 '07F8AFEC',
 '07FD08C8',
 '08053B2B',
 '080DBBEF',
 '080E155C',
 '0810AAFA',
 '0815134D',
 '081E3F30',
 '0830FCA0',
 '0832C111',
 '0837B2CF',
 '083839C7',
 '0839CEE3',
 '083D03E5',
 '08443C72',
 '08495949',
 '084B474F',
 '084D01D3',
 '08548E70',
 '085ADB71',
 '086E5DD5',
 '08702BDB',
 '087095C7',
 '087165E4',
 '0875EA92',
 '087CBF68',
 '087E04C5',
 '088001DA',
 '08802AB2',
 '088A680B',
 '08A948CC',
 '08A97E0C',
 '08ADCF85',
 '08B17323',
 '08B1D62B',
 '08B22DAB',
 '08B4FEC0',
 '08B9DFEF',
 '08BA2180',
 '08BCC883',
 '08D3D0B6',
 '08D69EB4',
 '08D6D550',
 '08D7E515',
 '08E4D2D6',
 '08EAA2CB',
 '08EC4F5B',
 '08ED4AE9',
 '08EF476D',
 '08EF72DE',
 '08F452CF',
 '08F47EBA',
 '08F7F83A',
 '08FB679F',
 '0904612E',
 '090B77B3',
 '091BC727',
 '0922AB66',
 '09266AF0',
 '09299093',
 '092F5EFF',
 '092FD9CF',
 '093304A4',
 '093456D7',
 '0935E318',
 '09368EC9',
 '09396A59',
 '093FC384',
 '0947E863',
 '0948C934',
 '09490884',
 '094DB5D4',
 '095FFF3F',
 '09630970',
 '09641F67',
 '0965EC45',
 '0966B229',
 '09676E2E',
 '097CD675',
 '09988D7C',
 '09989277',
 '09995E41',
 '099A4032',
 '099BC521',
 '099D876D',
 '09B0BBA7',
 '09B2D407',
 '09B48D0B',
 '09B52E07',
 '09B97DFE',
 '09D7E4FA',
 '09DC92C5',
 '09DD720A',
 '09DDAA88',
 '09DE2F57',
 '09E0E324',
 '09E1988B',
 '09E1E653',
 '09E3EE34',
 '09EA1A37',
 '09EB15AA',
 '09EB4F00',
 '09F18F79',
 '09F90C50',
 '09FD03AD',
 '0A08EC51',
 '0A0D2BAD',
 '0A0E755C',
 '0A0FF9EB',
 '0A10A938',
 '0A1560D3',
 '0A15C811',
 '0A1AB335',
 '0A2510E5',
 '0A254897',
 '0A296B1E',
 '0A2A1FC3',
 '0A2FAFA5',
 '0A398D80',
 '0A475496',
 '0A4ACFBD',
 '0A520111',
 '0A567B93',
 '0A575E93',
 '0A5D91BE',
 '0A5DAC76',
 '0A63B3A3',
 '0A6604CB',
 '0A6C6FB4',
 '0A8478AE',
 '0A968F8B',
 '0A97E0C1',
 '0A990BE9',
 '0A9A3087',
 '0AA2F1D8',
 '0AAEC4EC',
 '0AB1BE73',
 '0AC1438B',
 '0AC5ACB1',
 '0AC8F2B8',
 '0AC9113B',
 '0ACD6604',
 '0ACED25B',
 '0ACF14C4',
 '0ACF7BFE',
 '0ACFCEA7',
 '0AD224B5',
 '0AD3BA36',
 '0ADC5821',
 '0AE14045',
 '0AE9651A',
 '0B002509',
 '0B003FA6',
 '0B00BA67',
 '0B017C0B',
 '0B0338EC',
 '0B054663',
 '0B05FE67',
 '0B08755E',
 '0B0ADEB6',
 '0B0DA3DC',
 '0B185497',
 '0B1B8D25',
 '0B23C19B',
 '0B23EC19',
 '0B2D8123',
 '0B317C57',
 '0B3B54E4',
 '0B3CDF24',
 '0B40411E',
 '0B46561F',
 '0B46563B',
 '0B46E8A6',
 '0B4B5593',
 '0B4EC93C',
 '0B54FBF6',
 '0B659C39',
 '0B78A057',
 '0B78A521',
 '0B7A84D3',
 '0B7D39A1',
 '0B845BA3',
 '0B86525A',
 '0B890E85',
 '0B8B0D91',
 '0B908117',
 '0BB2E102',
 '0BBB6080',
 '0BC0A2DC',
 '0BC0E906',
 '0BC1D058',
 '0BC22D41',
 '0BC2EB17',
 '0BC3491B',
 '0BC7337B',
 '0BCE997F',
 '0BF6BC56',
 '0BF77E37',
 '0BF79DFE',
 '0BF8A745',
 '0C01DCFD',
 '0C14EACF',
 '0C1EB600',
 '0C21380B',
 '0C280BFF',
 '0C2AE079',
 '0C2C9DD2',
 '0C2DEF79',
 '0C2FE58D',
 '0C309CF2',
 '0C33D1B1',
 '0C33EF81',
 '0C34AB7F',
 '0C37CBAD',
 '0C3BAC1F',
 '0C42C8D3',
 '0C4400FF',
 '0C55BCAD',
 '0C601A7F',
 '0C629EED',
 '0C6703C3',
 '0CA4B187',
 '0CECE932',
 '0D109F83',
 '0D52D485',
 '0D57443D',
 '0D8F2D0E',
 '0DC52CFD',
 '0F36910E',
 '1F2989F0',
 '2BECA4ED',
 '3333E44B',
 '335ED749',
 '33865634',
 '339CD1B3',
 '33CD4141',
 '34190567',
 '345C2848',
 '348EB203',
 '34C238D5',
 '34DF872C',
 '34ED541F',
 '34F273FD',
 '350410CF',
 '35095641',
 '35170767',
 '351E811C',
 '358A0AB5',
 '35BD5C33',
 '35E9831D',
 '36E22876',
 '36E5AE3D',
 '3709B4C3',
 '373A6845',
 '4C5370B9',
 '4C6E8511',
 '4C7A9B63',
 '4C7D4F86',
 '4C81D300',
 '4CC3C85D',
 '4CC89935',
 '4CD2C7C1',
 '4CD3CC33',
 '4CDC36DD',
 '4CDD5BAE',
 '4CE6FC2D',
 '4CF99586',
 '4D07390E',
 '4D0FB79F',
 '4D1FB58D',
 '4D2B1EE6',
 '4D5D795C',
 '4D634C00',
 '4D66E94F',
 '4D68F3D7',
 '4D71CB46',
 '4D7B0467',
 '4D8B08D7',
 '4D8C4F7A',
 '4D91A54A',
 '4DA444BF',
 '4DADEF94',
 '4DBAC46F',
 '4DCCAA64',
 '4DDC055F',
 '4DDE3B69',
 '4DF15CEF',
 '4DFEDD28',
 '4E045540',
 '4E0DE25A',
 '4E1BA375',
 '4E1BB800',
 '4E286443',
 '4E2EC568',
 '4E3BBB83',
 '4E47B81B',
 '4E636137',
 '4E718DAA',
 '4E78BE27',
 '4EBC7FCF',
 '4EC97A4B',
 '4ECD74BC',
 '4EDF3BB0',
 '4EEE5722',
 '4EF77785',
 '4F05DC4B',
 '4F076E00',
 '4F10C1EB',
 '4F1AE805',
 '4F3BE6AD',
 '4F4B6B43',
 '4F51463F',
 '4F872588',
 '4F8CCD61',
 '4FA5C415',
 '4FB0218B',
 '4FF45383',
 '4FF7CE5C',
 '500B3463',
 '500F4F9C',
 '8620BB61',
 '8623AC36',
 '8626355D',
 '86263FDB',
 '862979F8',
 '862ADA3F',
 '86317390',
 '863479D1',
 '86349B09',
 '86366AC3',
 '863B5D1F',
 '863BFDE1',
 '863C435D'])


LENGTH_TRAIN = 0
LENGTH_TEST = 0

LEARNING_RATE = 0.00001
LAMBDA = 0.1
TRAIN = []
TEST = []
# WEIGHT_VECTOR = np.random.randn(6)
WEIGHT_VECTORS = {}


TRUE_RANK_2014 = {}
TRUE_RANK_2015 = {}
IDCG_2014 = 0.0
IDCG_2015 = 0.0

def pre_data():
    # randomly init CONFS and SCHOOLS
    # school_list = range(100)
    # conf_list = ["KDD","ICDM","CVPR","AAAI","ICDL","ICML"]
    # [[school_name, conference_name], [f1, f2, f3, f4], X]
    global LENGTH_TEST
    global LENGTH_TRAIN
    global TRUE_RANK_2014
    global TRUE_RANK_2015
    global IDCG_2014
    global IDCG_2015


    whole_rank_2014 = {}
    whole_rank_2015 = {}
    # data = {("CMU","KDD"):[[2011],[2012],[2013],[2014],[2015]]}
    # 2011 : [f1 f2 f3 f4 f5 ranking score]
    for key in affiliationIDs:
        conf = 'KDD'
        school = key
        f_2011 = dataset[(key, conf, '2011')]
        f_2012 = dataset[(key, conf, '2012')]
        f_2013 = dataset[(key, conf, '2013')]
        f_2014 = dataset[(key, conf, '2014')]
        f_2015 = dataset[(key, conf, '2015')]
        WEIGHT_VECTORS[(key,conf)] = np.zeros(6)
        whole_rank_2014[key] = f_2014[5]
        whole_rank_2015[key] = f_2015[5]

        train_feature = list_add(f_2011,f_2012, f_2013)
        test_feature = list_add(f_2012, f_2013, f_2014)

        train_data = [key,train_feature,f_2014[5]]
        test_data = [key,test_feature,f_2015[5]]

        TRAIN.append(train_data)
        TEST.append(test_data)


    # the sorted list of key according to its value.
    # true top 20 school in 2014 and 2015
    rank_2014 = sorted(whole_rank_2014, key = whole_rank_2014.__getitem__)[::-1][:20]
    rank_2015 = sorted(whole_rank_2015, key = whole_rank_2015.__getitem__)[::-1][:20]

    # build up the dictionary for top 20 school
    # TRUE_RANK["CMU"] = (rank_value, rank_position)
    for i in range(len(rank_2014)):
        TRUE_RANK_2014[rank_2014[i]] = (whole_rank_2014[rank_2014[i]],i+1)

    for school in TRUE_RANK_2014:
        IDCG_2014 += TRUE_RANK_2014[school][0]/(log(TRUE_RANK_2014[school][1]+1)/log(2))

    for i in range(len(rank_2015)):
        TRUE_RANK_2015[rank_2015[i]] = (whole_rank_2015[rank_2015[i]],i+1)

    for school in TRUE_RANK_2015:
        IDCG_2015 += TRUE_RANK_2015[school][0]/(log(TRUE_RANK_2015[school][1]+1)/log(2))

    LENGTH_TEST = len(TEST)
    LENGTH_TRAIN = len(TRAIN)

    return


def list_add(l1,l2,l3):
    result = []
    for i in range(len(l1)):
        result.append(l1[i]+l2[i]+l3[i])
    return result


def train():
    # [[school_name,conference_name],[f1,f2,f3,f4],X]
    global WEIGHT_VECTORS

    whole_rank_2014 = {}
    total_diff = 0.0
    for data in TRAIN:
        weight = WEIGHT_VECTORS[(data[0],'KDD')]
        real_score = data[2] * 1.0
        feature_vector = np.array(data[1])
        predict_score = np.dot(feature_vector,weight)
        whole_rank_2014[data[0]] = predict_score
        diff = predict_score - real_score

        # calculate delta for w c_j s_i
        dw = diff * feature_vector
        total_diff += abs(diff)
        # update
        WEIGHT_VECTORS[(data[0], 'KDD')] += -LEARNING_RATE*(dw + LAMBDA*weight)

    rank_result = sorted(whole_rank_2014, key=whole_rank_2014.__getitem__)[::-1]
    print rank_result
    evalutate(rank_result, IDCG_2014,TRUE_RANK_2014)
    # print WEIGHT_VECTOR
    return total_diff/LENGTH_TRAIN


def test():

    global WEIGHT_VECTORS

    # [[school_name,conference_name],[f1,f2,f3,f4],X]
    whole_rank_2015 = {}
    total_diff = 0.0
    for data in TEST:
        weight = WEIGHT_VECTORS[(data[0],'KDD')]
        real_score = data[2] * 1.0
        feature_vector = np.array(data[1])
        predict_score = np.dot(feature_vector, weight)
        whole_rank_2015[data[0]] = predict_score
        diff = predict_score - real_score
        total_diff += abs(diff)
    print "total error on test:%f" % (total_diff/LENGTH_TEST)

    rank_result = sorted(whole_rank_2015,key=whole_rank_2015.__getitem__)[::-1]
    print rank_result
    evalutate(rank_result,IDCG_2015,TRUE_RANK_2015)


def evalutate(rank,i,dic):
    DCG = 0.0
    for school in dic:
        predict_rank = rank.index(school) + 1
        rel = dic[school][0]

        DCG += rel/(log(predict_rank+1)/log(2))

    NDCG = DCG/i
    print NDCG
    return



def learn():

    for iteration in range(30):
        print "*****************************************************************"
        print "Iter %d" % iteration
        print "Testing"
        test()
        print "Training..."
        loss = train()
        print "total error on train:%f" % loss



    return


def basic_info():
    print "LEARNING_RATE = %f" % LEARNING_RATE
    print "LAMBDA = %f" % LAMBDA
    # print "Rank2014"
    # for school in TRUE_RANK_2014:
    #     print affiliationName[school]
    # print "Rank2015"
    # for school in TRUE_RANK_2015:
    #     print affiliationName[school]
    return


def main():
    pre_data()
    basic_info()
    learn()
    print TRUE_RANK_2014
    print TRUE_RANK_2015
    print WEIGHT_VECTORS

if __name__ == '__main__':
    main()


