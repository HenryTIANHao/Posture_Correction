# Posture_Correction
思考拍照角度纠正解决方案:
1.目前的限制条件：
1.1 非正常姿态导致测量误差较大
1.2 自拍信息量有限，且会产生畸变（人体还原？姿态识别？）

2.目前可用的方法：
2.1 runze代码中step3中的轮廓点进行连线并通过线段长度和斜率来判断姿态
2.2 通过openpose等现有方法进行姿态的分析并提示![image](https://user-images.githubusercontent.com/111735121/186069116-1a571977-9393-41b7-afcb-981eaf641586.png)
