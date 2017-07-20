#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017-3-9

@author: yuql
'''

from abcbase import DataSrcFactory, SecurityDataSrcBase
import sys
from until.tools import getPrettyTable,getMarkDownTable, sendTable
#DS_CLASS_PATH = "jqds.JqDatasrc"
#DS_CLASS_NAME = "joinquant"
DS_CLASS_PATH = "datasrc.tsprovider.tushare69ds.TsDatasrc"
DS_CLASS_NAME = "tushare"

dsfactory = DataSrcFactory.getFrom(DS_CLASS_PATH,DS_CLASS_NAME)
dsobj = dsfactory.getDataSrc()
print dir(dsobj)

def MACD_CN(close, fastperiod=12, slowperiod=26, signalperiod=9) :
    return SecurityDataSrcBase.MACD_CN(close, fastperiod, slowperiod, signalperiod)

def KDJ_CN(high, low, close, fastk_period=9, slowk_period=3, fastd_period=3):
    return SecurityDataSrcBase.KDJ_CN(high, low, close, fastk_period, slowk_period, fastd_period)

def CCI_CN(high, low, close, timeperiod=14):
    return SecurityDataSrcBase.CCI_CN(high, low, close, timeperiod)

def GET_RUN_MINUTES(context):
    return SecurityDataSrcBase.GET_RUN_MINUTES(context)

def CROSS_LAST_COUNT(src, crossval, crossup=True):
    return SecurityDataSrcBase.CROSS_LAST_COUNT(src, crossval, crossup)

def STD_DATA_DAY(security, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, dataCount)
    return ret

def STD_DAY(security, ref=0, data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, ref, data)
    return ret


def BOLL_DAY_STATE(security, data={}):
    curname = sys._getframe().f_code.co_name
    return dsobj.invokeMethod(curname, security, data)

def BOLL_DATA_DAY(security, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, dataCount)
    return ret
    
def BOLL_DAY(security, ref=0, data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, ref, data)
    return ret

def BOLL_STATE(context, security, freq = 30, data={}):
    curname = sys._getframe().f_code.co_name
    return dsobj.invokeMethod(curname, context, security, freq, data)

def WR_DAY(context, security, timeperiod=9, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, timeperiod, ref)
    return ret

def WR_DATA_DAY(context, security, timeperiod=9, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, timeperiod, dataCount)
    return ret

def RSI_DAY(security, timeperiod=6, data={}, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, timeperiod, data, ref)
    return ret

def RSI_DATA_DAY(security, timeperiod=6, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, timeperiod, data, dataCount)
    return ret

def KDJ_DAY(security, data={}, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, ref)
    return ret

def KDJ_DATA_DAY(security, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, dataCount)
    return ret

def KDJ_DATA(context, security, freq = 'D', data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, freq, data, dataCount)
    return ret

def GET_WAVE_CRYPTO(context, security, period = 'D', data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, period, data)
    return ret

def GET_INERT_CRYPTO(context, security, period = 'D', data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, period, data)
    return ret

def GET_BUNDLE(context, security, crypto=False):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, crypto)
    return ret

def CCI_DAY(security, data={}, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, ref)
    return ret

def CCI_DATA_DAY(security, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, data, dataCount)
    return ret

def CCI_DATA(context, security, freq = 'D', data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, freq, data, dataCount)
    return ret

def MA_N_DAY(security, n=5, ref=0, data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, n, ref, data)
    return ret

def MA_N_DATA_DAY(security, n=5, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, n, data, dataCount)
    return ret
    
def MAVOL_N_DAY(context, security, n=5, ref=0, data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, n, ref, data)
    return ret

def MAVOL_N_DATA_DAY(context,security, n=5, data={}, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, n, data, dataCount)
    return ret

def VOL_PRE(context, security, data={}, isFix=True):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, data, isFix)
    return ret

def VOL_PV(context, security, n=20, data={}, isFix=True):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, n, data, isFix)
    return ret

# 获取所有股票代码
#return list
def GET_ALL_SECURITIES(filtPaused=True, filtSt=True):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname,filtPaused,filtSt)
    return ret

# 获取股票信息
#security
def GET_SECURITY_INFO(security):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security)
    return ret
    
# 获取当前分时收盘价
#context, security, data={}, freq=5, dataCount=1
def GET_CLOSE_DATA_INTRADAY(context, security, data={}, freq=5, dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, data, freq, dataCount)
    return ret

#context, security, ref=0
def GET_HIGH_DAY(context, security, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, ref)
    return ret
        
#context, security, ref=0
def GET_LOW_DAY(context, security, ref=0):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, ref)
    return ret
        
# 获取日线历史数据最大值
#context,security,isLastest=True,data={},dataCount=1
def GET_HIGH_DATA_DAY(context,security,isLastest=True,data={},dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context,security,isLastest,data,dataCount)
    return ret

# 获取日线历史数据最小值
#context,security,isLastest=True,data={},dataCount=1
def GET_LOW_DATA_DAY(context,security,isLastest=True,data={},dataCount=1):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context,security,isLastest,data,dataCount)
    return ret

# 获取当前日线或ref天前收盘价
#security, ref=0 ,data={}
def GET_CLOSE_DAY(security, ref=0 ,data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security, ref ,data)
    return ret

#security,isLastest=True,data={},dataCount=20
# 获取日线历史数据
def GET_CLOSE_DATA_DAY(security,isLastest=True,data={},dataCount=20):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, security,isLastest,data,dataCount)
    return ret
   
# 获取日线周线月线收盘价历史数据
#context,security,isLastest=True,data={},dataCount=180*20
#return closeDay, closeMonth, closeWeek
def GET_CLOSE_DATA(context,security,isLastest=True,data={},dataCount=180*20):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context,security,isLastest,data,dataCount)
    return ret

# 获取当前日线或ref天前成交量
#context, security, ref=0 ,data={}
def GET_VOL_DAY(context, security, ref=0 ,data={}):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security, ref,data)
    return ret

# 获取日线历史成交量
#context, security,isLastest=True,data={},dataCount=20
def GET_VOL_DATA_DAY(context, security,isLastest=True,data={},dataCount=20):
    curname = sys._getframe().f_code.co_name
    ret = dsobj.invokeMethod(curname, context, security,isLastest,data,dataCount)
    return ret


#静态方法公用工具类
class DSUtil(object):
    
    @staticmethod
    def getConfigLoader():
        if (DS_CLASS_NAME == 'joinquant'):
            return dsobj.getConfigLoader()
        return None
    
    @staticmethod
    def sendSecurities(context, stocks, cryptal=False, sendMail=True):
        if len(stocks) == 0:
            return
        bundleList= []
        for security in stocks:
            print "%s bundle..." % (security)
            bundle = GET_BUNDLE(context, security,cryptal)
            bundleList.append(bundle)
        #schema = ['code','name','industry','close','wave','inert']
        schema = ['code','name','industry','close']
        table = getPrettyTable(bundleList, schema) 
        print table
        mdtable = getMarkDownTable(bundleList, schema)
        print mdtable
        configloader = DSUtil.getConfigLoader()
        if sendMail:
            sendTable(DS_CLASS_NAME, bundleList, schema, configloader.getEmailConfig() if (configloader != None) else None)
        return table