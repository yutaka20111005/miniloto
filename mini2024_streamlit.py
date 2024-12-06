print('ミニロトヒストグラム作成')
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import streamlit as st

# import mini202401
# import mini202402
# import mini202403
# import mini202404
# import mini202405
# import mini202406
# import mini202407
# import mini202408
# import mini202409
import mini202410
import mini202411
import mini202412

## honsuji = np.concatenate([mini202401.honsuji,mini202402.honsuji,mini202403.honsuji,mini202404.honsuji,mini202405.honsuji,mini202406.honsuji,mini202407.honsuji,mini202408.honsuji,mini202409.honsuji])
honsuji = np.concatenate([mini202410.honsuji,mini202411.honsuji,mini202412.honsuji])


print('先に honsuji の要素数を表示してみる')
print("本数字の個数：",len(honsuji))
print("平均：", round(np.mean(honsuji),2))
print("分散：", round(np.var(honsuji),2))
print("標準偏差：",round(np.std(honsuji),2))


#度数分布表作成
x1 = 1; x2 = 32; nbin = 31
hist,edges = np.histogram(honsuji,range=(x1,x2),bins=nbin)

#階級幅
binw = (x2-x1)/nbin

# matplot棒グラフ描画の準備
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)

# 棒グラフ描画の準備
ax1.set_title('ミニロト　ヒストグラム')
ax1.set_ylim(0,31)
ax1.set_xlim(0,32)
###ax1.bar(edges[:-1],hist,width=0.9*binw)
ax1.bar(edges[:-1],hist,width=1.0*binw)

# 表示する
st.pyplot(fig)
