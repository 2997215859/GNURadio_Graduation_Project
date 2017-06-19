# GNURadio_Graduation_Project
# 毕设做的GNURadio相关的工作

## 安装说明：
1. 在本地计算机新建文件夹`/home/ruiy/`，在该目录下执行`git clone git@github.com:2997215859/GNURadio_Graduation_Project.git gnuradio`，将在该目录下得到文件夹`gnuradio`。其中包括`gr-ruiy`文件夹和`my-grc`文件夹，前者包括本次毕业设计所写模块，后者中的`bysj1_0.grc`是本次毕业设计的内容。
2. 切到`gr-ruiy/build`目录下，依次执行下列命令
  ```
  $ cmake ../
  $ make
  $ sudo make install
  $ sudo ldconfig
  ```
3. 在GRC中刷新，即可在右侧`ruiy`模块下见到新增的几个Block。有**carrier_offset**、**iqbal_gen_3_0**、**mul_mod**、**nonlinear**四个Block，分别用来产生载波、IQ不平衡、不同调制信号、非线性。其中非线性的算法直接写在了模块中，如果需要更改对信号的处理，需要更改源代码，并重新编译安装。不同Block对应的源文件如下。其他模块也是，修改对应模块的源代码，然后按照步骤2中的操作，重新编译安装即可。
- **carrier_offset** <=> `gr-ruiy/lib/carrier_offset_impl.cc` 和 `carrier_offset_impl.h`
- **iqbal_gen_3_0** <=> `gr-ruiy/python/iqbal_gen_3_0.py`
- **mul_mod** <=> `gr-ruiy/python/mul_mod.py`
- **nonlinear** <=> `gr-ruiy/lib/nonlinear_impl.cc 和 nonlinear_impl.h`

