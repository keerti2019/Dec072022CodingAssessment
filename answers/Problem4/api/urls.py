from django.urls import path
from . import views

urlpatterns = [
    path("weather/<str:date_of_day>/<str:weather_station>", views.GetAllWeatherRecords.as_view()),
    path("yield/<str:year>", views.GetAllYieldData.as_view()),
    path("weather/stats", views.WeatherStats.as_view()),

]

# testurls
#
# http://127.0.0.1:8000/api/weather/1985-01-01/USC00257715
# date_of_day ranges from 1985-01-01 to 2014-12-31 (YYYY-MM-DD)
# http://127.0.0.1:8000/api/yield/1985
# year ranges from 1985-2014
# Weather statistics--added pagination
# http://127.0.0.1:8000/api/weather/stats?start=0&end=60
# http://127.0.0.1:8000/api/weather/stats?start=0&end=60&req_yr=1985
# http://127.0.0.1:8000/api/weather/stats?start=0&end=60&station=USC00121873
# http://127.0.0.1:8000/api/weather/stats?start=0&end=60&req_yr=1985&station=USC00121873

#
# year ranges from 1985-2014/
# station_ids are given by
# USC00257715
# USC00113879
# USC00127935
# USC00112193
# USC00250640
# USC00257070
# USC00114442
# USC00115833
# USC00130133
# USC00132724
# USC00250130
# USC00256970
# USC00116446
# USC00253175
# USC00129113
# USC00134142
# USC00121229
# USC00116526
# USC00259510
# USC00255470
# USC00257515
# USC00258395
# USC00338313
# USC00131402
# USC00118916
# USC00124181
# USC00128036
# USC00126580
# USC00129670
# USC00115943
# USC00124008
# USC00116910
# USC00114108
# USC00127298
# USC00110187
# USC00253365
# USC00251200
# USC00112140
# USC00253615
# USC00255310
# USC00132864
# USC00129511
# USC00118740
# USC00333780
# USC00254900
# USC00255565
# USC00250435
# USC00252020
# USC00138296
# USC00132977
# USC00118147
# USC00250622
# USC00331592
# USC00258915
# USC00250420
# USC00338830
# USC00115515
# USC00120784
# USC00112483
# USC00332098
# USC00116579
# USC00137979
# USC00258480
# USC00258133
# USC00115712
# USC00331152
# USC00335297
# USC00334189
# USC00253660
# USC00137161
# USC00336600
# USC00253715
# USC00338822
# USC00256135
# USC00254440
# USC00132999
# USC00335041
# USC00331541
# USC00135952
# USC00256040
# USC00134735
# USC00123513
# USC00129557
# USC00114198
# USC00252820
# USC00120177
# USC00134894
# USC00130600
# USC00137147
# USC00116610
# USC00126705
# USC00339312
# USC00336196
# USC00134063
# USC00332119
# USC00120200
# USC00258465
# USC00115326
# USC00338769
# USC00116558
# USC00115079
# USC00253735
# USC00333758
# USC00335315
# USC00252205
# USC00125237
# USC00333375
# USC00338552
# USC00132789
# USC00250375
# USC00138688
# USC00115901
# USC00122149
# USC00114823
# USC00110338
# USC00121873
# USC00123527
# USC00127755
# USC00111436
# USC00110072
# USC00131533
# USC00135769
# USC00135796
# USC00119241
# USC00336781
# USC00254110
# USC00253910
# USC00253630
# USC00126001
# USC00255080
# USC00117551
# USC00121747
# USC00127875
# USC00127646
# USC00111280
# USC00121425
# USC00129253
# USC00250070
# USC00252840
# USC00116738
# USC00253035
# USC00130112
# USC00338534
# USC00115768
# USC00131635
# USC00251145
# USC00252100
# USC00119354
# USC00113335
# USC00256570
# USC00124837
# USC00112348
# USC00332791
# USC00336118
# USC00129080
# USC00127522
# USC00125337
# USC00123418
# USC00127482
# USC00121030
# USC00253185
# USC00331072
# USC00120676
# USC00127125
# USC00331890
# USC00254985
# USC00259090
