import os
import zipfile

comic_folder = r"C:\Users\weiheng\Desktop\comic"

def compress_subfolders_in_comic(comic_folder):
    """
    將指定 comic_folder 內的每個子資料夾壓縮成單獨的 ZIP 檔案。

    :param comic_folder: 主資料夾的路徑，包含若干子資料夾，每個子資料夾內有圖片文件。
    """
    if not os.path.exists(comic_folder):
        print(f"指定的資料夾 {comic_folder} 不存在！")
        return

    for subfolder_name in os.listdir(comic_folder):
        subfolder_path = os.path.join(comic_folder, subfolder_name)

        if os.path.isdir(subfolder_path):
            print(f"正在壓縮子資料夾: {subfolder_name}...")
            output_zip = os.path.join(comic_folder, f'{subfolder_name}.zip')

            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_STORED) as zipf:
                for root, _, files in os.walk(subfolder_path):
                    for filename in files:
                        file_path = os.path.join(root, filename)

                        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                            # 將圖片存入 ZIP 中，去掉子資料夾的層級
                            arcname = os.path.relpath(file_path, subfolder_path)
                            zipf.write(file_path, arcname)

            print(f"子資料夾 {subfolder_name} 壓縮完成，已保存為 {output_zip}")

if __name__ == "__main__":
    comic_folder = r"C:\Users\weiheng\Desktop\comic"
    
    if os.path.exists(comic_folder):
        compress_subfolders_in_comic(comic_folder)
    else:
        print(f"資料夾 {comic_folder} 不存在，請檢查路徑！")
