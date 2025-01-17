## 以下是建立新的 Conda 環境的步驟：

### 1. **建立新的 Conda 環境**
在終端輸入以下命令以創建一個新的 Conda 環境：
```bash
conda create -n my_compression_env python=3.10
```
- `my_compression_env` 是環境的名稱，可以換成你想用的名稱。
- `python=3.10` 是你想要的 Python 版本，可根據需要調整。

激活環境：
```bash
conda activate my_compression_env
```

### 2. **安裝必要的依賴庫**
批量壓縮可能需要使用的庫包括：
- `pillow`：處理圖片。
- `zipfile` 或 `shutil`：壓縮文件。
- `os`：遍歷目錄。

使用以下命令安裝相關依賴：
```bash
pip install pillow
```
（`zipfile` 和 `os` 是 Python 標準庫，無需安裝。）


### 3.匯出專案的 `environment.yml` 檔案
完成環境的配置後，可以用以下命令導出環境
```
conda env export --name my_compression_env > environment.yml
```

## 在其他台電腦下載之後

### 根據 `environment.yml` 的設定創建環境
```
conda env create -f environment.yml
```

