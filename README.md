# Covid-19-TaiwanTracker
抓取臺灣Covid-19疫情狀況資料 (Python)

### 如何導入  
建立Package資料夾，放入covid.py  
設定Package路徑
```py
sys.path.append("Package/")
```
在主程式開頭加入此行程式碼
```py
from covid import function_covid as get_covid
```

### 變數
- 病例總數
```py
get_covid().cases
```
- 死亡人數
```py
get_covid().death
```
- 康復人數
```py
get_covid().recovered
```
