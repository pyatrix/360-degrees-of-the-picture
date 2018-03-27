# 360-degrees-of-the-picture
Batch rotates the image 360 degrees and saves it as a file.

(批次將圖片以360度旋轉並儲存為檔案)
 
將程式跟欲處理的圖片放在同一個資料夾中，
處理完的圖片輸出至同一個資料夾。

建議圖片檔名存為數字開頭，
本程式最後會讀取程式本身造成失敗而停止。(有待修改)

需要安裝：opencv(python版)

$ pip install opencv-python
 
 
批次旋轉的使用命令：
$ python Rotate_batch_picture.py

 
旋轉單張的使用命令：
$ python Rotate_one_picture.py lena.jpg
