t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
res=t['year'].zfill(4)+'-'+t['month'].zfill(2)+'-'+t['day'].zfill(2)+' '+t['hour'].zfill(2)+':'+t['minute'].zfill(2)+':'+t['second'].zfill(2)
print res