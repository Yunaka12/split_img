import cv2
import glob
import os

# 分割したときの画像サイズを計算
def calc_unit(img,h_split,v_split):
    height = img.shape[0]
    width = img.shape[1]
    # 割り切れるとき
    if height%h_split==0 and width%v_split==0:
        h_unit = int(height/h_split)
        w_unit = int(width/v_split)
    else:
        raise ValueError("画像を分割しようとすると余りが生じるよ")
    return h_unit, w_unit

# 指定サイズに画像を分割する（紙に書かないとここは理解できない）
def split_img(img,h_split,v_split,h_unit,w_unit):
    split_img_list=[]
    for i in range(h_split):
        for j in range(v_split):
            # print(h_unit*i,h_unit*(i+1),w_unit*j,w_unit*(j+1))
            split_img = img[h_unit*i:h_unit*(i+1),w_unit*j:w_unit*(j+1),:]
            split_img_list.append(split_img)
    return split_img_list

# 分割した画像たちを保存
def save_img_list(split_img_list,img_name):
    if os.path.exists("split_imgs"):
        pass
    else:
        os.mkdir("split_imgs")
    for i in range(len(split_img_list)):
        cv2.imwrite("./split_imgs/"+img_name+"_"+str(i)+".jpg",split_img_list[i])

def do_split(h_split,v_split,img_path):
    for i in range(len(img_path)):
        img = cv2.imread(img_path[i])
        img_name = os.path.basename(img_path[i]).split(".")[0]
        h_unit,w_unit = calc_unit(img,h_split,v_split)
        split_img_list = split_img(img,h_split,v_split,h_unit,w_unit)
        save_img_list(split_img_list,img_name)



if __name__ == "__main__":
    h_split = 3
    v_split = 2
    img_path = glob.glob("分割する画像のパス")
    do_split(h_split,v_split,img_path)
