以下是建立新的 Conda 環境並用來進行批量壓縮的步驟：

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

### 3. **初始化專案**
建立專案目錄：
```bash
mkdir my_compression_project
cd my_compression_project
```

在此目錄下新建 Python 文件，比如 `compressor.py`，並在文件中編寫壓縮腳本。

### 4. **批量壓縮腳本示例**
以下是一個簡單的 Python 腳本示例，實現批量壓縮目錄中的圖片文件：

```python
import os
from PIL import Image
import zipfile

def compress_images(input_dir, output_dir, zip_name, quality=85):
    # 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)

    # 創建壓縮包
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg')):
                    input_path = os.path.join(root, file)
                    output_path = os.path.join(output_dir, file)

                    # 壓縮圖片
                    img = Image.open(input_path)
                    img.save(output_path, quality=quality, optimize=True)

                    # 添加到壓縮包
                    zipf.write(output_path, os.path.relpath(output_path, output_dir))

if __name__ == "__main__":
    input_directory = "input_images"  # 原始圖片文件夾
    output_directory = "compressed_images"  # 壓縮後的文件夾
    zip_file_name = "compressed_images.zip"  # 壓縮包名稱

    compress_images(input_directory, output_directory, zip_file_name)
    print("批量壓縮完成！")
```

### 5. **運行腳本**
將圖片放到 `input_images` 文件夾下，然後運行腳本：
```bash
python compressor.py
```

### 6. **進一步優化**
如果你的壓縮需求更複雜（例如支持多線程、多格式），可以考慮：
- 使用 `concurrent.futures` 提高效率。
- 將壓縮功能封裝成模塊，便於重複使用。

